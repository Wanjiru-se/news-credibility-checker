import os
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


def extract_claims(article_text):
    prompt = f"""
Extract only factual, verifiable claims from this article.

Return JSON only in this format:

{{
  "claims": [
    {{
      "claim_text": "..."
    }}
  ]
}}

Article:
{article_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]

        return json.loads(text.strip())

    except Exception as e:
        return {
            "claims": [],
            "error": str(e)
        }