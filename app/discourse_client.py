import requests
import os

def post_reply(topic_id, message):
    url = f"{os.getenv('DISCOURSE_API_URL')}/posts.json"
    headers = {
        "Api-Key": os.getenv("DISCOURSE_API_KEY"),
        "Api-Username": os.getenv("DISCOURSE_API_USERNAME")
    }
    data = {
        "topic_id": topic_id,
        "raw": message
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code == 200
