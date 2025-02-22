"""
Title: Twitter Lookup Agent
Author: Ann Hagan via Eden Marco's Udemy Course
Date: 2025-02-22
Purpose: The agent will a Twitter username. Uses React Agent from LangChain HUB.
"""

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub
from tools.tavily_search_tool import get_profile_url_tavily


load_dotenv()

#look up person function
def lookup(name: str) -> str:
    llm = ChatOllama(model='llama3.2', base_url="http://localhost:11434", temperature=0)
    template = """ Given the full name {name_of_person} I want you to get me a link to their Twitter Profile and extract the username.
    Your answer should contain only twitter username."""

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
    tools_for_agent = [Tool(
        name="Crawl Google for Twitter profile page.", 
        func=get_profile_url_tavily, 
        description="Useful for when you need to get a Twitter usename.",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})

    linked_profile_url = result["output"]
    return linked_profile_url

if __name__ == "__main__":
    # Test the lookup function
    name = "Eden Marco"
    result = lookup(name)
    print("\nTwitter username:")
    print(result)