from flask import Flask, request, jsonify
from database.repository import ReportRepository
from database.models import VerificationReport

app = Flask(__name__)

repo = ReportRepository()
repo.create_table_if_not_exists()
@app.route('/')
def home():
    return jsonify({"message": "News Credibility Checker backend is running"})

@app.route('/api/reports', methods=['POST'])
def save_analysis():
    data = request.json
    try:
        new_report = VerificationReport(
            article_url=data.get('article_url'),
            article_text=data.get('article_text'),
            credibility_score=data.get('credibility_score', 0.0),
            claim_extraction_data=data.get('claim_extraction_data'),
            api_verification_data=data.get('api_verification_data')
        )
        report_id = repo.save_report(new_report)
        return jsonify({"status": "success", "message": "Report stored successfully", "report_id": report_id}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        history = repo.get_all_reports()
        return jsonify({"status": "success", "history": history}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
