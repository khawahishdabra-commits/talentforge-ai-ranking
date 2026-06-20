## Overview
This project was developed for Redrob Intelligent Candidate Discovery & Ranking Challenge.

The solution ranks candidate profiles based on:

- AI/ML skill relevance
- Professional experience
- Profile headline alignment
- Recruiter engagement signals
- GitHub activty
- Interview and offer metrics

The script processes candidate profiles and generates a ranked CSV containing the top candidates.

---

## Repository Structure

```
.
├── generate_submission.py
├── sample_candidates.jsonl
├── top100.csv
├── candidate_schema.json
├── requirements.txt
├── submission_metadata.yaml
├── README.md
└── .gitignore
```

---
## Requirements

- Python 3.13.5
- Standard Python libraries

Install dependencies:

```bash
pip intsall -r requirements.txt
```

---

## Running the Project

Generate the ranked cnadidate list:

```bash
python generate_submission.py
```

The script needs:

```text
sample_candidates.jsonl
```

and generates:

```text
top100.csv
```

---

## Ranking Methodology

The ranking score is calculated using:

### 1. Skill Matching
Candidates receive points for matching important AI/ML skills such as:

- Retrieval
- Ranking
- Qdrant
- Pinecone
- Weaviate
- Fine-tuning LLMs
- OpenSearch
- Embeddings
- Python
- NLP
- Elasticsearch
- FAISS

Additional bonuses are awarded based on:

- Skill proficiency
- Endorsements
- Duartion of experience with the skill

### 2. Experience Score

Years of professional experience contribute to the final ranking score.

### 3. Headline Alignment

AI-focused professional headlines receive postive scoring.

Non-relevant titles may receive penalties.

### 4. Recruiter Signals

Additional signals include:

- Open to work status
- GitHub activity
- Recruiter response rate
- Interview completion rate
- Offer acceptance rate
- Recruiter saves
- Profile completeness
- Notice period

---

## Output Format

The genarated CSV contains:

```csv
candidate_id,rank,score,reasoning
```

Example:

```csv
candidate_id,rank,score,reasoning
CAND_0000001,1,314.83,"Matched 3 AI/ML JD skills, strong recruiter engagement and endorsements.
```

---

## Sandbox

Google Colab Sandbox:

https://colab.research.google.com/drive/1fGwsfb4uEbvaL_b-h39eiEAUQBXqyrna?usp=sharing

---
## Notes

The official competition dataset(`candidates.jsonl`) is not included in the repository because of its large size.

A smaller sample dataset(`sample_candidates.jsonl`) is provided for demonstration and reproductibilty purposes.

The same ranking pipeline can be executed on the full dataset during evaluation.

---

## Repository 

GitHub Repository:

https://github.com/khawahishdabra-commits/talentforge-ai-ranking