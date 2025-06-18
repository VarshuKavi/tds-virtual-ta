# TDS Virtual Teaching Assistant 🤖📘

A virtual assistant for IIT Madras' *Tools for Data Science* course that automatically responds to student questions using course content and AI (GPT-4).

---

## 📚 Features

- Automatically answers questions about course content
- Uses content scraped and saved as structured JSON
- Supports **OpenAI API** and **mock mode** for testing
- Flask API with a single POST endpoint `/ask`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tds-virtual-ta.git
cd tds-virtual-ta
```

### 2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Create a .env File
OPENAI_API_KEY=your_openai_key_here
USE_OPENAI=true

To enable mock mode, set USE_OPENAI=false.

### 5.Running the App
python run.py

### 6.Making a Request
You can ask questions using curl or Postman.
Example:
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is taught in week 2?"}'

### 7. Testing
Run the test script from the tests/ directory:
python tests/test_api.py

### 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

### Author
Varshini M
MCA, B.Com (CA)
IIT Madras Online Degree – Data Science