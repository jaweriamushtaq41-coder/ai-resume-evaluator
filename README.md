<div align="center">

# 🚀 AI Resume Evaluator
### *Free & Powered by Hugging Face* 🤗

**Apna resume upload karo, AI se instant feedback pao — bilkul FREE! 💯**

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Mistral--7B-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Free](https://img.shields.io/badge/Cost-100%25%20FREE-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## ✨ Ye Kya Hai?

Ek **AI-powered resume checker** jo tumhara PDF/DOCX resume padhta hai aur batata hai:

| 🔍 Kya Check Hota Hai | 💡 Kya Milta Hai |
|---|---|
| Skills & Keywords | Missing skills ka suggestion |
| Resume Structure | Formatting improvement tips |
| Content Quality | Weak points highlight |
| Overall Impression | Actionable feedback |

> 💸 **Best Part?** Isme OpenAI ka paid API nahi lagta — **Hugging Face ka FREE Inference API** use hota hai, so zero cost pe chalao! 🎉

---

## 🎯 Features

- 📄 **Resume Upload** — PDF ya DOCX, dono support
- 🧠 **LLM Analysis** — `Mistral-7B-Instruct-v0.3` free model se deep content analysis
- 📈 **Improvement Suggestions** — Practical aur specific feedback
- 🌐 **Simple Web UI** — Flask-based, no complex setup
- 🆓 **100% Free** — Sirf ek free HF token chahiye

---

## 🔑 Hugging Face Token Kaise Banayein (2 min ka kaam)

```
1️⃣  https://huggingface.co par account banao
2️⃣  Settings → Access Tokens → "New Token"
3️⃣  Type = "Read" select karo → Generate
4️⃣  Token copy karo → .env file mein daalo
```

> ⚡ Free tier mein rate limits hain, lekin testing/personal use ke liye **more than enough** hai.

---

## ⚙️ Quick Setup

### 1️⃣ Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # 🪟 Windows
source venv/bin/activate   # 🍎🐧 Mac/Linux
```

### 2️⃣ Dependencies Install Karo

```bash
pip install -r requirements.txt
```

### 3️⃣ Token Setup Karo

`.env.example` ko `.env` mein rename karo aur apna token daalo:

```env
HF_TOKEN=hf_xxxxxxxxxxxx
```

### 4️⃣ App Run Karo

```bash
python app.py
```

### 5️⃣ Browser Mein Kholo 🎉

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
resume-evaluator-hf/
├── 🐍 app.py              # Main Flask app + HF backend logic
├── 📦 requirements.txt    # Python dependencies
├── 🔐 .env.example        # HF token template
├── 📂 templates/
│   └── 🖥️ index.html      # Upload form + feedback UI
└── 📂 uploads/            # Uploaded resumes yahan store hote hain
```

---

## 💡 Pro Tips

- 🔄 **Model change karna hai?** `app.py` mein `HF_MODEL` variable edit karo — koi bhi free instruct model use kar sakte ho
- ⏳ **"Model loading" error aaya?** Chill karo, 20-30 sec wait karke retry karo — free API ka cold-start hota hai
- 🚫 **`.env` kabhi GitHub par push mat karo** — token leak ho sakta hai!
- 💎 **Zyada speed/reliability chahiye?** Paid OpenAI version bhi available hai — link neeche 👇

---

## 🔗 Related

> 🌟 **OpenAI (Paid) Version** bhi available hai agar zyada fast & reliable chahiye — pehle wala already diya hua hai.

---

<div align="center">

### ⭐ Agar pasand aaya to star zaroor dena!

Made with 🧠 + ☕ + 🤗 Hugging Face

</div>
