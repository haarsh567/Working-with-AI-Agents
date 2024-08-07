import streamlit as st
from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Function to run the CrewAI process
def run_crewai(topic):
    # Initialize Crew
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )

    # Start the task execution process
    result = crew.kickoff(inputs={'topic': topic})
    return result

# Streamlit app
def main():
    st.title("CrewAI Research and Writing Tool")

    # Input for topic
    topic = st.text_input("Enter the topic you want to research:")

    # Button to start the process
    if st.button("Run Analysis"):
        if topic:
            with st.spinner("Processing..."):
                # Run the CrewAI process
                result = run_crewai(topic)
                
                # Display results
                st.subheader("Results")
                st.write(result)
        else:
            st.error("Please enter a topic to research.")

if __name__ == "__main__":
    main()
