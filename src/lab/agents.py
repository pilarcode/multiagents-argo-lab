
import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Annotated, Literal, Any, Optional, List
from dataclasses import dataclass
from agno.models.ollama import Ollama
from agno.embedder.ollama import OllamaEmbedder
from agno.models.huggingface import HuggingFace
from agno.models.groq import Groq
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.serpapi import SerpApiTools
from agno.tools.csv_toolkit import CsvTools
from agno.vectordb.lancedb import LanceDb, SearchType
from lab.prompt import TEXT2SQL_TEMPLATE

@dataclass
class Text2SQLAgent:
	""" Text to SQL Agent to convert natural language to SQL """
	#FIXME refactor this
	ollama_model_name: str = "llama3.2:3b"
	agent_name: str  = "text2sql"
	role: str = "Text to SQL Agent"
	
	def __post_init__(self):
		# Instantiate the Ollama model
		self.ollama_model= Ollama(id=self.ollama_model_name)

		# Instantiate the agent
		self.text2sql_agent = Agent(model=self.ollama_model, 
								name=self.agent_name, 
								role=self.role,
								instructions=[TEXT2SQL_TEMPLATE], 
								show_tool_calls=True)


	def request(self, question):
		""" Run the agent and return the answer. """
		response = self.text2sql_agent.run(question)
		answer = response.content
		return answer
	
@dataclass
class RagAgent:
	""" RAG Agent to search the knowledge base """
	groq_model_name: str = "llama-3.1-8b-instant"
	agent_name: str = "Rag_agent"
	role: str = "Responds to questions about Thai recipes"
	def __post_init__(self):
		
		# Instantiate the embedder model 
		ollama_embedder = OllamaEmbedder(id="nomic-embed-text:latest",dimensions=768)

		# Define the database where the vector database will be stored
		db_url = "./tmp/lancedb"
		# Instantiate the vector database
		vector_db = LanceDb(
			table_name="recipes",  # Table name in the vector database
			uri=db_url,  # Location to initiate/create the vector database
			embedder=ollama_embedder,  # Without using this, it will use OpenAIChat embeddings by default
			search_type=SearchType.vector,
		)

		# Create a knowledge base of PDFs from URLs
		knowledge_base = PDFUrlKnowledgeBase(
			urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
			vector_db=vector_db
		)
		# Load the knowledge base
		knowledge_base.load(recreate=False)

		# Instantiate the Groq model
		self.groq_model=Groq(id="llama-3.1-8b-instant",api_key=os.getenv("GROQ_API_KEY"))

		# Instantiate the agent
		self.rag_agent = Agent(model=self,
              name=self.agent_name,
              role=self.role,
              knowledge=knowledge_base,  
              search_knowledge=False,
              show_tool_calls=True,
              markdown=False)

	def request(self, question):
		""" Run the agent and return the answer. """
		response = self.rag_agent.run(question)
		return response.content
	


@dataclass
class WebSearcherAgent:
	hg_model_name: str = "meta-llama/Meta-Llama-3-8B-Instruct"
	agent_name: str = "Web Searcher"
	role: str = "Searches the web for information on a topic"
	def __post_init__(self):

		if os.getenv("HUGGINGFACE_API_TOKEN") is None:
			raise ValueError("HUGGINGFACE_API_TOKEN is not defined in the .env file")
	
		# Instantiate the Hugging Face model
		self.hg_model = HuggingFace(id=self.hg_model_name, api_key=os.getenv("HUGGINGFACE_API_TOKEN"))
		# Instantiate the agent
		self.web_searcher = Agent(model=self.hg_model, 
							tools=[DuckDuckGoTools()], 
							name=self.agent_name,
							role=self.role, 
							show_tool_calls=True,
							markdown=False)

	def request(self, question):
		""" Run the agent and return the answer. """
		response = self.web_searcher.run(question)
		return response.content

@dataclass
class MultiAgentTeam:
	""" Multi-Agent Team that combines text2sql and rag agents """
	groq_model_name: str = "llama-3.1-8b-instant"
	agent_name: str = "Multi-Agent Team"
	role: str = "Team leader agent"
	def __post_init__(self):
		
		if os.getenv("GROQ_API_KEY") is None:
			raise ValueError("GROQ_API_KEY is not defined in the .env file")
		# Instantiate the Groq model
		self.groq_model=Groq(id=self.groq_model_name, api_key=os.getenv("GROQ_API_KEY"))

		# Initialize the agents as tools
		text2sql_agent = Text2SQLAgent()
		rag_agent = RagAgent()
		websearcher_agent = WebSearcherAgent()
		tools = [text2sql_agent, rag_agent,websearcher_agent]
		# Instantiate the agent
		self.team_leader = Agent(
			name=self.agent_name,
			role=self.role,
			model=self.groq_model,
			tools=tools,
			show_tool_calls=True,
			markdown=False,
			debug_mode=False,
		)
		

	def request(self, question):
		""" Run the agent and return the answer. """
		response = self.team_leader.run(question)
		return response.content
		
