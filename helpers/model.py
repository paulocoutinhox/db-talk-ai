import os

import torch

from helpers import file
from models.deep_seek_model import DeepSeekModel
from models.gemini_model import GeminiModel
from models.gguf_model import GGUFModel
from models.grok_model import GrokModel
from models.local_model import LocalModel
from models.openai_model import OpenAIModel


def load_models():
    # Add fixed models
    models = []
    models.append(OpenAIModel())
    models.append(DeepSeekModel())
    models.append(GrokModel())
    models.append(GeminiModel())

    # Add fixed local models
    models.append(
        LocalModel(
            "Qwen/Qwen2.5-3B-Instruct",
            torch_dtype=torch.bfloat16,
        )
    )

    # Add local gguf models dynamically
    models_dir = file.get_models_folder()

    if os.path.exists(models_dir):
        for f in os.listdir(models_dir):
            if f.endswith(".gguf"):
                models.append(GGUFModel(f"{models_dir}/{f}"))

    return models
