from scraper_chain.langchain_with_scraper import process_linkedin_profile

profile_url = "https://www.linkedin.com/in/annhagan/"
summary = process_linkedin_profile(profile_url)
print("\nProfile Analysis:")
print(summary) 