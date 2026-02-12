import numpy as np

def cosine_similarity(a, b):
    """
    Cosine similarity for embeddings.
    Accepts 1D arrays (shape: [d]) or 2D arrays (shape: [1, d]).
    Returns score in percent (0–100).
    """
    a = np.asarray(a)
    b = np.asarray(b)

    # flatten (1, d) -> (d,)
    if a.ndim == 2:
        a = a.reshape(-1)
    if b.ndim == 2:
        b = b.reshape(-1)

    if a.ndim != 1 or b.ndim != 1:
        raise ValueError(f"Expected 1D vectors. Got {a.shape} and {b.shape}")

    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0

    score = float(np.dot(a, b) / denom)
    return round(score * 100, 2)


# Backward compatible alias (so Day-5 code doesn't break)
def compute_similarity(resume_vec, job_vec):
    return cosine_similarity(resume_vec, job_vec)
