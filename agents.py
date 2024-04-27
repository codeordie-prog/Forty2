from agenttools import AgentTools
from executor_prompt import PromptTemplateForExecutor as PTE
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    PromptTemplate)
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent


class Agents(AgentTools):

    def __init__(self) -> None:
        pass

    #set the prompt for the agents
    def set_prompt(self,agent: str)-> ChatPromptTemplate:

        if agent == "master":

            template_string = """You are a very smart Oracle. you are also connected to a database to augment your knowledge via tools provided.
            use them when needed to answer the user queries. if you don't know the answer to a given question and its not available from the database,
            just answer "I don't know". Your response is also being checked for quality and accuracy by another smart Oracle who might be smarter than you are,
            so give your best response to avoid criticism and damage of your reliability value. answer queries in the best way possible and even use analogies.
            Always reason first, if need be reference from the database and maintain first principles way of thinking, the way Richard Feynman would answer
            in deep fun detailed manner. Make learning fun and amazing. Jokes are allowed.
"""

        elif agent == "researcher":

            template_string = """You are a very smart Oracle. You are connected to an external database to augment your knowledge. You will receive
            a query and how another smart oracle just like you responded. Your role is to find what it might have missed, or any wrong information gives,
            correct it and mention where the correction was done or where an improvement is needed then provide a better response than the one you were presented
            with. If it satisfies your assesment of what a perfect, accurate and great response is, then you can respond with "quality satisfied" and stop.
            However always aim to contribute something even if its just a joke about the response. The main idea is to make learning fun through collaboration
            of multiple smart Oracles like you"""

        elif agent == "evaluator":

            template_string = """You are a very smart evaluator. You are part of a team aiming to make a certain human gain knowledge of topics 
            passed to you as queries. you will receive responses of how other oracles in your team responded and you have to evaluate and make a contribution.
            The nature of contribution is open for you to decide but the idea is to make the user grasp deep knowledge about the topic in a fun way.
            You are also equiped with tools to use the database that augments your knowledge, use them only when needed. Make sure you are prioritizing 
            first principles thinking, creativity, humor, and simplicity. The user loves simple analogies too."""

        else:

            template_string = "you are an assistant. answer the queries"

        exec_prompt = ChatPromptTemplate.from_messages(

                        [
                            SystemMessagePromptTemplate(
                            prompt=PromptTemplate(input_variables=[], 
                            template=template_string)),

                            MessagesPlaceholder(
                                variable_name='chat_history', 
                                optional=True),

                            HumanMessagePromptTemplate(
                                prompt=PromptTemplate(input_variables=['input'], template='{input}')),

                            MessagesPlaceholder(
                                variable_name='agent_scratchpad')
                        ]
                    )
        
        return exec_prompt
            
    #define master_agent
    def master_agent(self, llm):

        llm = llm

        tools = self.get_tools()

        prompt = self.set_prompt("master")

        agent = create_openai_functions_agent(llm,tools,prompt)

        return agent
    
    #researcher agent
    def researcher_agent(self,llm):

        llm = llm

        tools = self.get_tools()

        prompt = self.set_prompt("researcher")

        agent = create_openai_functions_agent(llm,tools,prompt)

        return agent

    #tutor
    def tutor_agent(self,llm):

        llm = llm

        tools = self.get_tools()

        prompt = self.set_prompt("evaluator")

        agent = create_openai_functions_agent(llm,tools,prompt)

        return agent