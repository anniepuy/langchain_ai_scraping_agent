"""
Title: Simple Langchain.py
Purpose: Simple Langchain Prompt Template implementation
Author: Ann Hagan
Resource: https://python.langchain.com/docs/tutorials/llm_chain/
Date: 2025-02-20
"""

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


llm = ChatOllama(model='llama3.2', base_url="http://localhost:11434", temperature=0)

#1. Create your prompt template
summary_template = """
given the information {information} about a topic I want you to create:
1. A short summary
2. Two intersting facts about the topic
"""

#Summary template
summary_prompt_template = PromptTemplate(input_variables="information", template = summary_template)


#Create the chain
chain = summary_prompt_template | llm 

information = """Naval Ship Maintenance"""

response = chain.invoke(input={"information": information})
print(response.content)
