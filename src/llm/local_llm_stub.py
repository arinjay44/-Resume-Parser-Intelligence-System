def generate_explanation(job_text: str, resume_id: str, chunks):
    """
    Simple deterministic explanation based on retrieved evidence.
    This is a safe prototype. Later swap with OpenAI call.
    """
    bullets = []
    for score, idx, ch in chunks:
        snippet = ch.replace("\n", " ").strip()
        snippet = snippet[:220] + ("..." if len(snippet) > 220 else "")
        bullets.append(f"- Evidence {idx+1} (score {score}%): \"{snippet}\"")

    explanation = (
        f"Candidate {resume_id} matches the job because their resume contains "
        f"multiple sections semantically similar to the job description.\n\n"
        f"Top supporting evidence:\n" + "\n".join(bullets)
    )
    return explanation
