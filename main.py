import streamlit as st
from utils.styles import set_styles
from utils.navigation import navigate

# Set page configuration
st.set_page_config(page_title="Public Health Care Risk Assessment Tool", layout="centered")

# Apply styles
set_styles()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Main Menu", "Baseline Data", "Hazard Data", "Analysis Options"])

# Navigate to selected page
navigate(page)

# Footer
st.markdown("<div class='footer'>© 2024 Public Health Risk Assessment Tool</div>", unsafe_allow_html=True)
st.markdown("---")
