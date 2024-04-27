
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from agents import Agents

class Agent_Executor(Agents):

    def __init__(self):
        super().__init__()

    

    def create_agent(self,llm, agent : str) -> Agents:

        llm = llm
        tools = self.get_tools()
        prompt=self.set_prompt(agent=agent)
        agent = create_openai_functions_agent(llm,tools,prompt)

        return agent

    #create the agent executor
    def create_agent_executor(self, agent_type:str):
        
        tools = self.get_tools()

        agent = self.create_agent(llm = ChatOpenAI(),agent=agent_type)

        agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)


        return agent_executor
    
"""
ae = Agent_Executor()

exec = ae.create_agent_executor()

chathistory = []

response = exec.invoke({"input":"what is the last video youtube i watched?"})
    

print(response)"""



