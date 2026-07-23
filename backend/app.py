from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {
        "message": "News Credibility Checker backend is running"
    }


@app.route("/analyze", methods=["POST"])
def analyze_article():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data was submitted."
        }), 400

    input_type = data.get("inputType")
    content = data.get("content", "").strip()

    if not content:
        return jsonify({
            "error": "Please provide article text or a news article URL."
        }), 400

    # Placeholder results for the project skeleton.
    # Group members will later replace this with real AI and API logic.
    result = {
        "inputType": input_type,
        "credibilityScore": 75,
        "claims": [
            {
                "claim": "This is a sample extracted claim.",
                "status": "Supported",
                "source": "https://example.com/source-one"
            },
            {
                "claim": "This is another sample claim.",
                "status": "Inconclusive",
                "source": "https://example.com/source-two"
            }
        ]
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)