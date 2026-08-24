from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import PyPDF2
import docx

# Load environment variables (HF_TOKEN) from .env file
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Free Hugging Face model (instruction-tuned, good for text analysis tasks)
# You can swap this with any other free chat/instruct model on Hugging Face
HF_MODEL = "deepseek-ai/DeepSeek-V4-Flash-0731"

client = InferenceClient(
    model=HF_MODEL,
    provider="novita",
    token=os.getenv("HF_TOKEN")
)


def extract_text(filepath):
    """Extract raw text from a PDF or DOCX resume file."""
    if filepath.lower().endswith('.pdf'):
        text = ""
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    elif filepath.lower().endswith('.docx'):
        doc = docx.Document(filepath)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return None


def analyze_resume(resume_text):
    """Send resume text to the free Hugging Face model and get feedback."""

    # Truncate very long resumes so we stay within the model's context limit
    max_chars = 6000
    if len(resume_text) > max_chars:
        resume_text = resume_text[:max_chars]

    prompt = f"""You are an expert resume reviewer and career coach.
Analyze the following resume and provide clear, actionable feedback.

Structure your response into these sections:
1. Skills Identified - list the key skills found in the resume.
2. Structure & Formatting Issues - comment on organization, clarity, length, formatting.
3. Improvement Suggestions - specific, actionable suggestions to make the resume stronger.
4. Overall Score (out of 10) - with a one-line justification.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.4,
    )

    message = response.choices[0].message
    content = message.content

    # Some reasoning models put the actual answer in reasoning_content
    # if the final "content" field comes back empty
    if not content or not content.strip():
        content = getattr(message, "reasoning_content", None)

    if not content or not content.strip():
        raise ValueError("The AI model returned an empty response. Please try again.")

    return content


@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = None
    error = None

    if request.method == 'POST':
        file = request.files.get('resume')

        if not file or file.filename == '':
            error = "Please select a resume file (PDF or DOCX) to upload."
        elif not (file.filename.lower().endswith('.pdf') or file.filename.lower().endswith('.docx')):
            error = "Only PDF and DOCX files are supported."
        else:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            resume_text = extract_text(filepath)

            if not resume_text or not resume_text.strip():
                error = "Could not extract any text from this file. Please try another file."
            else:
                try:
                    feedback = analyze_resume(resume_text)
                except Exception as e:
                    error = f"Something went wrong while analyzing the resume: {e}"

    return render_template('index.html', feedback=feedback, error=error)


if __name__ == '__main__':
    app.run(debug=True)