from agent_executor import Agent_Executor
import threading
import queue
import streamlit as st


class ParallelProcessing(Agent_Executor):

    def __init__(self):
        super().__init__()

    # Define args
    def set_args(self, query: str) -> tuple:
        args = [(query, "master"), (query, "researcher"), (query, "evaluator")]
        return args
    
    #just for the master agent
    def master_response(self,query:str,openai_api_key:str)->str:

        executor = self.create_agent_executor("master",openai_api_key=openai_api_key)
        response = executor.invoke({"input":query})
        return response['output']
    
    # Define task 1
    def task(self, args: tuple, result_queue: queue.Queue) -> None:
        query, agent_type = args
        executor = self.create_agent_executor(agent_type)
        response = executor.invoke({"input": query})
        result_queue.put(response['output'])

    # Define task 2
    def task2(self, response: str, args: tuple, result_queue: queue.Queue) -> None:
        query, agent_type = args
        input_string = f"based on the query: {query}, the first agent responded as follows: {response}"
        executor = self.create_agent_executor("researcher")
        response = executor.invoke({"input": input_string})
        result_queue.put(response['output'])
    
    # Define task 3
    def task3(self, response: str, response1:str, args: tuple, response_queue: queue.Queue) -> None:
        query, agent_type = args
        input_string = f"""after careful evaluation based on research documents from the database for the query: {query}, 
        the first agent responded as follows: {response} and the second as follows {response1}"""
        executor = self.create_agent_executor("evaluator")
        response = executor.invoke({"input": input_string})
        response_queue.put(response['output'])

    # Define workflow
    def work_flow(self, args_tuple: tuple) -> list:
        # Set the queue to hold the responses
        response_queue = queue.Queue()
        responses = []

        # Thread for the first agent
        thread = threading.Thread(target=self.task, args=(args_tuple[0], response_queue))
        thread.start()
        thread.join()

        # Response from the first agent
        response_from_first_agent = response_queue.get()
        responses.append(response_from_first_agent)

        # Thread for the second agent
        thread = threading.Thread(target=self.task2, args=(response_from_first_agent, args_tuple[1], response_queue))
        thread.start()
        thread.join()

        # Response from the second agent
        response_from_second_agent = response_queue.get()
        responses.append(response_from_second_agent)

        # Thread for the third agent
        thread = threading.Thread(target=self.task3, args=(response_from_first_agent,response_from_second_agent, args_tuple[2], response_queue))
        thread.start()
        thread.join()

        # Response from the third agent
        response_from_third_agent = response_queue.get()
        responses.append(response_from_third_agent)

        return responses

def main():

    work_flow = ParallelProcessing()

    st.markdown('<h1 style="color:blue; text-align:center;">42 R.O.Y.F</h1>', unsafe_allow_html=True)

    # Text input for the user to enter the query
    query = st.text_input("Query: ")

    my_tuple = [(query,"master"),(query,"researcher"),(query,"evaluator")]

    # Button to submit the query and process the responses
    if st.button("Submit Query"):
        # Process the query and get the responses from the agents


        responses = work_flow.work_flow(my_tuple)

        master_response = responses[0]
        researcher_response = responses[1]
        evaluator_response = responses[2]

        # Text areas to display the responses
        st.subheader("Responses:")
        st.write("Master response:")
        st.text_area("Master response area", value=master_response, height=200)
        st.write("Researcher response:")
        st.text_area("Researcher response area", value=researcher_response, height=200)
        st.write("Evaluator comment:")
        st.text_area("Evaluator comment area", value=evaluator_response, height=200)



if __name__ == "__main__":
    main()