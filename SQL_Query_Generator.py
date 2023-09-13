#!/usr/bin/env python3

import streamlit as st 
import openai
from utils import *
from dotenv import load_dotenv
import os
#'Get OpenAI API Key': "https://platform.openai.com/account/api-keys",
def main():
    """
    Main Function
    """
    st.set_page_config(
        page_title="SQL Query Generator",
        # page_icon="./assets/favicon.png",
        layout= "centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/satyadevshetty/ChatGPT-SQLQueryGenerator',
        'Report a bug': "https://github.com/satyadevshetty/ChatGPT-SQLQueryGenerator/issues",
        'About': "## Generate SQL queries using Generative AI built with Python and Streamlit"
        } )
    st.title("SQL Query Generator")
    
    hide_footer()
    hide_hamburger_menu()
    # Load and display animation
    anim = lottie_local(r"./assets/animations/queryking.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=300,
            width=300,
            key=None)
    openai.api_key = st.text_input("ChatGPT api_key",placeholder="Get API Key from https://platform.openai.com/account/api-keys")
    query = st.text_area("Enter the desired question to generate SQL Query")
    # openai.api_key = st.secrets["openai_api_key"]
    load_dotenv()
    # openai.api_key = os.environ["openai_api_key"]
    
    prompt = f"Translate this natural language query into syntactically correct SQL:\n\n{query}\n\nSQL Query:"
    chb = st.checkbox("Table Schema")
    if chb:
        schema = st.text_area("Enter Table Schema")
        prompt = f"Translate this natural language query into syntactically correct SQL:\n\n{query}\n\nUse this table schema:\n\n{schema}\n\n{prompt}"
    model_engine = "text-davinci-003"
    if st.button("✍️ Generate SQL Query"):
        try:
            if openai.api_key:
                completion = openai.Completion.create(
                            engine=model_engine,
                            prompt=prompt,
                            max_tokens=2048,
                            n=1,
                            stop = "\\n",
                            temperature=0.5,
                            frequency_penalty = 0.5,
                            presence_penalty = 0.5,
                            logprobs = 10)

                response = completion.choices[0].text
                st.balloons()
                st.markdown("### Output:")
                st.text(f"{response}")
            else:
                st.write("Please input openai_api_key")
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()