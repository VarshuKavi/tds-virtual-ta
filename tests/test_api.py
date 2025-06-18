import requests

def test_virtual_ta():
    response = requests.post(
        "http://localhost:5000/ask",
        headers={"Content-Type": "application/json"},
        json={"question": "What is taught in week 2?"}
    )

    print("Status Code:", response.status_code)
    try:
        print("Response:", response.json())
    except Exception:
        print("Raw Response:", response.text)


if __name__ == "__main__":
    test_virtual_ta()
