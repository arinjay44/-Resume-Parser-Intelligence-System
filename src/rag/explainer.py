from src.rag.retriever import retrieve_top_chunks
from src.llm.local_llm_stub import generate_explanation

def explain_match(resume_id: str, resume_text: str, job_text: str, top_k: int = 3):
    chunks = retrieve_top_chunks(resume_text, job_text, top_k=top_k)
    return generate_explanation(job_text, resume_id, chunks)
