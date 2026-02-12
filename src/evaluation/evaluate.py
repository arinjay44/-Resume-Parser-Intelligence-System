def recall_at_k(ranked_ids, relevant_ids, k=3):
    """
    ranked_ids: list of resume_ids in ranked order
    relevant_ids: set of correct ids
    """
    top_k = ranked_ids[:k]
    return 1.0 if any(r in top_k for r in relevant_ids) else 0.0
