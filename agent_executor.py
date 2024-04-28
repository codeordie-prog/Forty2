
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from agents import Agents
import os

class Agent_Executor(Agents):

    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(__file__)
        self.CHROMA_PATH = os.path.join(current_dir, 'data', 'CHROMA_PATH0(local)')
        self.CHROMA_PATH1 = os.path.join(current_dir, 'data', 'CHROMA_PATH0(local)') #fix this
        self.CHROMA_PATH2 = os.path.join(current_dir, 'data', 'CHROMA_PATH2(personal)')
        self.CHROMA_PATH3 = os.path.join(current_dir,'data','CHROMA_PATH3(books)')
        self.CHROMA_PATH4 = os.path.join(current_dir, 'data', 'CHROMA_PATH4(research_papers)')
        self.CHROMA_PATH5 = os.path.join(current_dir,'data','CHROMA_PATH5(assistant_info)')


    

    def create_agent(self,llm, agent : str) -> Agents:

        llm = llm
        tools = self.get_tools()
        prompt=self.set_prompt(agent=agent)
        agent = create_openai_functions_agent(llm,tools,prompt)

        return agent

    #create the agent executor
    def create_agent_executor(self, agent_type:str, openai_api_key:str):
        
        tools = self.get_tools()

        agent = self.create_agent(llm = ChatOpenAI(api_key=openai_api_key),agent=agent_type)

        agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)


        return agent_executor
    
"""
ae = Agent_Executor()

exec = ae.create_agent_executor("master")

chathistory = []

response = exec.invoke({"input":"what is the last video youtube i watched?"})
    

print(response)"""



