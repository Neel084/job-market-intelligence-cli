import requests
import os 
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

BASE_URL = "https://api.adzuna.com/v1/api/jobs"

def fetch_jobs(keywords , country="in",result_per_page=10):
    url = f"{BASE_URL}/{country}/search/1"

    params = {

        "app_id" : APP_ID,
        "app_key" : APP_KEY,
        "what" : keywords,
        "results_per_page" : result_per_page,
        "content-type" : "application/json"
    }

    response = requests.get(url,params = params, timeout = 5)

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")
    

    data = response.json()

    if "results" in data:
        return data["results"]
    else:
        raise Exception("No result found in response !!")
    