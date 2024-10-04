import streamlit as st
import json
import os

# Function to store the healthcare preparedness data
def store_healthcare_preparedness_data():
    # Load existing JSON data or create a new dictionary if the file doesn't exist
    json_file_path = "baseline_data.json"
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            baseline_data = json.load(f)
    else:
        baseline_data = {}

    # Ensure the "healthcare_preparedness" key exists in the dictionary
    if "healthcare_preparedness" not in baseline_data:
        baseline_data["healthcare_preparedness"] = {}

    st.markdown("<h2 class='header'>Baseline Healthcare Preparedness Capability</h2>", unsafe_allow_html=True)

    # Section: Healthcare System Preparedness
    st.markdown("<h2 class='header'>Healthcare System Preparedness</h2>", unsafe_allow_html=True)

    # Function 1: Develop, refine, or sustain Healthcare Coalitions
    st.markdown("<b>Function 1: Develop, refine, or sustain Healthcare Coalitions.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["coalition_current_status"] = st.text_area("Current Status:", key="coalition_current_status")
    baseline_data["healthcare_preparedness"]["coalition_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="coalition_status_score")

    # Function 2: Coordinate with emergency management
    st.markdown("<b>Function 2: Coordinate with emergency management.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["emergency_management_current_status"] = st.text_area("Current Status:", key="emergency_management_current_status")
    baseline_data["healthcare_preparedness"]["emergency_management_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="emergency_management_status_score")

    # Function 3: Identify and prioritize healthcare assets and essential services
    st.markdown("<b>Function 3: Identify and prioritize healthcare assets and essential services.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["healthcare_assets_current_status"] = st.text_area("Current Status:", key="healthcare_assets_current_status")
    baseline_data["healthcare_preparedness"]["healthcare_assets_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="healthcare_assets_status_score")

    # Function 4: Perform resource assessments and develop plans
    st.markdown("<b>Function 4: Perform resource assessments and develop plans.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["resource_assessment_current_status"] = st.text_area("Current Status:", key="resource_assessment_current_status")
    baseline_data["healthcare_preparedness"]["resource_assessment_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="resource_assessment_status_score")

    # Function 5: Coordinate training for healthcare responders
    st.markdown("<b>Function 5: Coordinate training for healthcare responders.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["training_current_status"] = st.text_area("Current Status:", key="training_current_status")
    baseline_data["healthcare_preparedness"]["training_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="training_status_score")

    # Function 6: Coordinate an exercise, evaluation, and corrective action program
    st.markdown("<b>Function 6: Coordinate an exercise, evaluation, and corrective action program.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["exercise_program_current_status"] = st.text_area("Current Status:", key="exercise_program_current_status")
    baseline_data["healthcare_preparedness"]["exercise_program_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="exercise_program_status_score")

    # Function 7: Participate with planning to address at-risk individuals
    st.markdown("<b>Function 7: Participate with planning to address at-risk individuals.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["at_risk_planning_current_status"] = st.text_area("Current Status:", key="at_risk_planning_current_status")
    baseline_data["healthcare_preparedness"]["at_risk_planning_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="at_risk_planning_status_score")

    # Healthcare System Preparedness Score
    st.markdown("<b>Healthcare System Preparedness Score</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["preparedness_score"] = st.text_input("Score:", value="Not Calculated", key="preparedness_score")

    # Section: Healthcare System Recovery
    st.markdown("<h2 class='header'>Healthcare System Recovery</h2>", unsafe_allow_html=True)

    # Function 1: Identify healthcare organization recovery needs
    st.markdown("<b>Function 1: Identify healthcare organization recovery needs.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["recovery_needs_current_status"] = st.text_area("Current Status:", key="recovery_needs_current_status")
    baseline_data["healthcare_preparedness"]["recovery_needs_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="recovery_needs_status_score")

    # Function 2: Maintain continuity of healthcare delivery
    st.markdown("<b>Function 2: Maintain continuity of the healthcare delivery.</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["continuity_current_status"] = st.text_area("Current Status:", key="continuity_current_status")
    baseline_data["healthcare_preparedness"]["continuity_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="continuity_status_score")

    # Healthcare System Recovery Score
    st.markdown("<b>Healthcare System Recovery Score</b>", unsafe_allow_html=True)
    baseline_data["healthcare_preparedness"]["recovery_score"] = st.text_input("Score:", value="Not Calculated", key="recovery_score")

    # Save the updated baseline data to the JSON file
    with open(json_file_path, 'w') as f:
        json.dump(baseline_data, f)

    st.success(f"Healthcare preparedness data saved to {json_file_path}!")


# Function to display the UI
def show():
    #st.title("Baseline Healthcare Preparedness")
    
    # Store healthcare preparedness data
    store_healthcare_preparedness_data()


# Run the healthcare preparedness page
show()
