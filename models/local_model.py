import json
import os

from helpers import file

from .base_model import BaseAIModel


class LocalModel(BaseAIModel):
    available_models = {}

    def __init__(self):
        super().__init__()
        self.client = None

    def load(self, model_config):
        """
        Load the model using its configuration.

        Args:
            model_config (dict): The configuration of the model including path, torch_dtype, and max_new_tokens.
        """
        try:
            from transformers import pipeline
        except ImportError:
            raise ImportError(
                "The 'transformers' and 'torch' libraries are not installed. Please install them using 'pip install transformers torch' before running this feature."
            )

        self.client = pipeline(
            "text-generation",
            model=model_config["path"],
            torch_dtype=model_config.get("torch_dtype", "auto"),
            device_map="auto",
        )

    def run(self, messages, variant=None):
        if variant is None:
            raise ValueError("A valid model variant (ID) must be provided.")

        model_config = self.available_models.get(variant)
        if not model_config:
            raise ValueError(f"Model variant '{variant}' not found.")

        if self.client is None:
            self.load(model_config)

        outputs = self.client(
            messages,
            max_new_tokens=model_config.get("max_new_tokens", 2048),
            return_full_text=False,
        )

        if isinstance(outputs, list) and "generated_text" in outputs[0]:
            return str(outputs[0]["generated_text"])
        else:
            raise ValueError("Unexpected output format from the model pipeline.")

    def name(self):
        return "Local"

    def get_variants(self):
        if not self.available_models:
            self.load_models_from_config()

        return {
            model_id: config["name"]
            for model_id, config in self.available_models.items()
        }

    @classmethod
    def load_models_from_config(self):
        """
        Loads models from a JSON configuration file and stores them in available_models.

        Returns:
            dict: A dictionary of available model configurations.
        """
        models_file = file.get_models_file()

        if not os.path.exists(models_file):
            return {}

        with open(models_file, "r", encoding="utf-8") as f:
            model_configs = json.load(f)

        self.available_models = {}

        for model_config in model_configs:
            model_name = model_config.get("name")
            model_path = model_config.get("path")
            torch_dtype = model_config.get("torch_dtype", "auto")
            max_new_tokens = model_config.get("max_new_tokens", 4096)

            if not model_name or not model_path:
                raise ValueError("Each model entry must have 'name' and 'path' fields.")

            self.available_models[model_path] = {
                "name": model_name,
                "path": model_path,
                "torch_dtype": torch_dtype,
                "max_new_tokens": max_new_tokens,
            }

        return self.available_models
