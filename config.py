import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DISCOURSE_API_URL = os.getenv("DISCOURSE_API_URL")
    DISCOURSE_API_KEY = os.getenv("DISCOURSE_API_KEY")
    DISCOURSE_USERNAME = os.getenv("DISCOURSE_USERNAME")
    COURSE_WEBSITE_URL = os.getenv("COURSE_WEBSITE_URL")