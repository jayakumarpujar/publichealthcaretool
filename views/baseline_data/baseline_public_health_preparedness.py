import streamlit as st
import json
import os

# Function to store the public health preparedness data
def store_public_health_preparedness_data():
    # Load existing JSON data or create a new dictionary if the file doesn't exist
    json_file_path = "baseline_data.json"
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            baseline_data = json.load(f)
    else:
        baseline_data = {}

    # Ensure the "public_health_preparedness" key exists in the dictionary
    if "public_health_preparedness" not in baseline_data:
        baseline_data["public_health_preparedness"] = {}

    st.markdown("<h2 class='header'><b>Community Preparedness</b></h2>", unsafe_allow_html=True)

    # Function 1: Determine risks to the health of the jurisdiction
    st.markdown("<b>Function 1: Determine risks to the health of the jurisdiction.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["risks_current_status"] = st.text_area("Current Status:", key="risks_current_status")
    baseline_data["public_health_preparedness"]["risks_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="risks_status_score")

    # Function 2: Build community partnerships to support health preparedness
    st.markdown("<b>Function 2: Build community partnerships to support health preparedness.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["partnerships_current_status"] = st.text_area("Current Status:", key="partnerships_current_status")
    baseline_data["public_health_preparedness"]["partnerships_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="partnerships_status_score")

    # Function 3: Engage with community organizations to foster public health, medical, and mental/behavioral health social networks
    st.markdown("<b>Function 3: Engage with community organizations to foster social networks.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["social_networks_current_status"] = st.text_area("Current Status:", key="social_networks_current_status")
    baseline_data["public_health_preparedness"]["social_networks_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="social_networks_status_score")

    # Function 4: Coordinate training or guidance to ensure community engagement in preparedness efforts
    st.markdown("<b>Function 4: Coordinate training or guidance to ensure community engagement.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["training_current_status"] = st.text_area("Current Status:", key="training_current_status")
    baseline_data["public_health_preparedness"]["training_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="training_status_score")

    # Community Preparedness Score
    st.markdown("<b>Community Preparedness Score</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["preparedness_score"] = st.text_input("Score:", value="Not Calculated", key="preparedness_score")

    st.markdown("<h2 class='header'>Community Recovery</h2>", unsafe_allow_html=True)

    # Function 1: Identify and monitor public health, medical, and mental/behavioral health system recovery needs
    st.markdown("<b>Function 1: Identify and monitor system recovery needs.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["recovery_needs_current_status"] = st.text_area("Current Status:", key="recovery_needs_current_status")
    baseline_data["public_health_preparedness"]["recovery_needs_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="recovery_needs_status_score")

    # Function 2: Coordinate community public health, medical, and mental/behavioral health system recovery operations
    st.markdown("<b>Function 2: Coordinate system recovery operations.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["recovery_operations_current_status"] = st.text_area("Current Status:", key="recovery_operations_current_status")
    baseline_data["public_health_preparedness"]["recovery_operations_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="recovery_operations_status_score")

    # Function 3: Implement corrective actions to mitigate damages from future incidents
    st.markdown("<b>Function 3: Implement corrective actions to mitigate damages from future incidents.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["corrective_actions_current_status"] = st.text_area("Current Status:", key="corrective_actions_current_status")
    baseline_data["public_health_preparedness"]["corrective_actions_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="corrective_actions_status_score")

    # Community Recovery Score
    st.markdown("<b>Community Recovery Score</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["recovery_score"] = st.text_input("Score:", value="Not Calculated", key="recovery_score")

    # Other sections (e.g., Emergency Operations Coordination, Emergency Public Info, etc.) follow the same pattern:
    # Ensure unique keys for each section to avoid DuplicateWidgetID errors, and store each section in the same `baseline_data.json` file.

    # Example for Emergency Operations Coordination
    st.markdown("<h2 class='header'>Emergency Operations Coordination</h2>", unsafe_allow_html=True)
    st.markdown("<b>Function 1: Conduct preliminary assessment.</b>", unsafe_allow_html=True)
    baseline_data["public_health_preparedness"]["emergency_preliminary_assessment_current_status"] = st.text_area("Current Status:", key="emergency_preliminary_assessment_current_status")
    baseline_data["public_health_preparedness"]["emergency_preliminary_assessment_status_score"] = st.text_input("Status Score:", value="Not Calculated", key="emergency_preliminary_assessment_status_score")

    # Save the updated baseline data to the JSON file
    with open(json_file_path, 'w') as f:
        json.dump(baseline_data, f)

    st.success(f"Public health preparedness data saved to {json_file_path}!")


# Function to display the UI
def show():
    #st.title("Baseline Public Health Preparedness")
    
    # Store public health preparedness data
    store_public_health_preparedness_data()


# Run the public health preparedness page
show()
