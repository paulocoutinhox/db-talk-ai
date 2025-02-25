import os

from .base_model import BaseAIModel


class AnthropicModel(BaseAIModel):
    def __init__(self):
        super().__init__()
        self.client = None
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.default_variant = "claude-3-7-sonnet-latest"

    def load(self):
        if not self.api_key:
            raise ValueError("The environment variable ANTHROPIC_API_KEY is missing.")

        try:
            import anthropic
        except ImportError:
            raise ImportError(
                "The 'anthropic' library is not installed. Please install it using 'pip install anthropic'."
            )

        self.client = anthropic.Anthropic(api_key=self.api_key)

    def run(self, messages, variant=None):
        if self.client is None:
            self.load()

        model_variant = variant or self.default_variant
        prepared_input = self.prepare_messages(messages, model_variant)

        # Separate system prompt from user/assistant messages
        system_prompt = ""
        filtered_messages = []

        for message in prepared_input:
            if message.get("role") == "system":
                system_prompt = message.get("content")
            else:
                filtered_messages.append(message)

        # Make the request
        response = self.client.messages.create(
            model=model_variant,
            max_tokens=4096,
            system=system_prompt or None,
            messages=filtered_messages,
        )

        return response.content[0].text.strip()

    def name(self):
        return "Anthropic"

    def get_variants(self):
        return {
            "claude-3-7-sonnet-latest": "Claude 3.7 Sonnet (200k context)",
            "claude-3-5-sonnet-latest": "Claude 3.5 Sonnet (200k context)",
        }
