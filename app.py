from agent_executor import Agent_Executor
from parallel_processing import ParallelProcessing
import streamlit as st


class App(ParallelProcessing):

    def __init__(self):
        super().__init__()
        self.chat_list = []


    def chatlist(self, response:str)->list:

        history = self.chat_list.append[response]

        return history

        

    def generate_response(self, openai_api_key : str, query : str):

        agent_executor = self.create_agent_executor("master",openai_api_key)

        response = agent_executor.invoke({"input":query})

        self.chatlist(response)

        return response['output']
        

        
def main():

    # Create an instance of App
    app = App()

    # Title of the Streamlit app
    st.markdown('<h1 style="color:blue; text-align:center;">42</h1>', unsafe_allow_html=True)


    # Text input for the user to enter the query
    query = st.text_input("Query: ")
    openai_api_key = st.text_input("Enter openai key :")

    # Function to save responses to a file or database
    def save_responses_to_file(response):
        # Implement this function to save responses to a file or database
        path = "C:/Users/LENOVO/Documents/Agent_responses/"
        with open(path.join("response.txt"), "a") as f:
            for response in response:
                f.write(response + "\n")
        st.write("Responses saved successfully!")



    # Button to submit the query and process the responses
    if st.button("Submit Query"):
        # Process the query and get the responses from the master agent
    
        response = app.generate_response(openai_api_key=openai_api_key,query=query)

        # Display the response
        st.write(f"Master response: {response}")
    

        # Button to save all responses
        if st.button("Save Response"):
            # Save the responses to a file or database
            save_responses_to_file(response)  # Implement this function as per your requirements


if __name__ == "__main__":
    main()


