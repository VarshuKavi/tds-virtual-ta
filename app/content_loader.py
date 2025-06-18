import json

def load_content(path="content/tds_content.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    sections = data.get("sections", [])
    return "\n\n".join(
        f"{s['title']}\n" + "\n".join(s['content']) for s in sections
    )
