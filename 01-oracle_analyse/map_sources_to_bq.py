import json
import os
import glob
import subprocess
import logging

# --- Configuration ---
LOG_LEVEL = logging.INFO
BQ_DATASETS_FILE = 'metadata/bq_datasets_to_scan.txt'
BQ_SCHEMA_CACHE_DIR = 'metadata/schemas'
ORACLE_ANALYSIS_GLOB = '*_analysis.json'
OUTPUT_REPORT_FILE = 'dependency_analysis/output/oracle_to_bq_mapping_report.md'
GCLOUD_CONFIG = 'jobb' # As per project instructions

# --- Logging Setup ---
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

def get_bq_references():
    """Reads project:dataset references from the config file."""
    if not os.path.exists(BQ_DATASETS_FILE):
        logging.error(f"BQ datasets file not found at '{BQ_DATASETS_FILE}'")
        return []
    
    with open(BQ_DATASETS_FILE, 'r') as f:
        references = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    logging.info(f"Found {len(references)} BigQuery references to scan: {references}")
    return references

def run_bq_command(command):
    """Runs a bq command using subprocess and returns the JSON output."""
    # The `bq` tool should automatically use the active gcloud configuration.
    full_command = f"bq {command}"
    try:
        logging.debug(f"Running command: {full_command}")
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running bq command: {command}")
        logging.error(f"Stderr: {e.stderr}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON from bq command output: {e}")
        return None

def fetch_and_cache_bq_schemas(references, force_refresh=False):
    """Fetches schemas for all tables in the given datasets and caches them."""
    os.makedirs(BQ_SCHEMA_CACHE_DIR, exist_ok=True)
    logging.info("Starting BigQuery schema fetch and cache process...")

    for ref in references:
        logging.info(f"Processing reference: {ref}")
        
        # `bq` expects project:dataset, so we replace the first '.' with ':'
        bq_ref = ref.replace('.', ':', 1)
        
        tables_data = run_bq_command(f"ls --format=json --max_results=10000 {bq_ref}")
        if not tables_data:
            logging.warning(f"Could not list tables for {bq_ref}. Skipping.")
            continue

        logging.info(f"Found {len(tables_data)} tables in {bq_ref}.")
        for table_info in tables_data:
            table_id = table_info['tableReference']['tableId']
            # `bq show` needs the full `project:dataset.table` format
            full_table_id = f"{bq_ref}.{table_id}"
            
            # Use a sanitized filename for the cache, based on the `bq` canonical name
            sanitized_ref = bq_ref.replace(':', '_')
            cache_file_path = os.path.join(BQ_SCHEMA_CACHE_DIR, f"{sanitized_ref}_{table_id}.json")

            if os.path.exists(cache_file_path) and not force_refresh:
                logging.debug(f"Schema for {full_table_id} found in cache. Skipping fetch.")
                continue

            logging.info(f"Fetching schema for {full_table_id}...")
            schema_data = run_bq_command(f"show --schema --format=prettyjson {full_table_id}")
            
            if schema_data:
                with open(cache_file_path, 'w') as f:
                    json.dump(schema_data, f, indent=2)
                logging.info(f"Cached schema for {full_table_id} at {cache_file_path}")

    logging.info("BigQuery schema fetching complete.")


if __name__ == '__main__':
    logging.info("--- Starting Oracle to BigQuery Mapping Process ---")
    bq_references = get_bq_references()
    if bq_references:
        fetch_and_cache_bq_schemas(bq_references)
    else:
        logging.warning("No BigQuery references found. Skipping BQ schema fetch.")

    # Next steps will be added here:
    # 1. Load cached BQ schemas
    # 2. Parse Oracle analysis files
    # 3. Perform mapping
    # 4. Generate report
    
    logging.info("--- Script finished (Phase 1: BQ Schema Caching) ---")
