import json
import csv

## JD Skill Weights
skill_weights = {
    "Retrieval":15,
    "Ranking":15,
    "Qdrant":10,
    "Pinecone":10,
    "Weaviate":10,
    "Milvus":10,
    "Fine-tuning LLMs":8,
    "OpenSearch":8,
    "Embeddings":15,
    "Python":12,
    "NLP":12,
    "Elasticsearch":10,
    "FAISS":10
}

## Good Headlines
ai_keywords = [
    "ai",
    "ml",
    "machine learning",
    "nlp",
    "data scientist",
    "applied scientist",
    "recommendation",
    "retreival",
    "ranking",
    "llm"
]

## Bad Headlines
bad_keywords = [
    "devops",
    "frontend",
    "full-stack",
    "qa",
    "testing",
    "support",
    "backend engineer"
]

## Proficiency Bonus
proficiency_bonus = {
    "expert":10,
    "advanced":6,
    "intermediate":3,
    "begineer":1
}

results = []

## Read Candidate
INPUT_FILE = "sample_candidates.jsonl"
with open(INPUT_FILE,"r",encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        skills = candidate["skills"]

        ## Skill Score
        skill_score = 0
        matching_skill_count = 0

        for s in candidate["skills"]:
            skill_name = s["name"]

            if skill_name in skill_weights:
                matching_skill_count += 1
                base_weight = skill_weights[skill_name]

                endorsements = s.get("endorsements",0)

                duration_months = s.get("duration_months",0)

                proficiecny = s.get("proficiency","").lower()

                endorsements_bonus = min(endorsements*0.5,25)

                duration_bonus = min(duration_months/12,10)
                
                prof_bonus = proficiency_bonus.get(proficiecny,0)

                skill_score += (
                    base_weight + 
                    endorsements_bonus +
                    duration_bonus +
                    prof_bonus
                )

        ## Experience
        years = candidate["profile"]["years_of_experience"]

        experience_score = min(years*3,30)

        ## Headline Score
        headline = candidate["profile"]["headline"].lower()

        title_score = 0

        for kw in ai_keywords:
            if kw in headline:
                title_score += 5

        for kw in bad_keywords:
            if kw in headline:
                title_score -= 75

        ## Recruit Signals
        signals = candidate["redrob_signals"]
        signal_score = 0

        if signals["open_to_work_flag"]:
            signal_score  += 5

        signal_score += signals["github_activity_score"]
        signal_score += signals["recruiter_response_rate"]*10
        signal_score += signals["interview_completion_rate"]*10
        signal_score += signals["offer_acceptance_rate"]*10
        signal_score += signals["saved_by_recruiters_30d"]
        signal_score += signals["profile_completeness_score"]*0.2
        notice = signals["notice_period_days"]

        if notice <= 30:
            signal_score += 5
        elif notice <= 60:
            signal_score += 2

        ## Final Score 
        final_score = (
            skill_score*3
            + experience_score
            + title_score
            + signal_score
        )

        templates = [
            f"Matched {matching_skill_count} AI/ML JD skills, strong recruiter engagement and endorsements.",

            f"Strong AI/ML alignment with {matching_skill_count} matching skills and {years:.1f} years of industry experience.",

            f"Relevant AI-focused profile with {matching_skill_count} key JD skills, strong activity signals and {years:.1f} years experience."
        ]

        reason = templates[len(results) % len(templates)]

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(final_score,2),
            "reason":reason
        })

## Sort
results.sort(
    key=lambda x: x["score"],
    reverse=True
)

## Write Submission
with open("top100.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(
        results[:100],
        start=1
    ):
        
        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reason"]
        ])

print("top100.csv generated successfully!")



