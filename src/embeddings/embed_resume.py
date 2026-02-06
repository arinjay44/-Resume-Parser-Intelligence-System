from sentence_transformers import SentenceTransformer

# Load model once
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_resume(text: str):
    """
    Convert resume text to embedding (normalized)
    """
    if not text or not text.strip():
        raise ValueError("Resume text is empty")

    return _model.encode(text, normalize_embeddings=True)
