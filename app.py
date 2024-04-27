from agent_executor import Agent_Executor
from parallel_processing import ParallelProcessing as pp
import streamlit as st

# Create an instance of ParallelProcessing
flow = pp()

# Title of the Streamlit app
st.markdown('<h1 style="color:blue; text-align:center;">42 R.O.Y.F</h1>', unsafe_allow_html=True)

# Text input for the user to enter the query
query = st.text_input("Query: ")

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
   
    response = flow.master_response(query)

    # Display the response
    st.write(f"Master response: {response}")
   

    # Button to save all responses
    if st.button("Save Response"):
        # Save the responses to a file or database
        save_responses_to_file(response)  # Implement this function as per your requirements





