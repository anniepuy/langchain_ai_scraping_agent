"""
Title: LinkedIn Scraper.py
Purpose: Scrapes using third party API and LLM to extract information from LinkedIN profiles
Author: Ann Hagan
Date: 2025--02-19
"""
import os 
import requests
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model='llama3.2', base_url="http://localhost:11434")

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIN profile using third party API"""
    try:
        if mock:
            linkedin_profile_url = "https://gist.githubusercontent.com/anniepuy/9e6238440f3e384b9ab18e4e00bd60fe/raw/c19b262cc666a2b28a9c37f1bfa2082f5b7f40ac/gistfile1.txt"
            response = requests.get(linkedin_profile_url, timeout=10)
        else: 
            api_endpoint = "https://api.scrapin.io/enrichment/profile"
            params = {
                "apikey": os.getenv("SCRAPIN_API_KEY"),
                "linkedInUrl": linkedin_profile_url,
            }
            response = requests.get(api_endpoint, params=params, timeout=10)
        
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json().get("person")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    profile_url = "https://www.linkedin.com/in/annhagan/"
    
    # Use mock=True for testing with the mock data
    result = scrape_linkedin_profile(profile_url, mock=True)
    
    if result:
        print("Profile data:")
        print(result)



