from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_job(job_text: str):
    return _model.encode(job_text)
