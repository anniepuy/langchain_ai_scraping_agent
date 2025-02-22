"""
Title: Simple Langchain.py
Purpose: Simple Langchain Prompt Template implementation
Author: Ann Hagan
Resource: https://python.langchain.com/docs/tutorials/llm_chain/
Date: 2025-02-20
"""

from linkedin_scraper import scrape_linkedin_profile
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOllama(model='llama3.2', base_url="http://localhost:11434", temperature=0)

#1. Create your prompt template
summary_template = """
given the LinkedIn profile information {information} about a topic I want you to create:
1. A short summary
2. Two intersting facts about the topic
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template = summary_template)

chain = summary_prompt_template | llm 

linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/annhagan/", mock=True)

response = chain.invoke(input={"information": linkedin_data})
print(response.content)