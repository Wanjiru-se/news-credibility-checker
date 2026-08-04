import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def verify_claim(claim):
    """
    Searches Google's Fact Check API for a claim.
    """

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    params = {
        "query": claim,
        "key": GOOGLE_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }