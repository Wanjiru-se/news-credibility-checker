from flask import Flask, request, jsonify
from flask_cors import CORS

from verifier import verify_claim

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

    # Call Google Fact Check API
    api_result = verify_claim(content)

    # If API returns an error
    if "error" in api_result:
        return jsonify(api_result), 500

    claims = api_result.get("claims", [])

    credibility_score = 0

    if len(claims) > 0:
        credibility_score = 90
    else:
        credibility_score = 40

    result = {
        "inputType": input_type,
        "credibilityScore": credibility_score,
        "googleFactCheck": claims
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)