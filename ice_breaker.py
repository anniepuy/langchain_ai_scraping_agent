"""
Title: Ice Breaker.py
Purpose: Sample LangChain Prompt Template implementation 
Author: Ann Hagan from Eden Marco's Udemy Course
Date: 2025--02-19
"""

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from agents.twitter_lookup_agent import lookup as twitter_lookup
from agents.linkedin_lookup_agent import lookup as linkedin_lookup
from output_parsers import summary_parser




#1. Create your prompt template inside a function
def ice_breaker_(name: str) -> str:
    linkedin_username = linkedin_lookup(name=name)
    twitter_username = twitter_lookup(name=name)
    
    summary_template = """
    given the information about a person from linkedin {information} about the person from the Linkedin and Twitter, I want you to create:
    1. A short summary
    2. Two intersting facts about the person

    Use both information from twitter and LinkedIn.
    \n{format_instructions}
    """

    #Summary template
    summary_prompt_template = PromptTemplate(input_variables=["information", "twitter_username"], template = summary_template,
                                             partial_variables={"format_instructions": summary_parser.get_format_instructions()})
    
    llm = ChatOllama(model='llama3.2', base_url="http://localhost:11434", temperature=0)

    #Create the chain
    chain = summary_prompt_template | llm  | summary_parser

    response = chain.invoke(input={"information": linkedin_username, "twitter_username": twitter_username})
    return response.content

if __name__ == "__main__":
    print(ice_breaker_("Eden Marco Udemy Instructor"))
