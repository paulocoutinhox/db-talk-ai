import pandas as pd
from sqlalchemy import create_engine, inspect, text
from streamlit import error

from .base_database import BaseDatabase

"""
- SQLite:
sqlite:///data/sample.db (relative)
sqlite:///absolute/path/sample.db (absolute)

- PostgreSQL:
postgresql://user:password@host:port/dbname

- MySQL:
mysql://user:password@host:port/dbname
"""


class SQLDatabase(BaseDatabase):
    """SQL database implementation."""

    def __init__(self, db_url):
        super().__init__(db_url)
        self.engine = create_engine(self.db_url)

    def connect(self):
        """Connect to the SQL database."""
        try:
            return self.engine.connect()
        except Exception as e:
            error(f"❌ Error connecting to the database: {e}")
            return None

    def run_query(self, query):
        """Execute a SQL query and return the result."""
        try:
            with self.engine.connect() as conn:
                return pd.read_sql(text(query), conn)
        except Exception as e:
            error(f"❌ Error executing the query: {e}")
            return None

    def get_code_language(self):
        """Get code language."""
        return "sql"

    def get_driver_name(self):
        """Get database driver name."""
        cs_data = self.db_url.split(":")
        return cs_data[0]

    def generate_schema(self, schema_file="schema.txt"):
        """Generates a schema file for the connected database with enhanced details."""
        try:
            inspector = inspect(self.engine)
            tables = inspector.get_table_names()

            if not tables:
                return "⚠️ No tables found in the database."

            schema_details = []

            for table in tables:
                schema_details.append(f"TABLE: {table}\nColumns:")

                # Get column information
                columns = inspector.get_columns(table)
                for col in columns:
                    col_name = col["name"]
                    col_type = col["type"]
                    col_nullable = "NULLABLE" if col["nullable"] else "NOT NULL"
                    col_default = f"DEFAULT {col['default']}" if col["default"] else ""
                    col_pk = "PRIMARY KEY" if col.get("primary_key") else ""
                    col_unique = "UNIQUE" if col.get("unique") else ""

                    # Format column details
                    col_details = f"- {col_name} ({col_type}) {col_pk} {col_unique} {col_nullable} {col_default}".strip()
                    schema_details.append(col_details)

                # Get foreign keys
                foreign_keys = inspector.get_foreign_keys(table)
                if foreign_keys:
                    schema_details.append("\nForeign Keys:")
                    for fk in foreign_keys:
                        fk_column = fk["constrained_columns"][0]
                        ref_table = fk["referred_table"]
                        ref_column = fk["referred_columns"][0]
                        on_delete = f"ON DELETE {fk.get('options', {}).get('ondelete', 'NO ACTION')}".upper()
                        on_update = f"ON UPDATE {fk.get('options', {}).get('onupdate', 'NO ACTION')}".upper()
                        schema_details.append(
                            f"- {fk_column} → {ref_table}.{ref_column} {on_delete} {on_update}"
                        )

                # Get indexes
                indexes = inspector.get_indexes(table)
                if indexes:
                    schema_details.append("\nIndexes:")
                    for idx in indexes:
                        index_name = idx["name"]
                        columns_str = ", ".join(idx["column_names"])
                        is_unique = "UNIQUE" if idx["unique"] else "NON-UNIQUE"
                        schema_details.append(
                            f"- {index_name} ({is_unique}): {columns_str}"
                        )

                # Get triggers (if supported)
                try:
                    with self.engine.connect() as conn:
                        triggers = conn.execute(
                            text(
                                f"SELECT name FROM sqlite_master WHERE type='trigger' AND tbl_name='{table}';"
                            )
                        )
                        triggers = [row[0] for row in triggers]
                        if triggers:
                            schema_details.append("\nTriggers:")
                            for trigger in triggers:
                                schema_details.append(f"- {trigger}")
                except Exception:
                    pass  # Ignore if triggers are not supported

                # Get views (if applicable)
                views = inspector.get_view_names()
                if table in views:
                    schema_details.append("\nVIEW (Readonly Table)")

                schema_details.append("")  # Blank line to separate tables

            # Write the schema to the file
            with open(schema_file, "w", encoding="utf-8") as f:
                f.write("\n".join(schema_details))

            return f"✅ Schema file '{schema_file}' generated successfully."

        except Exception as e:
            return f"❌ Error generating schema: {e}"
