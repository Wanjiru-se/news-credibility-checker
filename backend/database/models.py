from datetime import datetime

class VerificationReport:
    def __init__(self, report_id=None, article_url=None, article_text=None, 
                 credibility_score=0.0, claim_extraction_data=None, 
                 api_verification_data=None, created_at=None):
        self.report_id = report_id
        self.article_url = article_url
        self.article_text = article_text
        self.credibility_score = credibility_score
        self.claim_extraction_data = claim_extraction_data  
        self.api_verification_data = api_verification_data  
        self.created_at = created_at or datetime.utcnow()
