from src.embeddings.embed_resume import embed_resume
from src.embeddings.embed_job import embed_job
from src.scoring.similarity import cosine_similarity


def main():
    # Temporary demo text
    resume_text = """
    Associate Data Scientist with experience in Python, Machine Learning,
    NLP, Flask, SQL, and AWS. Worked on resume parsing and NLP pipelines.
    """

    job_description = """
    We are hiring a Data Scientist skilled in Python, NLP, Machine Learning,
    and cloud technologies like AWS.
    """

    resume_embedding = embed_resume(resume_text)
    job_embedding = embed_job(job_description)

    match_score = cosine_similarity(resume_embedding, job_embedding)

    print("\n===== DAY 4 OUTPUT =====")
    print("Resume–JD Match Score:", match_score, "%")


if __name__ == "__main__":
    main()
