# News Credibility Checker

A web-based system that helps users assess the credibility of news articles by extracting key claims, checking them against trusted sources, and generating a credibility report.

The system is being developed as a group project for SWE3040.

## Project Goal

The system allows users to submit either:

- News article text
- A news article URL

The final version will:

- Extract important claims from an article
- Search trusted news and fact-checking sources
- Classify claims as Supported, Unsupported, or Inconclusive
- Calculate an overall credibility score
- Display supporting evidence and source links

## Current Project Status

The project currently contains a working full-stack skeleton.

Implemented features:

- Article text submission
- Article URL submission
- Dynamic switching between text and URL inputs
- Empty input validation
- Flask backend
- Frontend-to-backend communication
- Placeholder credibility score
- Placeholder extracted claims
- Credibility report page
- Supporting source links

The current credibility results are placeholders. They will later be replaced with real AI and API-based verification.

## Technology Stack

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

### Backend

- Python
- Flask
- Flask-CORS

### Planned Integrations

- Gemini or OpenAI API
- Google Fact Check API
- News API
- MySQL

### Collaboration and Deployment

- GitHub
- GitHub Actions
- Render
- Trello

## Project Structure

```text
news-credibility-checker/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── extractor.py
│   ├── routes.py
│   ├── verifier.py
│   └── requirements.txt
│
├── database/
│
├── docs/
│
├── frontend/
│   ├── css/
│   ├── images/
│   ├── js/
│   │   ├── script.js
│   │   └── result.js
│   ├── index.html
│   └── result.html
│
├── .gitignore
└── README.md
