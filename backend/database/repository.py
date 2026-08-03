import json
from database.connection import DatabaseConnection
from database.models import VerificationReport

class ReportRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS verification_reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            article_url TEXT NULL,
            article_text LONGTEXT NULL,
            credibility_score DECIMAL(5,2) NOT NULL,
            claim_extraction_data LONGTEXT NULL,
            api_verification_data LONGTEXT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def save_report(self, report: VerificationReport) -> int:
        query = """
        INSERT INTO verification_reports 
        (article_url, article_text, credibility_score, claim_extraction_data, api_verification_data) 
        VALUES (%s, %s, %s, %s, %s)
        """
        claims_str = json.dumps(report.claim_extraction_data) if report.claim_extraction_data else None
        api_str = json.dumps(report.api_verification_data) if report.api_verification_data else None

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (
            report.article_url,
            report.article_text,
            float(report.credibility_score),
            claims_str,
            api_str
        ))
        conn.commit()
        inserted_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return inserted_id

    def get_all_reports(self):
        query = "SELECT id, article_url, article_text, credibility_score, created_at FROM verification_reports ORDER BY created_at DESC"
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
