from .base_model import BaseAIModel


class LocalModel(BaseAIModel):
    def __init__(self, model_id, torch_dtype, max_new_tokens=2048):
        self.client = None
        self.model_id = model_id
        self.torch_dtype = torch_dtype
        self.max_new_tokens = max_new_tokens

    def load(self):
        try:
            from transformers import pipeline
        except ImportError:
            raise ImportError(
                "The 'transformers' and 'torch' libraries are not installed. Please install them using 'pip install transformers torch' before running this feature."
            )

        self.client = pipeline(
            "text-generation",
            model=self.model_id,
            torch_dtype=self.torch_dtype,
            device_map="auto",
        )

    def run(self, messages):
        if self.client is None:
            self.load()

        outputs = self.client(
            messages,
            max_new_tokens=self.max_new_tokens,
            return_full_text=False,
        )

        if isinstance(outputs, list) and "generated_text" in outputs[0]:
            return str(outputs[0]["generated_text"])
        else:
            raise ValueError("Unexpected output format from the model pipeline.")

    def name(self):
        return f"Local ({self.model_id})"
