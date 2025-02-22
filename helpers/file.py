import os


def get_root_folder():
    """Get the root folder path."""

    return os.getenv(
        "DB_TALK_AI_ROOT",
        os.path.dirname(
            os.path.abspath(os.path.join(__file__, "..")),
        ),
    )


def get_data_folder():
    """Get the data folder path."""
    return os.path.join(get_root_folder(), "data")


def get_schemas_folder():
    """Get the schemas folder path."""
    return os.path.join(get_data_folder(), "schemas")


def get_models_folder():
    """Get the models folder path."""
    return os.path.join(get_data_folder(), "models")


def get_config_folder():
    """Get the config folder path."""
    return os.path.join(get_data_folder(), "config")


def get_schema_file(name):
    """Get the schema file path for a given name."""
    return os.path.join(get_schemas_folder(), name)


def get_databases_file():
    """Get the databases file path."""
    return os.path.join(get_config_folder(), "databases.json")
