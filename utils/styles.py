import streamlit as st

def set_styles():
    st.markdown("""
        <style>
            .main {
                background-color: #f5f5f5;
                padding: 20px;
                color: black;
            }
            .stButton button {
                background-color: red;
                color: white;
                text-align: center;
                font-size: 20px;
                border-radius: 10px;
                margin: 20px;
                align-items: center;
                padding: 20px;
                width: 300px;
                height: 60px;
                border: none;
                transition: 0.2s;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.7);
            }
            .text-input {
                margin-top: -10px;
                background-color: white;
                color: black;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .input-container {
                display: flex;
                flex-direction: column;
                gap: 7px;
                margin-bottom: 15px;
            }
            .title {
                text-align: center;
                color: red;
                font-size: 40px;
                margin-top: 20px;
            }
            .subtitle {
                text-align: center;
                color: black;
                font-size: 20px;
            }
            .content {
                color: black;
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.7);
            }
            .header { color: black; font-size: 24px; text-align: center; }
            .footer {
                text-align: center;
                margin-top: 20px;
                color: grey;
            }
            .back-option {
                position: absolute;
                top: 20px;
                right: 20px;
                font-size: 18px;
                color: blue;
                cursor: pointer;
            }
            .back-option:hover {
                text-decoration: underline;
            }
        </style>
    """, unsafe_allow_html=True)
