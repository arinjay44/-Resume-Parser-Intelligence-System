from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_vec, job_vec):
    score = cosine_similarity([resume_vec], [job_vec])[0][0]
    return round(score * 100, 2)
