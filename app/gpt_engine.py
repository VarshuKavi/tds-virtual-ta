import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USE_OPENAI = os.getenv("USE_OPENAI", "true").lower() == "true"

# Set API key if OpenAI is enabled
if USE_OPENAI and OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# Load course content from JSON file
try:
    with open("content/tds_content.json", "r", encoding="utf-8") as f:
        tds_content = json.load(f)
except Exception as e:
    print("Error loading course content:", e)
    tds_content = []

def generate_response(question):
    if not tds_content:
        return "Sorry, course content is unavailable."

    if not USE_OPENAI or not OPENAI_API_KEY:
        return f"(MOCK) Received your question: '{question}'. Course has {len(tds_content)} entries."

    try:
        # Combine course content into one string
        content_str = "\n".join(
            [f"Week {item['week']}: {item['topic']}\n{item['content']}" for item in tds_content]
        )

        messages = [
            {"role": "system", "content": "You are a helpful TA for a Data Science course."},
            {"role": "user", "content": f"Course Content:\n{content_str}\n\nQuestion: {question}"}
        ]

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message["content"]

    except Exception as e:
        return f"(MOCK fallback) OpenAI error: {e}"
