from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def health_check():
    return {"status": "AI Sales Automator Backend Running"}

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@app.post("/upload")
async def upload(file: UploadFile = File(...), email: str = Form(...)):

    # Read CSV
    df = pd.read_csv(file.file)

    data = df.to_string()

    prompt = f"""
You are a professional sales analyst.

Analyze this dataset and generate a short professional summary.

Dataset:
{data}

Explain:
- Top performing category
- Region performance
- Revenue highlights
- Any unusual trends
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-001:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    result = response.json()

    # SAFE extraction
    if "candidates" in result:
        summary = result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        summary = "AI summary could not be generated. API response: " + str(result)

    send_email(email, summary)

    return {"summary": summary}


def send_email(to_email, summary):

    msg = EmailMessage()

    msg["Subject"] = "AI Generated Sales Summary"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email

    msg.set_content(summary)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)