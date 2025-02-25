import os

from .base_model import BaseAIModel


class OpenAIModel(BaseAIModel):
    def __init__(self):
        super().__init__()
        self.client = None
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.default_variant = "gpt-4o-mini"

    def load(self):
        if not self.api_key:
            raise ValueError("The environment variable OPENAI_API_KEY is missing.")

        try:
            import openai
        except ImportError:
            raise ImportError(
                "The 'openai' library is not installed. Please install it using 'pip install openai'."
            )

        self.client = openai.OpenAI(api_key=self.api_key)

    def run(self, messages, variant=None):
        if self.client is None:
            self.load()

        model_variant = variant or self.default_variant

        # Prepare messages according to the model's role support
        prepared_input = self.prepare_messages(messages, model_variant)

        if isinstance(prepared_input, str):
            # Handle plain-text input for models without role support
            response = self.client.completions.create(
                model=model_variant,
                prompt=prepared_input,
                temperature=0.2,
            )

            return response.choices[0].text.strip()
        elif isinstance(prepared_input, list):
            # Standard Chat Completions API with role-based messages
            response = self.client.chat.completions.create(
                model=model_variant,
                messages=prepared_input,
                temperature=0.2,
            )

            return response.choices[0].message.content.strip()

        else:
            raise ValueError(
                f"Invalid input format for model variant '{model_variant}'."
            )

    def name(self):
        return "OpenAI"

    def get_variants(self):
        return {
            "gpt-4o": "GPT-4o (128k context)",
            "chatgpt-4o-latest": "ChatGPT-4o (128k context)",
            "gpt-4o-mini": "GPT-4o Mini (128k context)",
            "gpt-4-turbo": "GPT-4 Turbo (128k context)",
            "gpt-4": "GPT-4 (8k context)",
        }
