import os
from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain.memory import ConversationBufferMemory
from prompt import Prompttemplate
from langchain.chains import (
    ConversationalRetrievalChain
)


class QueryDataBase(Prompttemplate):

    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(__file__)
        self.CHROMA_PATH = os.path.join(current_dir, 'data', 'CHROMA_PATH0(local)')
        #self.CHROMA_PATH1 = os.path.join(current_dir, 'Database', 'CHROMA_PATH0(local)')
        self.CHROMA_PATH2 = os.path.join(current_dir, 'data', 'CHROMA_PATH2(personal)')
        self.CHROMA_PATH3 = os.path.join(current_dir,'data','CHROMA_PATH3(books)')
        self.CHROMA_PATH4 = os.path.join(current_dir, 'data', 'CHROMA_PATH4(research_papers)')
        self.CHROMA_PATH5 = os.path.join(current_dir,'data','CHROMA_PATH5(assistant_info)')

    def get_retriever(self, CHROMA_PATH : str):

        try:

            embedding_function = OpenAIEmbeddings()

            db = Chroma(persist_directory=CHROMA_PATH,embedding_function=embedding_function)

            retriever = db.as_retriever()

            return retriever
        
        except FileNotFoundError:

            print("an error occured during get retriever function, check the  specified persist directory ")

        except Exception as e:

            print("an error occured during get_retriever method please check the persist directory or embedding model used")


    
    def retriever_chain(self,CHROMA_PATH: str): #specifify the CHROMA_PATH as personal,medical or local

        try:

            llm = ChatOpenAI()

            prompt = self.generate_prompt()

            memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True,output_key="answer")

            local_path =  self.CHROMA_PATH

            medical_docs_path = self.CHROMA_PATH

            personal_docs_path = self.CHROMA_PATH2


            if CHROMA_PATH == "personal":

                retriever = self.get_retriever(personal_docs_path)

            elif CHROMA_PATH == "medical":

                retriever = self.get_retriever(medical_docs_path)

            elif CHROMA_PATH == "local":

                retriever = self.get_retriever(local_path)

            else:
                raise ValueError


            chain = ConversationalRetrievalChain.from_llm(

                        llm=llm, 
                        retriever=retriever, #this ensures only relevant vectors with respect to the prompt are retrieved
                        memory=memory,
                        return_source_documents=True,
                        combine_docs_chain_kwargs={'prompt': prompt}
                        )
            
            return chain
        
        except FileNotFoundError:

            print("an error occured during chain retrieval function please check the paths specified for CHROMA_PATH data base for retrieval")

        except ValueError:

            print("The path provided for get_retriever chain was not valid. Please choose parameters: personal or medical")
        except Exception as e:

 
            print("an error was encountered during chain retreival, check the parameter passed for CHROMA_PATH, should be local,medical or personal")


 #test purposes       
"""
qd = QueryDataBase()

chain = qd.retriever_chain("local")

query = "what is your name?"

response = chain.invoke(query)

print(response['answer'])

  """      