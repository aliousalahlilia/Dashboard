import streamlit as st
from PIL import Image

def setup_page():
    st.set_page_config(
        page_title="CNAS Fraud Detection Dashboard",
        page_icon=Image.open("assets/favicon.ico"),
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            body {
                background-color: #f0f2f6;
            }
            .main {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .sidebar .sidebar-content {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .stButton>button {
                background-color: #0072bb;
                color: white;
                border-radius: 5px;
                padding: 10px;
                border: none;
            }
            .stButton>button:hover {
                background-color: #005f8d;
                color: white;
            }
            .stTextInput>div>input {
                border-radius: 5px;
                padding: 10px;
                border: 1px solid #d1d1d1;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )