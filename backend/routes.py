from flask import Blueprint, request, jsonify
from database import db, Report, ExtractedClaim

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/reports', methods=['POST'])
def save_report():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    try:
        new_report = Report(
            input_type=data.get('input_type'),
            article_content=data.get('article_content'),
            credibility_score=data.get('credibility_score', 0)
        )
        db.session.add(new_report)
        db.session.flush()
        
        claims_list = data.get('claims', [])
        for item in claims_list:
            new_claim = ExtractedClaim(
                report_id=new_report.id,
                claim_text=item.get('claim_text'),
                verdict=item.get('verdict'),
                explanation=item.get('explanation')
            )
            db.session.add(new_claim)
            
        db.session.commit()
        return jsonify({"message": "Report saved successfully!", "report_id": new_report.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500

@api_blueprint.route('/api/reports', methods=['GET'])
def get_report_history():
    try:
        reports = Report.query.order_by(Report.created_at.desc()).all()
        history = []
        for report in reports:
            claims_data = [{
                "claim_text": c.claim_text,
                "verdict": c.verdict,
                "explanation": c.explanation
            } for c in report.claims]
            
            history.append({
                "id": report.id,
                "input_type": report.input_type,
                "article_content": report.article_content,
                "credibility_score": report.credibility_score,
                "created_at": report.created_at.isoformat(),
                "claims": claims_data
            })
        return jsonify(history), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve history", "details": str(e)}), 500
