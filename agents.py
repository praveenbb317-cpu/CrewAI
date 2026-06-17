from crewai import Agent
from langchain_ollama import ChatOllama


llm=llm="ollama/llama3.2:1b"

researcher = Agent(
    llm=llm,
    role="senior researcher analyst",
    goal="conduct in depth research and analysis on the complex topic o.",
    backstory="You are a senior researcher analyst with expertise in conducting in-depth research and analysis on complex topics.",
    verbose=True,
)

writer = Agent(
    llm=llm,
    role="creative writer",
    goal="craft enngaging and comprehensive reports based on the research and analysis conducted by the researcher.",
    backstory="You are an experienced writer with a strong background in writing comprehensive reports based on research and analysis.",
    verbose=True,
)

reviewer = Agent(
    llm=llm,
    role="critical reviewer",
    goal="evaluate the reports written by the writer, providing constructive feedback and suggestions for improvement.",
    backstory="You are a critical reviewer with expertise in evaluating reports and providing constructive feedback for improvement.",
    verbose=True,
)




