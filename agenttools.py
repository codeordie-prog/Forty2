import os
from query_database import QueryDataBase
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import tool



class AgentTools(QueryDataBase):

    def __init__(self):
        super().__init__()
       
        self.CHROMA_PATH = "./data/CHROMA_PATH5(assistant_info)"
        self.CHROMA_PATH1 = "./data/CHROMA_PATH5(assistant_info)"
        self.CHROMA_PATH2 ="./data/CHROMA_PATH5(assistant_info)"
        self.CHROMA_PATH3 = "./data/CHROMA_PATH5(assistant_info)"
        self.CHROMA_PATH4 = "./data/CHROMA_PATH5(assistant_info)"
        self.CHROMA_PATH5 = "./data/CHROMA_PATH5(assistant_info)"

    
    
    #medical information tool
    def medical_info_tool(self):

        try:

            chroma_path = self.CHROMA_PATH
            if os.path.exists(chroma_path):
                retriever = self.get_retriever(chroma_path)

                medical_retriever_tool = create_retriever_tool(
                    retriever,
                    "medical_search",
                    """Search for medical information from the database. For any medical enquiry, you must use this tool!,there are several sources
                    including the British National Formulary and several treatment guidelines use them to get the best information""",
                )

                return medical_retriever_tool
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("An error occured during tool use. path provided for medical info retrieval is not correct.")
    
    #tool2
    def personal_info_tool(self):
        try:

            chroma_path = self.CHROMA_PATH2

            if os.path.exists(chroma_path):
                    
                retriever = self.get_retriever(chroma_path)

                personal_info_retriever_tool = create_retriever_tool(
                    retriever,
                    "personal_document_search",
                    "search for personal information about the user, this includes interests, resumes,schedules, meetings,journals, friends,email etc. use this tool when personal info access is required"
                )

                return personal_info_retriever_tool
            else:
                raise FileNotFoundError
            
        except FileNotFoundError:
            print("An error occured during tool use. The path to personal info is not correct. check it")
    
    #tool3
    def book_reference_tool(self):

        try:

            chroma_path = self.CHROMA_PATH3

            if os.path.exists(chroma_path):

                retriever = self.get_retriever(chroma_path)

                book_ref_tool = create_retriever_tool(
                    retriever,
                    "book_references",
                    """reference to books in the database to obtain relevant response. there will be several books, 
                    information retrieval might require several references or just a single book reference,
                    make sure you mention which book you used and what chapter. use this tool to sharpen accuracy of response about specific topics
                    if the relevant info cannot be found in the available books, you dont have to rely on this tool for the response."""
                )

                return book_ref_tool
            
            else:
                raise FileNotFoundError
            
        except FileNotFoundError:

            print("An error occured during book reference tool use. Check the path provided for chroma database inside the tools")

    
    #tool4
    def research_tool(self):

        try:

            chroma_path = self.CHROMA_PATH4

            if os.path.exists(chroma_path):

                retriever = self.get_retriever(chroma_path)

                research_tool = create_retriever_tool(retriever,
                                                      "research_tool",
                                                      """Research papers and journals references to sharpen accuracy of the response. 
                                                      To stick to the scientific methodology and first principles thinking, use this tool to get relevant research 
                                                      findings on specific topics. use this tool to augment your knowledge and give relevant, 
                                                      scientific accurate responses""")
                
                return research_tool
            
            else:
                raise FileNotFoundError
            
        except FileNotFoundError:

            print("An error occured during research tool use. check the path to the chroma data base.")

    #tool6
    def assistant_info(self):

        try:

            chroma_path = self.CHROMA_PATH5

            if os.path.exists(chroma_path):

                retriever = self.get_retriever(chroma_path)

                AI_info_tool = create_retriever_tool(
                    retriever,
                    "AI_assistant_info",
                    """use this tool to know your background, your creator, 
                    purpose and other info relating to you. use it to respond to any enquiries about you or this interaction interface."""
                )

                return AI_info_tool
            
            else:
                raise FileNotFoundError
            
        except FileNotFoundError:

            print("An error occured, fix the path to source info about the AI assistant")

    #tool7
    def retreiver_tool(self):

        retrieve = create_retriever_tool()
    
    #get study mate tools

    def study_mate_tools(self):

        research = self.research_tool()
        book_tool = self.book_reference_tool()
        AI_info = self.assistant_info()

        return [research,book_tool,AI_info] 
     
    #getter for the tools
    def get_tools(self):

        medical_tool = self.medical_info_tool()
        personal_info_tool = self.personal_info_tool()
        research = self.research_tool()
        book_references = self.book_reference_tool()
        AI_info = self.assistant_info()
        tools =  [medical_tool,AI_info,personal_info_tool,research,book_references]
        return tools
