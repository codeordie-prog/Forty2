from typing import Type
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,SystemMessagePromptTemplate,HumanMessagePromptTemplate,PromptTemplate


class PromptTemplateForExecutor:

    """This class creates the prompt template passed to the agent
    Advantages of using this template which includes the prompt in the LanguageModelManager class as the system message is:
    
    1. Creates memory for the agent
    2. Maintains context in the conversations through consistently injecting the system message to the agent"""    

    #constructor
    def __init__(self):
        pass

       

    #generates the prompt template
    def generate_the_template(self) -> ChatPromptTemplate:

        exec_prompt = ChatPromptTemplate.from_messages(

                    [
                        SystemMessagePromptTemplate(
                        prompt=PromptTemplate(input_variables=[], 
                        template='You are a helpful assistant.')),

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