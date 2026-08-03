import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_team_secret_key_12345')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'mysql+pymysql://root:YOUR_PASSWORD_HERE@localhost/news_credibility_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
