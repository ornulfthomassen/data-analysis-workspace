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


def create_markdown_files():
    """
    Parses all '*_analysis.json' files in the current directory, and for each procedure or view,
    creates a Markdown file in a structured 'obsidian_export' directory.
    The Markdown files are formatted for Obsidian, with links for dependencies.
    """
    # Define the main output directory
    output_dir = 'obsidian_export'
    procedures_dir = os.path.join(output_dir, 'procedures')
    views_dir = os.path.join(output_dir, 'views')

    # Create directories if they don't exist
    os.makedirs(procedures_dir, exist_ok=True)
    os.makedirs(views_dir, exist_ok=True)

    print(f"Output will be saved in '{output_dir}/'")

    # Process all JSON analysis files in the current directory
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
                is_procedure = 'procedure_name' in item
                is_view = 'view_name' in item
                
                if not (is_procedure or is_view):
                    continue

                name = item.get('procedure_name') or item.get('view_name')
                if not name:
                    continue

                # Clean name to be a valid filename
                filename = f"{name}.md"
                folder = procedures_dir if is_procedure else views_dir
                filepath = os.path.join(folder, filename)

                # Start building Markdown content
                obj_type = "Procedure" if is_procedure else "View"
                content = f"""# {name}

**Schema:** `{schema}` | **Type:** `{obj_type}`

"""

                # Add functionality/description
                functionality = item.get('functionality') or item.get('description')
                if functionality:
                    content += f"""## Description
{functionality}

"""

                # Add data sources as links
                data_sources = item.get('data_sources', [])
                if data_sources:
                    content += """## Data Sources (Inputs)
"""
                    for source in data_sources:
                        content += f"""- ← [[{source}]]
"""
                    content += """
"""

                # Add target tables as links
                target_tables = item.get('target_tables', [])
                if target_tables:
                    content += """## Target Tables (Outputs)
"""
                    for target in target_tables:
                        table_name = target.get('table_name')
                        if table_name:
                            content += f"""- → [[{table_name}]]
"""
                    content += """
"""
                
                # Write the content to a .md file
                with open(filepath, 'w') as md_file:
                    md_file.write(content)

    print("Markdown generation complete.")
    print(f"Files are located in '{procedures_dir}/' and '{views_dir}/'.")

if __name__ == '__main__':
    create_markdown_files()
