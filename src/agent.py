import pandas as pd

from langchain.agents.agent import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI


def get_pandas_agent(df: pd.DataFrame) -> AgentExecutor:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-1106",
        streaming=True
    )
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True
    )
    return agent
