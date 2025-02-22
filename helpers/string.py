import textwrap


def clean_multiline(text):
    return textwrap.dedent(text).strip()
