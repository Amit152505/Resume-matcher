# Resume Matcher CLI (Python + spaCy)

A simple CLI utility to parse resumes, extract keywords, and score candidates against job descriptions.
The tool highlights missing keywords and suggests targeted improvements.

## Install

`git clone https://github.com/YOUR_USERNAME/resume-matcher-cli.git
cd resume-matcher-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm`


# EXAMPLE 

Prepare two .txt files:

-> resume.txt

-> job.txt

Run:
`python matcher.py resume.txt job.txt`

Example Output
Resume Score: 67.5%

✅ Matched keywords: python, data, analysis
❌ Missing keywords: cloud, machine, learning
