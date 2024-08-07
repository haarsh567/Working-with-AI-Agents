from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

## calling the Gemini model
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

##Creating a Researcher Agent with Memory

news_researcher=Agent(role="Senior Researcher",
                 goal='Uncover ground breaking technologies in {topic}',
                 verbose=True,
                 memory=True,
                 backstory=("Diven by curiosity, you are at the forefront of innovation,"
                            "eager to explore and share knowledge that could change the world."
),
tools=[tool],
llm=llm,
allow_delegations=True


)


##creating  a writer agent with custom tools responsible in writing news blog

news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accesssible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegations=False
)