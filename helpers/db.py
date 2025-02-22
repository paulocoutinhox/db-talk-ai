import json
import os
import uuid

from db.sql_database import SQLDatabase
from helpers import file


def load_databases():
    """Load database configurations from a JSON file."""
    file_path = file.get_databases_file()

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_databases(databases):
    """Save the database configurations to a JSON file."""
    file_path = file.get_databases_file()

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(databases, f, indent=4)


def create_database(db_type, db_url):
    """Create a database connection based on the provided type."""
    if db_type == "sql":
        return SQLDatabase(db_url)
    else:
        raise ValueError(f"❌ Unsupported database type: {db_type}")


def generate_schema(selected_db, databases, db_conn):
    """Generate and save the database schema, updating the configuration if successful."""
    schema_dir = file.get_schemas_folder()
    os.makedirs(schema_dir, exist_ok=True)

    schema_file = selected_db.get("schema", f"{uuid.uuid4()}.txt")
    schema_path = os.path.join(schema_dir, schema_file)

    # Generate the schema using the database connection
    schema_message = db_conn.generate_schema(schema_path)

    if "✅" in schema_message:
        # Update schema key
        selected_db["schema"] = schema_file
        save_databases(databases)

        return True, schema_message
    else:
        return False, schema_message
