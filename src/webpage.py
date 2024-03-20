import dotenv
import os
import pandas as pd
import streamlit as st


def config_webpage(title: str) -> None:
    st.set_page_config(page_title=title)
    st.header(title)

    st.sidebar.header("DataChain")
    st.sidebar.markdown("""
       This is a toy application designed by Nicolás Maturana,
       upload you csv file and ask questions to the chatbot to perform
       simple data analysis tasks.
    """)


def input_api_key() -> str:
    dotenv.load_dotenv()  # load environment variables
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        st.sidebar.divider()
        openai_api_key = st.sidebar.text_input(
            "OpenAI API Key", type="password"
        )
    return openai_api_key


def clear_button() -> bool:
    st.sidebar.divider()
    clear = st.sidebar.button("Clear conversation history")
    return clear


def load_dataframe() -> pd.DataFrame:
    uploaded_file = st.file_uploader(
        "Upload your dataset",
        type=["csv"],
        on_change=_clear_submit,
    )
    if not uploaded_file:
        st.warning(
            """
            This app uses LangChain's `PythonAstREPLTool` which is vulnerable
            to arbitrary code execution. Please use caution in deploying and
            sharing this app.
            """
        )

    if uploaded_file:
        df = _load_data(uploaded_file)
    else:
        df = pd.DataFrame()
    return df


def _clear_submit():
    st.session_state["submit"] = False


@st.cache_data(ttl="1h")
def _load_data(uploaded_file):
    extension = os.path.splitext(uploaded_file.name)[1][1:].lower()
    if extension == 'csv':
        return pd.read_csv(uploaded_file)
    else:
        st.error(f"Unsupported file format: {extension}")
        return None
