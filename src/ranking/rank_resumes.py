from src.embeddings.embed_resume import embed_resume
from src.embeddings.embed_job import embed_job
from src.scoring.similarity import compute_similarity

def rank_resumes(resume_texts: dict, job_description: str):
    """
    resume_texts = {
        "resume_1": "...",
        "resume_2": "..."
    }
    """

    job_embedding = embed_job(job_description)

    results = []

    for resume_id, resume_text in resume_texts.items():
        resume_embedding = embed_resume(resume_text)
        score = compute_similarity(resume_embedding, job_embedding)

        results.append({
            "resume_id": resume_id,
            "score": score
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)
