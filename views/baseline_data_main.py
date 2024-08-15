import streamlit as st
from views.baseline_data import (
    baseline_health_services,
    baseline_at_risk_populations,
    baseline_public_health_preparedness,
    baseline_healthcare_preparedness,
    community_characteristics
)

def show():
    st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='header'>Step 1. Baseline Data</h2>", unsafe_allow_html=True)

    option = st.selectbox("Choose an option", [
        "Baseline Health, Services, and Infrastructure",
        "Baseline At-Risk Populations",
        "Baseline Public Health Preparedness Capability",
        "Baseline Healthcare Preparedness Capability",
        "Community Characteristics"
    ])

    if option == "Baseline Health, Services, and Infrastructure":
        baseline_health_services.show()
    elif option == "Baseline At-Risk Populations":
        baseline_at_risk_populations.show()
    elif option == "Baseline Public Health Preparedness Capability":
        baseline_public_health_preparedness.show()
    elif option == "Baseline Healthcare Preparedness Capability":
        baseline_healthcare_preparedness.show()
    elif option == "Community Characteristics":
        community_characteristics.show()
