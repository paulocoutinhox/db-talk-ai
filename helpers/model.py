from models.anthropic_model import AnthropicModel
from models.deep_seek_model import DeepSeekModel
from models.gemini_model import GeminiModel
from models.grok_model import GrokModel
from models.local_gguf_model import LocalGGUFModel
from models.local_model import LocalModel
from models.openai_model import OpenAIModel


def load_models():
    # Add fixed models
    models = []
    models.append(OpenAIModel())
    models.append(DeepSeekModel())
    models.append(GrokModel())
    models.append(GeminiModel())
    models.append(AnthropicModel())

    # Add local models
    local_model = LocalModel()

    if local_model.get_variants():
        models.append(local_model)

    # Add local gguf models
    gguf_models = LocalGGUFModel()

    if gguf_models.get_variants():
        models.append(gguf_models)

    return models
