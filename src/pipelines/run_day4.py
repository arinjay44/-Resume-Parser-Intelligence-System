from src.embeddings.embed_resume import embed_resume
from src.embeddings.embed_job import embed_job
from src.scoring.similarity import compute_similarity

def main():
    resume_text = """
    Data Scientist skilled in Python, Machine Learning, NLP, Deep Learning,
    Pandas, NumPy, SQL, TensorFlow, AWS.
    """

    job_description = """
    Looking for a Data Scientist with strong Python, ML, NLP,
    Deep Learning, and cloud experience.
    """

    resume_vec = embed_resume(resume_text)
    job_vec = embed_job(job_description)

    score = compute_similarity(resume_vec, job_vec)

    print("\n===== DAY 4 OUTPUT =====")
    print(f"Resume–JD Match Score: {score} %")

if __name__ == "__main__":
    main()
