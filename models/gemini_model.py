import os

from .base_model import BaseAIModel


class GeminiModel(BaseAIModel):
    def __init__(self):
        super().__init__()
        self.client = None
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.default_variant = "gemini-2.0-pro"

    def load(self):
        if not self.api_key:
            raise ValueError("The environment variable GEMINI_API_KEY is missing.")

        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(
                "The 'openai' library is not installed. Please install it using 'pip install openai'."
            )

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

    def run(self, messages, variant=None):
        if self.client is None:
            self.load()

        model_variant = variant or self.default_variant
        prepared_input = self.prepare_messages(messages, model_variant)

        response = self.client.chat.completions.create(
            model=model_variant,
            messages=prepared_input,
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()

    def name(self):
        return "Gemini"

    def get_variants(self):
        return {
            "gemini-2.0-flash": "Gemini 2 Flash (1m context)",
        }
