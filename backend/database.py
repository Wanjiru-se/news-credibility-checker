from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    input_type = db.Column(db.String(10), nullable=False)
    article_content = db.Column(db.Text, nullable=False)
    credibility_score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    claims = db.relationship('ExtractedClaim', backref='report', lazy=True, cascade="all, delete-orphan")

class ExtractedClaim(db.Model):
    __tablename__ = 'extracted_claims'
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('reports.id'), nullable=False)
    claim_text = db.Column(db.Text, nullable=False)
    verdict = db.Column(db.String(50))
    explanation = db.Column(db.Text)
