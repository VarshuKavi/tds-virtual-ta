from flask import Blueprint, request, jsonify
from .gpt_engine import generate_response

bp = Blueprint('routes', __name__)

@bp.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data.get('question')
        if not question:
            return jsonify({"error": "No question provided"}), 400

        answer = generate_response(question)
        return jsonify({"answer": answer})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
