"""
Title: LinkedIn Scraper.py
Purpose: Scrapes using third party API and LLM to extract information from LinkedIN profiles
Author: Ann Hagan
Date: 2025--02-19
"""
from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

#pydantic object, extended from base Model which allows to define a schema for the output

class Summary(BaseModel):
    summary: str = Field(description="Summary of the entire text")
    facts: List[str] = Field(description="3-5 key facts about the text")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}
    

summary_parser = PydanticOutputParser(pydantic_object=Summary)
