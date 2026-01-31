from sentence_transformers import SentenceTransformer

# Load once (efficient)
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_resume(text: str):
    """
    Convert resume text to normalized embedding
    """
    if not text or not text.strip():
        raise ValueError("Resume text is empty")

    embedding = _model.encode(
        text,
        normalize_embeddings=True
    )
    return embedding
