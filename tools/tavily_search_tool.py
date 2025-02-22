"""
Title: Tavily Search Tool
Author: Ann Hagan
Date: 2025-02-22
Purpose: A langchain tool that uses the Tavily API to search the web.
"""


from langchain_community.tools.tavily_search import TavilySearchResults
import os

def get_profile_url_tavily(name: str):
    """Search the web for a person's LinkedIN  or Twitterprofile URL."""
    search = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))
    response = search.run(f"{name}")
    return response

