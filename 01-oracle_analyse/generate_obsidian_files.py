import json
import os
import glob
from config import SCHEMAS


def extract_schema_from_filename(file_path):
    """Extract Oracle schema name from analysis JSON filename."""
    basename = os.path.basename(file_path)
    for schema, tables in SCHEMAS.items():
        for table_name in tables.values():
            if table_name in basename:
                return schema.upper()
    return "UNKNOWN"

def create_markdown_content(item, schema):
    """Builds the Markdown content for a single procedure or view."""
    is_procedure = 'procedure_name' in item
    obj_type = "Procedure" if is_procedure else "View"
    name = item.get('procedure_name') or item.get('view_name')

    content = f"""# {name}

**Schema:** `{schema}` | **Type:** `{obj_type}`

"""

    functionality = item.get('functionality') or item.get('description')
    if functionality:
        content += f"""## Description
{functionality}

"""

    # Helper to generate column tables
    def generate_column_table(columns):
        if not columns:
            return ""

        table_content = ""
        # Check if columns are dicts (detailed) or strings (simple)
        if isinstance(columns[0], dict):
            table_content += "| Column Name | Data Type | Nullable |\n"
            table_content += "|---|---|---|\n"
            for col in columns:
                col_name = col.get('name', 'N/A')
                data_type = col.get('data_type', 'N/A')
                nullable = col.get('nullable', 'N/A')
                table_content += f"| {col_name} | {data_type} | {nullable} |\n"
        else: # Simple list of strings
            table_content += "| Column Name |\n"
            table_content += "|---|\n"
            for col_name in columns:
                table_content += f"| {col_name} |\n"
        return table_content

    data_sources = item.get('data_sources', [])
    if data_sources:
        content += "## Data Sources (Inputs)\n"
        for source in data_sources:
            if isinstance(source, str):
                content += f"- ← [[{source}]]\n"
            elif isinstance(source, dict):
                source_name = source.get('table_name', '')
                columns = source.get('columns', [])
                content += f"- ← [[{source_name}]]\n"
                if columns:
                    content += generate_column_table(columns)
        content += "\n"

    target_tables = item.get('target_tables', [])
    if target_tables:
        content += "## Target Tables (Outputs)\n"
        for target in target_tables:
            table_name = target.get('table_name')
            if table_name:
                columns = target.get('columns', [])
                content += f"- → [[{table_name}]]\n"
                if columns:
                    content += generate_column_table(columns)
        content += "\n"

    return content

def create_markdown_files():
    """
    Parses all '*_analysis.json' files in the current directory, and for each procedure or view,
    creates a Markdown file in a structured 'obsidian_export' directory.
    The Markdown files are formatted for Obsidian, with links for dependencies.
    """
    output_dir = 'obsidian_export'
    procedures_dir = os.path.join(output_dir, 'procedures')
    views_dir = os.path.join(output_dir, 'views')

    os.makedirs(procedures_dir, exist_ok=True)
    os.makedirs(views_dir, exist_ok=True)

    print(f"Output will be saved in '{output_dir}/'")

    json_files = glob.glob('*_analysis.json')
    if not json_files:
        print("No '_analysis.json' files found in the current directory.")
        return

    print(f"Found {len(json_files)} JSON files to process...")

    for file_path in json_files:
        schema = extract_schema_from_filename(file_path)
        print(f"Processing {file_path} (schema: {schema})...")
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"  - Warning: Could not decode JSON from {file_path}. Skipping.")
                continue

            for item in data:
                if 'procedure_name' not in item and 'view_name' not in item:
                    continue

                name = item.get('procedure_name') or item.get('view_name')
                if not name:
                    continue
                
                content = create_markdown_content(item, schema)

                filename = f"{name}.md"
                folder = procedures_dir if 'procedure_name' in item else views_dir
                filepath = os.path.join(folder, filename)

                with open(filepath, 'w') as md_file:
                    md_file.write(content)

    print("Markdown generation complete.")
    print(f"Files are located in '{procedures_dir}/' and '{views_dir}/'.")

if __name__ == '__main__':
    create_markdown_files()
