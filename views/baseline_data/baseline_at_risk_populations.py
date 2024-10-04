import streamlit as st
import json
import os

# Function to store baseline at-risk population data
def store_at_risk_population_data():
    # Load the existing JSON data if it exists, or create a new dictionary
    json_file_path = "baseline_data.json"
    
    # Check if the file exists
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            baseline_data = json.load(f)
    else:
        baseline_data = {}

    # If "at_risk_population" key doesn't exist, create it
    if "at_risk_population" not in baseline_data:
        baseline_data["at_risk_population"] = {}

    st.markdown("<h2>At-Risk Population Data</h2>", unsafe_allow_html=True)

    # Hearing Disability Section
    st.markdown("<b>Hearing Disability</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["hearing_disability_percent"] = st.text_input("Percent of Population with a Hearing Disability:", value="0", key="hearing_disability_percent")
    baseline_data["at_risk_population"]["hearing_population_size_score"] = st.text_input("Population Size Score:", value="0", key="hearing_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["hearing_data_source"] = st.text_input("Enter data source for Hearing Disability", key="hearing_data_source")

    # Vision Disability Section
    st.markdown("<b>Vision Disability</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["vision_disability_percent"] = st.text_input("Percent of Population with a Vision Disability:", value="0", key="vision_disability_percent")
    baseline_data["at_risk_population"]["vision_population_size_score"] = st.text_input("Population Size Score:", value="0", key="vision_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["vision_data_source"] = st.text_input("Enter data source for Vision Disability", key="vision_data_source")

    # Ambulatory Disability Section
    st.markdown("<b>Ambulatory Disability</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["ambulatory_disability_percent"] = st.text_input("Percent of Population with an Ambulatory Disability:", value="0", key="ambulatory_disability_percent")
    baseline_data["at_risk_population"]["ambulatory_population_size_score"] = st.text_input("Population Size Score:", value="0", key="ambulatory_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["ambulatory_data_source"] = st.text_input("Enter data source for Ambulatory Disability", key="ambulatory_data_source")

    # Cognitive Disability Section
    st.markdown("<b>Cognitive Disability</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["cognitive_disability_percent"] = st.text_input("Percent of Population with a Cognitive Disability:", value="0", key="cognitive_disability_percent")
    baseline_data["at_risk_population"]["cognitive_population_size_score"] = st.text_input("Population Size Score:", value="0", key="cognitive_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["cognitive_data_source"] = st.text_input("Enter data source for Cognitive Disability", key="cognitive_data_source")

    # Limited English Proficiency Section
    st.markdown("<b>Limited English Proficiency</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["limited_english_percent"] = st.text_input("Percent of Population with Limited English Proficiency:", value="0", key="limited_english_percent")
    baseline_data["at_risk_population"]["limited_english_population_size_score"] = st.text_input("Population Size Score:", value="0", key="limited_english_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["limited_english_data_source"] = st.text_input("Enter data source for Limited English Proficiency", key="limited_english_data_source")

    # Poverty Section
    st.markdown("<b>Poverty</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["poverty_percent"] = st.text_input("Percent of Population in Poverty:", value="0", key="poverty_percent")
    baseline_data["at_risk_population"]["poverty_population_size_score"] = st.text_input("Population Size Score:", value="0", key="poverty_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["poverty_data_source"] = st.text_input("Enter data source for Poverty", key="poverty_data_source")

    # Chronic Diseases (Diabetes) Section
    st.markdown("<b>Chronic Diseases (Diabetes)</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["diabetes_percent"] = st.text_input("Percent of Population with Diabetes:", value="0", key="diabetes_percent")
    baseline_data["at_risk_population"]["diabetes_population_size_score"] = st.text_input("Population Size Score:", value="0", key="diabetes_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["diabetes_data_source"] = st.text_input("Enter data source for Diabetes", key="diabetes_data_source")

    # Children Under 18 Section
    st.markdown("<b>Children Under 18</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["children_under_18_percent"] = st.text_input("Percent of Population Under Age 18:", value="0", key="children_under_18_percent")
    baseline_data["at_risk_population"]["children_population_size_score"] = st.text_input("Population Size Score:", value="0", key="children_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["children_data_source"] = st.text_input("Enter data source for Children Under 18", key="children_data_source")

    # Elderly 65 and Older Section
    st.markdown("<b>Elderly 65 and Older</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["elderly_percent"] = st.text_input("Percent of Population Age 65 and Older:", value="0", key="elderly_percent")
    baseline_data["at_risk_population"]["elderly_population_size_score"] = st.text_input("Population Size Score:", value="0", key="elderly_population_size_score")
    st.markdown("<b>Data Source:</b>", unsafe_allow_html=True)
    baseline_data["at_risk_population"]["elderly_data_source"] = st.text_input("Enter data source for Elderly Population", key="elderly_data_source")

    # Save the updated baseline data to the JSON file (without overwriting other pages' data)
    with open(json_file_path, 'w') as f:
        json.dump(baseline_data, f)

    st.success(f"At-Risk population data saved to {json_file_path}!")

# Function to display the UI
def show():
    #st.title("Baseline At-Risk Population Data")
    
    # Store at-risk population data
    store_at_risk_population_data()

# Run the at-risk population page
show()
