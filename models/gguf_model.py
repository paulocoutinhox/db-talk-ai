import os

from .base_model import BaseAIModel


class GGUFModel(BaseAIModel):
    def __init__(self, model_path):
        self.model_path = model_path
        self.llm = None

    def load(self):
        try:
            from gpt4all import GPT4All
        except ImportError:
            raise ImportError(
                "The 'gpt4all' library is not installed. Please install it using 'pip install gpt4all' before running this feature."
            )

        self.llm = GPT4All(model_name=self.model_path)

    def run(self, messages):
        if self.llm is None:
            self.load()

        # Build the prompt using manual system/user simulation
        prompt_parts = []

        for message in messages:
            role = message.get("role")
            content = message.get("content")

            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"User: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")

        # Combine the messages into a full prompt
        full_prompt = "\n".join(prompt_parts)

        # Generate the response
        response = self.llm.generate(full_prompt)

        return response.strip()

    def name(self):
        return os.path.basename(self.model_path)
