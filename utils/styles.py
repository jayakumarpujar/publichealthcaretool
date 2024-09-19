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
                margin-top: 10px;
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
            body {
            background-color: #f5f5f5;
            color: black;
            font-family: Arial, sans-serif;
            }

            .main-container {
                background-color: #e6e6fa;
                padding: 20px;
                border-radius: 10px;
                width: 80%;
                margin: 0 auto;
            }

            .header {
                text-align: center;
                color: black;
                font-size: 32px;
                margin-bottom: 20px;
            }

            .subheader {
                color: #333333;
                font-size: 24px;
                margin-top: 20px;
            }

            .label {
                font-weight: bold;
                margin-top: 10px;
                display: block;
            }

            .text-input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                border: 1px solid #cccccc;
                background-color: #ffffff;
                color: black;
                font-size: 16px;
            }

            textarea.text-input {
                resize: vertical;
                height: 100px;
            }

            select.text-input {
                height: 40px;
            }

            h3, h4, h5 {
                color: black;
                margin-top: 20px;
            }

            p {
                color: black;
                line-height: 1.5;
            }

            .probability-section, .impact-section {
                background-color: #d9ead3;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
            }
            
            .human-impact {
                background-color: #d9d2e9;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
            }
            .stRadio > div {
                margin-bottom: 0; /* Remove bottom margin */
            }
            .stRadio > div > label {
                margin-bottom: 0; /* Remove bottom margin */
            }
            .input-label {
            font-weight: bold;
            color: black;
            margin-bottom: 5px; /* Reduced bottom margin */
            }
        .result-text {
            font-size: 16px; /* Reduced font size */
            font-weight: bold;
            color: black;
            margin-top: 10px; /* Optional, reduce the top margin */
        }
            </style>
    """, unsafe_allow_html=True)
