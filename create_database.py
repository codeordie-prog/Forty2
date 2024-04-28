import os
import shutil
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain_community.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PDFMinerLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)

class CreateDataBase:

    def __init__(self):

        pass
    

    #loader mapper for doc extensions - function 1
    def loader_mapping(self):

        LOADER_MAPPING = {

            ".csv": (CSVLoader, {"encoding": "utf-8"}), #specify encoding utf-8 very important
            ".doc": (UnstructuredWordDocumentLoader, {}),
            ".docx": (UnstructuredWordDocumentLoader, {}),
            ".enex": (EverNoteLoader, {}),
            ".epub": (UnstructuredEPubLoader, {}),
            ".html": (UnstructuredHTMLLoader, {}),
            ".md": (UnstructuredMarkdownLoader, {}),
            ".odt": (UnstructuredODTLoader, {}),
            ".pdf": (PDFMinerLoader, {}),
            ".ppt": (UnstructuredPowerPointLoader, {}),
            ".pptx": (UnstructuredPowerPointLoader, {}),
            ".txt": (TextLoader, {"encoding": "utf8"}),
        }

        return LOADER_MAPPING  

    
    #load multiple documents - function 2
    def load_multiple_documents(self, dir_path: str):

        try:

            if not os.path.exists(dir_path):

                raise FileNotFoundError

            documents = []
            map = self.loader_mapping()

            for file in os.listdir(dir_path):
                ext = "." + file.rsplit(".", 1)[-1]

                if ext in map :
                    
                    loader_class, loader_args = map[ext]
                    # Create a new loader instance for each file
                    loader = loader_class(os.path.join(dir_path, file), **loader_args)
                    # Append the loaded documents from the current file
                    documents.extend(loader.load())
                else:
                    # Handle unsupported extensions (optional: log a message)
                    pass

            return documents

        except FileNotFoundError:

            print(f"directory path {dir_path} doesn't exist, check the path you specified to load documents from")

        
        except Exception as e:

            print("an error occured ",e)

        

    
    #split documents into chunks - function 3
    def split_loaded_documents(self, documents : list[Document]):

        try:

            text_splitter = RecursiveCharacterTextSplitter( #define a splitter
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
            )

            chunks = text_splitter.split_documents(documents) #split the documents
            print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

        
            return chunks
        
        except Exception as e:

            print("during splitting of chunks an error occured.", e)
    

    #save to database - function 5
    def save_to_chroma(self,chunks: list[Document], CHROMA_PATH : str):

        try:
            # Clear out the database first.
            
            if os.path.exists(CHROMA_PATH):
                shutil.rmtree(CHROMA_PATH)

            # Create a new DB from the documents.

            persist_directory = CHROMA_PATH
            

            db = Chroma.from_documents(
                        chunks, OpenAIEmbeddings(), persist_directory=persist_directory
                    )
            db.persist()
            print(f"Saved {len(chunks)} chunks to {persist_directory}.")
        
        except FileNotFoundError:

            print("the specified directory for CHROMA PATHS do not exist, please check the directories")

        except Exception as e:

            print("an error occured during saving to chroma database, check the specified directories please.")
            



    #for test purposes - function 6
    def generate_data_store(self, directory_path : str, CHROMA_PATH : str):

        try:

            if os.path.exists(directory_path) and os.path.exists(CHROMA_PATH):

                documents = self.load_multiple_documents(directory_path)
                chunks = self.split_loaded_documents(documents)
                self.save_to_chroma(chunks, CHROMA_PATH)

            else:
                raise FileNotFoundError
            
        except FileNotFoundError:

            print("An error occured during generation of the database function, review the specified directory and CHROMA_PATHS")

        except Exception as e:

            print("An exception was encountered during the generation of the database function, review the paths specified")


#to do list - 1. handle directory path error
'''
def main():

    cd = CreateDataBase()
    chroma_path =r"C:\Users\LENOVO\Documents\forty2\data\CHROMA_PATH5(assistant_info)"
    directory_path = r"C:\Users\LENOVO\Documents\test\aiinfo"
    cd.generate_data_store(directory_path,chroma_path)

if __name__ == "__main__":
    main()'''




        