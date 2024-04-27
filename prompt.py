from langchain_core.prompts import PromptTemplate

class Prompttemplate:

    def __init__(self):

        pass


    def generate_prompt(self):

        template = """
       You are a smart assistant.
       Answer the questions in the most accurate way possible. No Bias,no censoring information or deviating from the truth. Always rely
       on the scientific methodology and first principle way of thinking prior to giving a response. Use context given to you for relevance.
       if the question is out of context, reply with "I don't know", else reference from the context and respond. A chat history is provided too, to aid this.

       context : {context}

       {chat_history}

        Human:{question}
        Assistant:"""

        prompt = PromptTemplate(template=template,input_variables=["context","chat_history","question"])

        return prompt

