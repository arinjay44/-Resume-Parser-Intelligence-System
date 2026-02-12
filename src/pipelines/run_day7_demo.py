from src.ranking.rank_resumes import rank_resumes
from src.rag.explainer import explain_match
from src.evaluation.evaluate import recall_at_k


def main():
    resumes = {
        "r1": "Python Data Scientist with NLP, ML, AWS, Flask.",
        "r2": "Frontend developer with React and JavaScript.",
        "r3": "Machine Learning Engineer with TensorFlow and AWS.",
        "r4": "Data Analyst with SQL, Excel, dashboards.",
        "r5": "Backend Java developer with Spring."
    }

    test_queries = [
        {
            "jd": "Looking for Python Data Scientist with NLP and AWS",
            "relevant": {"r1", "r3"}
        },
        {
            "jd": "Hiring frontend React developer",
            "relevant": {"r2"}
        }
    ]

    print("\n===== DAY 7: FINAL DEMO & EVALUATION =====\n")

    scores = []

    for i, q in enumerate(test_queries, start=1):
        jd = q["jd"]
        relevant = q["relevant"]

        ranked = rank_resumes(resumes, jd)
        ranked_ids = [r["resume_id"] for r in ranked]

        r_at_3 = recall_at_k(ranked_ids, relevant, k=3)
        scores.append(r_at_3)

        print(f"\n--- QUERY {i} ---")
        print("Job:", jd)
        print("\nTop 3 Results:")
        for r in ranked[:3]:
            print(f"  {r['resume_id']} → {r['score']}%")

        print("\nExplanation (Top Candidate):")
        top_id = ranked[0]["resume_id"]
        explanation = explain_match(top_id, resumes[top_id], jd, top_k=2)
        print(explanation)

        print(f"\nRecall@3: {r_at_3}")

    avg_recall = sum(scores) / len(scores)
    print(f"\n✅ Average Recall@3 across queries: {round(avg_recall, 2)}")


if __name__ == "__main__":
    main()
