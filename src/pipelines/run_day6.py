from src.ranking.rank_resumes import rank_resumes
from src.rag.explainer import explain_match

def main():
    # Demo resumes (replace with parsed resume texts later)
    resumes = {
        "resume_1": "Python Data Scientist with NLP, ML, AWS experience. Worked on NLP pipelines and ML models.",
        "resume_2": "Frontend developer with React, JavaScript, UI work.",
        "resume_3": "Machine Learning Engineer with Deep Learning, TensorFlow, cloud deployment on AWS."
    }

    job_description = """
    Hiring a Data Scientist with Python, NLP, Machine Learning,
    Deep Learning and cloud experience (AWS).
    """

    ranked = rank_resumes(resumes, job_description)

    print("\n===== DAY 6: RAG EXPLANATIONS =====\n")

    for r in ranked[:3]:
        rid = r["resume_id"]
        score = r["score"]
        print(f"\n--- {rid} | Score: {score}% ---")
        explanation = explain_match(rid, resumes[rid], job_description, top_k=3)
        print(explanation)

if __name__ == "__main__":
    main()
