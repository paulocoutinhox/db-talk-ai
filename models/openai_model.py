import os

from .base_model import BaseAIModel


class OpenAIModel(BaseAIModel):
    def __init__(self):
        self.client = None
        self.api_key = os.getenv("OPENAI_API_KEY")

    def load(self):
        if not self.api_key:
            raise ValueError("The environment variable OPENAI_API_KEY is missing.")

        try:
            import openai
        except ImportError:
            raise ImportError(
                "The 'openai' library is not installed. Please install it using 'pip install openai' before running this feature."
            )

        self.client = openai.OpenAI(api_key=self.api_key)

    def run(self, messages):
        if self.client is None:
            self.load()

        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()

    def name(self):
        return "OpenAI GPT-4"
