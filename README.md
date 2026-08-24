# AI Resume Evaluator (Free — Hugging Face Version)

AI system jo resume (PDF/DOCX) analyze karta hai aur skills, structure, aur improvement areas par feedback deta hai. Ye version **free** hai — OpenAI ki jagah Hugging Face ka free-tier model use karta hai.

## Features
- Resume upload (PDF ya DOCX)
- LLM (Hugging Face Mistral-7B-Instruct) se content analysis — **free**
- Improvement suggestions
- Simple web interface (Flask)

## Hugging Face Token Kaise Banayein (Free)

1. https://huggingface.co par account banayein (agar nahi hai to)
2. Settings → Access Tokens → "New Token" par click karein
3. Type "Read" select karein aur token generate karein
4. Token copy karein — ye `.env` file mein use hoga

Free tier mein limited requests milti hain (rate limits), lekin testing aur is task ke liye kaafi hain.

## Setup

1. Virtual environment banayein aur activate karein:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

2. Dependencies install karein:
   ```
   pip install -r requirements.txt
   ```

3. `.env.example` ko `.env` mein rename karein aur apna Hugging Face token daalein:
   ```
   HF_TOKEN=hf_xxxxxxxxxxxx
   ```

4. App run karein:
   ```
   python app.py
   ```

5. Browser mein open karein:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure
```
resume-evaluator-hf/
├── app.py                 # Main Flask app (Hugging Face backend logic)
├── requirements.txt        # Python dependencies
├── .env.example             # HF token template
├── templates/
│   └── index.html         # Upload form + feedback display
└── uploads/                # Uploaded resumes get stored here
```

## Notes
- Model: `mistralai/Mistral-7B-Instruct-v0.3` (free via Hugging Face Inference API). Aap `app.py` mein `HF_MODEL` variable change karke koi bhi doosra free instruct model use kar sakte hain.
- Agar model "loading" error de to thodi der (20-30 sec) baad dobara try karein — free inference API kabhi kabhi cold-start leta hai.
- `.env` file kabhi bhi GitHub par push na karein (token leak ho sakta hai).
- Agar aage chal kar zyada reliable/fast chahiye to OpenAI wala version (paid) use kar sakte hain — wo bhi maine pehle diya tha.
