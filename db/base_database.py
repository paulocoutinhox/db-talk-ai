from abc import ABC, abstractmethod


class BaseDatabase(ABC):
    """Base class for all database connections."""

    def __init__(self, db_url):
        self.db_url = db_url

    @abstractmethod
    def connect(self):
        """Establish connection with the database."""
        pass

    @abstractmethod
    def run_query(self, query):
        """Run a query and return the result."""
        pass

    @abstractmethod
    def generate_schema(self, schema_file):
        """Generate the database schema and save it to a file."""
        pass

    @abstractmethod
    def get_code_language(self):
        """Get code language."""
        pass

    @abstractmethod
    def get_driver_name(self):
        """Get database driver name."""
        pass
