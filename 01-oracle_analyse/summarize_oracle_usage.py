import json
import os
import glob
import logging
from collections import defaultdict

# --- Configuration ---
LOG_LEVEL = logging.INFO
ORACLE_ANALYSIS_GLOB = '*_analysis.json'
OUTPUT_REPORT_FILE = 'dependency_analysis/output/oracle_source_usage_summary.md'
SCHEMAS_TO_INCLUDE = {'CCM', 'CLM_ADM', 'CLM_CCM', 'CRM_ANALYSE'}

# --- Logging Setup ---
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

def get_defined_objects(json_files):
    """
    Parses all analysis files to get a set of all objects (views/procedures)
    that are defined within this project's schemas.
    """
    defined_objects = set()
    for file_path in json_files:
        # Extract schema from filename to correctly qualify the object name
        schema_name = os.path.basename(file_path).split('_')[3].upper() # Heuristic based on filename convention
        if schema_name not in SCHEMAS_TO_INCLUDE:
            continue

        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
                for item in data:
                    name = item.get('procedure_name') or item.get('view_name')
                    if name:
                        defined_objects.add(f"{schema_name}.{name}")
            except json.JSONDecodeError:
                logging.warning(f"Could not decode JSON from {file_path}. Skipping.")
    logging.info(f"Found {len(defined_objects)} defined objects across {len(SCHEMAS_TO_INCLUDE)} schemas.")
    return defined_objects

def analyze_source_usage(json_files, defined_objects):
    """
    Analyzes all JSON files to build a map of external source usage.
    """
    # Structure: { 'SCHEMA.TABLE': { 'total_columns': set(), 'used_by': { 'SCHEMA.VIEW': set() } } }
    usage_data = defaultdict(lambda: {'total_columns': set(), 'used_by': defaultdict(set)})

    for file_path in json_files:
        using_schema_name = os.path.basename(file_path).split('_')[3].upper()
        if using_schema_name not in SCHEMAS_TO_INCLUDE:
            continue

        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue

            for item in data:
                using_object_name = item.get('procedure_name') or item.get('view_name')
                if not using_object_name:
                    continue
                
                full_using_object_name = f"{using_schema_name}.{using_object_name}"

                data_sources = item.get('data_sources', [])
                for source in data_sources:
                    if isinstance(source, str):
                        source_name = source
                        columns = [] # No column info available
                    elif isinstance(source, dict):
                        source_name = source.get('table_name')
                        columns = source.get('columns', [])
                    else:
                        continue
                    
                    if not source_name:
                        continue

                    # If the source is another view/proc from our analyzed schemas, skip it
                    if source_name in defined_objects or source_name.split('.')[0] in SCHEMAS_TO_INCLUDE:
                        continue

                    # We have an external source, let's record the usage
                    for col in columns:
                        # Handle both simple string columns and dict columns
                        col_name = col.get('name') if isinstance(col, dict) else col
                        if col_name:
                            usage_data[source_name]['total_columns'].add(col_name)
                            usage_data[source_name]['used_by'][full_using_object_name].add(col_name)

    logging.info(f"Analysis complete. Found {len(usage_data)} external sources being used.")
    return usage_data

def generate_markdown_report(usage_data):
    """
    Generates a Markdown report from the aggregated usage data.
    """
    report_content = """# Oracle External Source Usage Summary

This report details which external tables and views are used as data sources, and exactly which columns are used by which procedures or views.
"""

    # Sort by source table name for consistent output
    sorted_sources = sorted(usage_data.keys())

    for source_name in sorted_sources:
        data = usage_data[source_name]
        total_cols_sorted = sorted(list(data['total_columns']))
        
        report_content += f"""
## `{source_name}`

**Total Unique Columns Used:** {len(total_cols_sorted)}
"""
        if total_cols_sorted:
            report_content += "- `" + '`, `'.join(total_cols_sorted) + "`\n\n"
        
        report_content += "**Used By:**\n\n"
        
        sorted_users = sorted(data['used_by'].keys())
        for user_name in sorted_users:
            used_cols = sorted(list(data['used_by'][user_name]))
            report_content += f"### `{user_name}`\n"
            if used_cols:
                report_content += f"- **Columns ({len(used_cols)}):** `" + '`, `'.join(used_cols) + "`\n\n"
            else:
                report_content += "- *Usage detected, but no specific columns listed.*\n\n"
        
        report_content += "---\n\n"

    return report_content

if __name__ == '__main__':
    logging.info("--- Starting Oracle Source Usage Analysis ---")
    json_files = glob.glob(ORACLE_ANALYSIS_GLOB)
    if not json_files:
        logging.error("No analysis JSON files found. Exiting.")
    else:
        # Step 1: Find all defined objects to distinguish internal vs. external sources
        defined_objects = get_defined_objects(json_files)
        
        # Step 2: Analyze usage of external sources
        usage_data = analyze_source_usage(json_files, defined_objects)
        
        # Step 3: Generate the report
        report_md = generate_markdown_report(usage_data)
        
        # Step 4: Write the report to a file
        output_dir = os.path.dirname(OUTPUT_REPORT_FILE)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        with open(OUTPUT_REPORT_FILE, 'w') as f:
            f.write(report_md)
            
        logging.info(f"Successfully generated report at: {OUTPUT_REPORT_FILE}")

    logging.info("--- Script finished ---")
