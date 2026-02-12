def chunk_text(text: str, chunk_size: int = 600, overlap: int = 120):
    """
    Simple character-based chunker.
    Works fine for prototype. Later can upgrade to token-based chunking.
    """
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0:
            start = 0
        if end == len(text):
            break
    return chunks
