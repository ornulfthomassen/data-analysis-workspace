import json
import os
import glob
import logging
from collections import defaultdict

# --- Configuration ---
LOG_LEVEL = logging.INFO
ORACLE_ANALYSIS_GLOB = '*_analysis.json'
SCHEMAS_TO_INCLUDE = {'CCM', 'CLM_ADM', 'CLM_CCM', 'CRM_ANALYSE'}
OUTPUT_ROOT_DIR = 'obsidian_export' # Renamed to avoid conflict with `dirs`


# --- Logging Setup ---
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')


def normalize_name(name, schema=None):
    """
    Normalizes an object name to a canonical format: `SCHEMA.OBJECTNAME`.
    Handles case-insensitivity and existing schema prefixes.
    If no schema is in the name, it uses the provided schema context.
    """
    if not name:
        return None
    name_upper = name.upper()
    if '.' in name_upper:
        return name_upper
    if schema:
        return f"{schema.upper()}.{name_upper}"
    return name_upper


def gather_metadata(json_files):
    """
    Pass 1: Read all JSON files to build a complete map of the project.
    """
    defined_objects = set()
    creators_map = defaultdict(lambda: defaultdict(set))
    all_dependencies = set()
    object_data = {}

    logging.info("Starting Pass 1: Gathering metadata from all JSON files...")

    # First, get all defined objects to distinguish internal from external
    for file_path in json_files:
        # Heuristic to find schema from filename, e.g., tnn-consumer-common-nx_temp_ccm_user... -> ccm
        schema_name = os.path.basename(file_path).split('_')[3].upper()
        if schema_name not in SCHEMAS_TO_INCLUDE:
            continue
        with open(file_path, 'r') as f:
            data = json.load(f)
            for item in data:
                name = item.get('procedure_name') or item.get('view_name')
                if name:
                    norm_name = normalize_name(name, schema_name)
                    defined_objects.add(norm_name)
                    object_data[norm_name] = item

    logging.info(f"Found {len(defined_objects)} defined objects.")

    # Now, process dependencies and creators, using the context schema for normalization
    for norm_name, item in object_data.items():
        context_schema = norm_name.split('.')[0]
        
        # Process data sources
        for source in item.get('data_sources', []):
            s_name_raw = source.get('table_name') if isinstance(source, dict) else source
            if s_name_raw:
                all_dependencies.add(normalize_name(s_name_raw, context_schema))

        # Process target tables to find creators
        if 'procedure_name' in item:
            for target in item.get('target_tables', []):
                t_name_raw = target.get('table_name')
                if not t_name_raw:
                    continue
                
                target_norm_name = normalize_name(t_name_raw, context_schema)
                all_dependencies.add(target_norm_name)

                for col in target.get('columns', []):
                    col_name = col.get('name') if isinstance(col, dict) else col
                    if col_name:
                        creators_map[target_norm_name][norm_name].add(col_name)
    
    logging.info(f"Found {len(all_dependencies)} unique dependencies.")
    logging.info(f"Found {len(creators_map)} tables that are created by procedures.")
    return defined_objects, creators_map, all_dependencies, object_data
def generate_column_table(columns):
    """Helper to generate a markdown table for a list of columns."""
    if not columns:
        return ""

    table_content = ""
    # Check if columns are dicts (detailed) or strings (simple)
    if isinstance(columns[0], dict):
        table_content += """| Column Name | Data Type | Nullable |
|---|---|---|
"""
        for col in columns:
            col_name = col.get('name', 'N/A')
            data_type = col.get('data_type', 'N/A')
            nullable = col.get('nullable', 'N/A')
            table_content += f"| {col_name} | {data_type} | {nullable} |\n"
    else:  # Simple list of strings
        table_content += """| Column Name |
|---|
"""
        for col_name in columns:
            table_content += f"| {col_name} |\n"
    return table_content + "\n"


def get_external_output_folder(norm_name, creators_map):
    """
    Determines the correct subfolder for an external object.
    """
    if norm_name in creators_map:
        return "target_tables"
    elif norm_name.endswith(('_V', '_MV')) or '_V_' in norm_name: # Heuristic for views
        return "source_views"
    else:
        return "source_tables"


def generate_markdown_files(defined_objects, creators_map, all_dependencies, object_data):
    """
    Pass 2: Generate all markdown files for both defined and external objects.
    """
    dirs = {
        "views": os.path.join(OUTPUT_ROOT_DIR, 'views'),
        "procedures": os.path.join(OUTPUT_ROOT_DIR, 'procedures'),
        "target_tables": os.path.join(OUTPUT_ROOT_DIR, 'target_tables'),
        "source_views": os.path.join(OUTPUT_ROOT_DIR, 'source_views'),
        "source_tables": os.path.join(OUTPUT_ROOT_DIR, 'source_tables'),
    }
    for d in dirs.values():
        os.makedirs(d, exist_ok=True)

    logging.info("Starting Pass 2: Generating Markdown files...")

    # Generate files for defined objects
    for norm_name, item in object_data.items():
        context_schema, name = norm_name.split('.', 1)
        is_procedure = 'procedure_name' in item
        
        content = f"""# {name}

**Schema:** `{context_schema}` | **Type:** `{'Procedure' if is_procedure else 'View'}`

"""
        if functionality := item.get('functionality') or item.get('description'):
            content += f"""## Description
{functionality}

"""

        if data_sources := item.get('data_sources'):
            content += """## Data Sources (Inputs)
"""
            for source in data_sources:
                s_name_raw = source.get('table_name') if isinstance(source, dict) else source
                s_name_norm = normalize_name(s_name_raw, context_schema)
                content += f"- ← [[{s_name_norm}]]\n"
                if isinstance(source, dict) and source.get('columns'):
                    content += generate_column_table(source['columns'])
            content += "\n"

        if target_tables := item.get('target_tables'):
            content += """## Target Tables (Outputs)
"""
            for target in target_tables:
                t_name_raw = target.get('table_name')
                t_name_norm = normalize_name(t_name_raw, context_schema)
                content += f"- → [[{t_name_norm}]]\n"
                if target.get('columns'):
                    content += generate_column_table(target['columns'])
            content += "\n"

        folder = dirs["procedures"] if is_procedure else dirs["views"]
        filepath = os.path.join(folder, f"{norm_name}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    # Generate files for external objects
    external_objects = all_dependencies - defined_objects
    logging.info(f"Generating {len(external_objects)} external stub files...")
    for norm_name in external_objects:
        output_folder_key = get_external_output_folder(norm_name, creators_map)
        output_folder = dirs[output_folder_key]

        content = f"""# {norm_name}

**Type:** `{output_folder_key.replace('_', ' ').title()}`

"""
        if norm_name in creators_map:
            content += """## Created By
"""
            for creator_norm_name, columns in creators_map[norm_name].items():
                content += f"### → [[{creator_norm_name}]]\n"
                if columns:
                    sorted_cols = sorted(list(columns))
                    content += f"- **Columns ({len(sorted_cols)}):** `" + '`, `'.join(sorted_cols) + "`\n\n"
        
        filepath = os.path.join(output_folder, f"{norm_name}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    """Main function to run the script."""
    # Clean up old directories
    # Only clean the specific subdirectories now
    for dir_name in ['views', 'procedures', 'target_tables', 'source_views', 'source_tables']:
        full_path = os.path.join(OUTPUT_ROOT_DIR, dir_name)
        if os.path.exists(full_path):
            # Remove all files but keep the directory
            for f in os.listdir(full_path):
                os.remove(os.path.join(full_path, f))
        else:
            os.makedirs(full_path, exist_ok=True) # Ensure it exists


    json_files = glob.glob(ORACLE_ANALYSIS_GLOB)
    if not json_files:
        logging.error(f"No analysis files found matching '{ORACLE_ANALYSIS_GLOB}'. Exiting.")
        return

    defined_objects, creators_map, all_dependencies, object_data = gather_metadata(json_files)
    generate_markdown_files(defined_objects, creators_map, all_dependencies, object_data)
    
    logging.info("Markdown generation complete.")
    logging.info(f"Files are located in '{OUTPUT_ROOT_DIR}/'.")

if __name__ == '__main__':
    main()
