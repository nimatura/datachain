import streamlit as st

from src.agent import get_pandas_agent
from src.webpage import (
    clear_button,
    config_webpage,
    input_api_key,
    load_dataframe
)
from langchain_community.callbacks import StreamlitCallbackHandler


def main():
    config_webpage(title="Ask your dataset")
    openai_api_key = input_api_key()
    clear = clear_button()

    df = load_dataframe()

    if "messages" not in st.session_state or clear:
        st.session_state["messages"] = [{
            "role": "assistant",
            "content": "Ask me a question about your CSV."
        }]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="What is this data about?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        agent = get_pandas_agent(df)

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(
                st.container(),
                expand_new_thoughts=False
            )
            answer = agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )
            st.write(answer)


if __name__ == "__main__":
    main()
