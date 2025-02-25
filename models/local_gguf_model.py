import os

from helpers import file

from .base_model import BaseAIModel


class LocalGGUFModel(BaseAIModel):
    available_models = {}

    def __init__(self):
        super().__init__()
        self.llm = None
        self.force_string_prompt = True

    def load(self, model_config):
        """
        Load a GGUF model using the specified configuration.

        Args:
            model_config (dict): Model configuration including the path.
        """
        try:
            from gpt4all import GPT4All
        except ImportError:
            raise ImportError(
                "The 'gpt4all' library is not installed. Please install it using 'pip install gpt4all' before running this feature."
            )

        self.llm = GPT4All(model_name=model_config["path"])

    def run(self, messages, variant=None):
        if variant is None:
            raise ValueError("A valid model variant (ID) must be provided.")

        model_config = self.available_models.get(variant)
        if not model_config:
            raise ValueError(f"Model variant '{variant}' not found.")

        if self.llm is None:
            self.load(model_config)

        model_variant = variant or self.default_variant
        prepared_input = self.prepare_messages(messages, model_variant)

        response = self.llm.generate(prepared_input)

        return response.strip()

    def name(self):
        return "Local GGUF"

    def get_variants(self):
        if not self.available_models:
            self.load_models_from_directory()

        return {
            model_path: config["name"]
            for model_path, config in self.available_models.items()
        }

    @classmethod
    def load_models_from_directory(cls):
        """
        Scans the models directory for GGUF files and loads their configurations.

        Returns:
            dict: A dictionary of available GGUF models.
        """
        models_dir = file.get_models_folder()

        if not os.path.exists(models_dir):
            return {}

        cls.available_models = {}

        for f in os.listdir(models_dir):
            if f.endswith(".gguf"):
                model_path = os.path.join(models_dir, f)
                model_name = os.path.splitext(f)[0]

                cls.available_models[model_path] = {
                    "name": model_name,
                    "path": model_path,
                }

        return cls.available_models
