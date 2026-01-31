import numpy as np

def cosine_similarity(resume_embedding, job_embedding):
    """
    Returns similarity score between resume and job (0–100)
    """
    score = float(np.dot(resume_embedding, job_embedding))
    return round(score * 100, 2)
