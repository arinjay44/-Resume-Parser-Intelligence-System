from src.embeddings.embed_resume import embed_resume
from src.embeddings.embed_job import embed_job
from src.scoring.similarity import cosine_similarity  # <-- use your dot-product cosine

from src.rag.chunker import chunk_text


def retrieve_top_chunks(resume_text: str, job_text: str, top_k: int = 3):
    """
    Chunk resume -> embed chunks -> compare to JD embedding -> return top chunks.
    Uses cosine_similarity from Day-4 (dot product) which works with 1D embeddings.
    """
    chunks = chunk_text(resume_text)
    if not chunks:
        return []

    jd_emb = embed_job(job_text)  # 1D vector

    scored = []
    for idx, ch in enumerate(chunks):
        ch_emb = embed_resume(ch)  # 1D vector
        score = cosine_similarity(ch_emb, jd_emb)  # returns 0–100
        scored.append((score, idx, ch))

    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:top_k]
