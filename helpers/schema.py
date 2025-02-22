import os

from helpers import file


def load_schema(schema_file):
    if schema_file:
        schema_path = file.get_schema_file(schema_file)

        if os.path.exists(schema_path):
            with open(schema_path, "r", encoding="utf-8") as f:
                return f.read().strip(), None
        else:
            return "", "⚠️ Schema file not found. Generate it first."
    else:
        return "", "⚠️ No schema generated yet."
