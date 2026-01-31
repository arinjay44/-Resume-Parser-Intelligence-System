from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_job(text: str):
    """
    Convert job description text to normalized embedding
    """
    if not text or not text.strip():
        raise ValueError("Job description is empty")

    embedding = _model.encode(
        text,
        normalize_embeddings=True
    )
    return embedding
