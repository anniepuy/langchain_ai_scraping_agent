"""
Title: Websearch.py
Purpose: Sample LangChain Prompt Template implementation with Wikipedia
Author: Ann Hagan 
Date: 2025-02-19
"""

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.tools import Tool
from output_parsers import summary_parser

# Create the Wikipedia tool
wikipedia = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    description="Useful for searching Wikipedia articles",
    func=wikipedia.run
)

def web_search(name: str) -> str:
    """Search Wikipedia and generate a summary about a person"""
    try:
        # Use Wikipedia Search
        wikipedia_info = wikipedia_tool.run(name)  # Changed from invoke to run
        
        if not wikipedia_info:
            return "No information found for this person."

        summary_template = """
        Given the information about a person from Wikipedia: {information}, 
        I want you to create:
        1. A short summary
        2. Two interesting facts about the person

        Use only information from Wikipedia.
        \n{format_instructions}
        """

        # Summary template
        summary_prompt_template = PromptTemplate(
            input_variables=["information"],
            template=summary_template,
            partial_variables={"format_instructions": summary_parser.get_format_instructions()}
        )

        # Initialize LLM
        llm = ChatOllama(model='llama3.2', base_url="http://localhost:11434", temperature=0)

        # Create the chain
        chain = summary_prompt_template | llm | summary_parser

        response = chain.invoke(input={"information": wikipedia_info})
        return response.content

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Test with multiple examples
    test_names = ["Joe Biden", "Elon Musk", "Invalid Person Name"]
    for name in test_names:
        print(f"\nSearching for: {name}")
        print("-" * 50)
        result = web_search(name)
        print(result)
        print("-" * 50)