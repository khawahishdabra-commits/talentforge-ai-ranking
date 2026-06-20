# Candidate Intelligence Machine

## Overview

Candidate Intelligence Machine is an AI-powered candidate ranking engine developed for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

The objective is to move beyond simple keyword matching and build a system that intelligently identifies and ranks the most relevant candidates for a specialized AI/ML role.

The solution combines candidate skills, experience, profile quality, and recruiter engagement signals to produce a ranked shortlist of top candidates.

---

## Problem Statement

Traditional recruitment systems rely heavily on keyword filtering, often missing highly relevant candidates or ranking unsuitable profiles too highly.

This project addresses that problem by creating a multi-factor ranking engine that evaluates:

- Technical skill relevance
- Skill proficiency
- Skill endorsements
- Skill experience duration
- Professional experience
- Headline relevance
- Recruiter engagement
- Candidate activity signals

The goal is to generate a high-quality ranked shortlist rather than a simple filtered list.

---

## Methodology

### 1. Skill Matching

The job description was analyzed to identify key AI/ML skills such as:

- Retrieval
- Ranking
- Embeddings
- NLP
- Python
- FAISS
- Elasticsearch
- Qdrant
- Pinecone
- Weaviate
- Milvus
- OpenSearch
- Fine-tuning LLMs

Each skill is assigned a weight based on importance.

---

### 2. Skill Quality Evaluation

For every matching skill, the system evaluates:

- Base skill importance
- Endorsements received
- Duration of skill usage
- Proficiency level

Skill score is computed using:

```
Skill Score =
Base Weight
+ Endorsement Bonus
+ Duration Bonus
+ Proficiency Bonus
```

---

### 3. Experience Scoring

Candidates receive additional score based on their total professional experience.

```
Experience Score =
Years of Experience × Factor
```

with a capped maximum contribution.

---

### 4. Headline Relevance Analysis

Professional headlines are analyzed for AI-related keywords.

Positive indicators include:

- AI
- ML
- Machine Learning
- NLP
- Retrieval
- Ranking
- LLM
- Applied Scientist

Negative indicators include:

- QA
- Support
- Frontend
- Full Stack
- DevOps

This helps prioritize candidates whose professional identity aligns with the target role.

---

### 5. Recruiter & Behavioral Signals

The ranking engine incorporates Redrob platform signals including:

- Open To Work status
- GitHub activity score
- Recruiter response rate
- Interview completion rate
- Offer acceptance rate
- Saved by recruiters
- Profile completeness score
- Notice period

These signals help identify candidates who are active, responsive, and recruiter-friendly.

---

## Final Ranking Formula

```
Final Score =
(Weighted Skill Score × 3)
+ Experience Score
+ Headline Relevance Score
+ Recruiter Signal Score
```

Candidates are ranked in descending order of final score.

---

## Dataset Features Used

### Profile Information

- Headline
- Years of Experience

### Skills

- Skill Name
- Proficiency
- Endorsements
- Duration of Usage

### Redrob Signals

- Open To Work Flag
- GitHub Activity Score
- Recruiter Response Rate
- Interview Completion Rate
- Offer Acceptance Rate
- Saved By Recruiters
- Profile Completeness Score
- Notice Period

---

## Repository Structure

```
.
├── generate_submission.py
├── candidate_schema.json
├── top100.csv
├── submission_metadata.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

Python 3.10+

No external dependencies are required.

---

## Reproducing Results

Place the provided dataset file:

```
candidates.jsonl
```

in the project root directory.

Run:

```bash
python generate_submission.py
```

Output:

```
top100.csv
```

---

## Dataset Note

The file `candidates.jsonl` is not included in this repository because it exceeds GitHub's file size limit.

The dataset was provided separately as part of the hackathon challenge.

---

## Output Format

The generated submission file follows the required format:

```csv
candidate_id,rank,score,reasoning
```

Example:

```csv
CAND_0039754,1,1120.82,"Matched 7 AI/ML JD skills, 16.2 years experience, strong AI-focused profile, high endorsements and recruiter engagement."
```

---

## Technologies Used

- Python
- JSON
- CSV

---

## Key Highlights

- Multi-factor candidate ranking
- Weighted skill relevance scoring
- Proficiency-based skill evaluation
- Endorsement and experience validation
- Recruiter engagement analysis
- Behavioral signal integration
- Human-readable ranking explanations
- Fast execution on large candidate datasets

---

## Result

The system produces an intelligent ranked shortlist of candidates by combining:

- Technical relevance
- Experience
- Skill credibility
- Recruiter engagement
- Hiring readiness

This approach provides a more robust candidate ranking mechanism than traditional keyword-based filtering systems.