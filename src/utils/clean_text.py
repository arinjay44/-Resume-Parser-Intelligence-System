import re

def clean_text(text: str) -> str:
    """
    Normalize resume text for parsing.
    """
    text = text.lower()

    # remove non-ascii characters
    text = text.encode("ascii", errors="ignore").decode()

    # replace multiple spaces/newlines with single
    text = re.sub(r"\s+", " ", text)

    return text.strip()
