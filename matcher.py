#!/usr/bin/env python3
import spacy
import argparse

def extract_keywords(text, nlp):
    doc = nlp(text.lower())
    # simple keyword extraction: nouns & proper nouns
    keywords = [token.lemma_ for token in doc if token.pos_ in ("NOUN", "PROPN")]
    return set(keywords)

def score_resume(resume_text, job_text, nlp):
    resume_keywords = extract_keywords(resume_text, nlp)
    job_keywords = extract_keywords(job_text, nlp)

    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords

    score = len(matched) / len(job_keywords) * 100 if job_keywords else 0

    return {
        "score": round(score, 2),
        "matched": matched,
        "missing": missing
    }

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to parse resumes, extract keywords, and score against a job description."
    )
    parser.add_argument("resume", help="Path to resume text file")
    parser.add_argument("job", help="Path to job description text file")

    args = parser.parse_args()

    nlp = spacy.load("en_core_web_sm")

    with open(args.resume, "r", encoding="utf-8") as f:
        resume_text = f.read()

    with open(args.job, "r", encoding="utf-8") as f:
        job_text = f.read()

    results = score_resume(resume_text, job_text, nlp)

    print(f"\nResume Score: {results['score']}%")
    print(f"\n✅ Matched keywords: {', '.join(results['matched']) if results['matched'] else 'None'}")
    print(f"\n❌ Missing keywords: {', '.join(results['missing']) if results['missing'] else 'None'}")

if __name__ == "__main__":
    main()
