from src.ranking.rank_resumes import rank_resumes

def main():
    resumes = {
        "resume_1": "Python Data Scientist with NLP and ML experience",
        "resume_2": "Frontend developer with React and JavaScript",
        "resume_3": "Machine Learning Engineer with AWS and Deep Learning"
    }

    job_description = """
    Looking for a Data Scientist skilled in Python,
    Machine Learning, NLP, and cloud platforms.
    """

    ranked = rank_resumes(resumes, job_description)

    print("\n===== DAY 5: RESUME RANKING =====")
    for r in ranked:
        print(f"{r['resume_id']} → {r['score']} %")

if __name__ == "__main__":
    main()
