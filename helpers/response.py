import re


def clean(text: str) -> str:
    """
    Removes markdown-style code formatting, keeping the sql content.
    """
    # remove code block delimiters (```sql ... ``` or ``` ... ```)
    text = re.sub(r"```(?:\w+)?\n([\s\S]*?)\n```", r"\1", text, flags=re.MULTILINE)

    # remove inline code formatting (`...`)
    text = re.sub(r"`([^`]+)`", r"\1", text)

    return text.strip()
