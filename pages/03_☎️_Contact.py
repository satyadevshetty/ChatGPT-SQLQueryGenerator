"""
Feedback Page using formsubmit.co API
"""
import streamlit as st
from utils import *
from PIL import Image
from streamlit_card import card




st.set_page_config(
        page_title="SQL Query Generator | Feedback",
        # page_icon="./assets/favicon.png",
        layout= "centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/satyadevshetty/ChatGPT-SQLQueryGenerator',
        'Report a bug': "https://github.com/satyadevshetty/ChatGPT-SQLQueryGenerator/issues",
        'About': "## Generate SQL queries using Generative AI built with Python and Streamlit"
        } )


st.title("🤝🏽 Get in Touch")

hide_footer()
hide_hamburger_menu()

hasClicked = card(
        title="Satyadev Shetty",
        text="Entrepreneur",
        image="https://avatars.githubusercontent.com/u/49232059?v=4",
        url="https://github.com/satyadevshetty"
        )
        

st.write("### Want to Sponsor Me?")

st.write("[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/satyashetty)")

