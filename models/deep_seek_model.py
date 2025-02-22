import os

from .base_model import BaseAIModel


class DeepSeekModel(BaseAIModel):
    def __init__(self):
        self.client = None
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

    def load(self):
        if not self.api_key:
            raise ValueError("The environment variable DEEPSEEK_API_KEY is missing.")

        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(
                "The 'openai' library is not installed. Please install it using 'pip install openai' before running this feature."
            )

        self.client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")

    def run(self, messages):
        if self.client is None:
            self.load()

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()

    def name(self):
        return "DeepSeek"
