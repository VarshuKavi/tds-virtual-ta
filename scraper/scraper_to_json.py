import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv
load_dotenv()

COURSE_URL = os.getenv("COURSE_WEBSITE_URL")

def clean_text(text):
    return ' '.join(text.strip().split())

def scrape_course_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {
        "url": url,
        "title": soup.title.string if soup.title else "Course Page",
        "sections": []
    }

    headings = soup.find_all(['h1', 'h2', 'h3'])
    for heading in headings:
        section_title = clean_text(heading.get_text())
        content = []
        sibling = heading.find_next_sibling()
        while sibling and sibling.name not in ['h1', 'h2', 'h3']:
            if sibling.name in ['p', 'ul', 'ol']:
                content.append(clean_text(sibling.get_text()))
            sibling = sibling.find_next_sibling()

        if content:
            data["sections"].append({"title": section_title, "content": content})

    return data

def save_to_json(data, filename="content/tds_content.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    data = scrape_course_website(COURSE_URL)
    save_to_json(data)
    print("Scraped content saved to content/tds_content.json")
