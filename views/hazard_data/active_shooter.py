import streamlit as st
import os
import json

from views.baseline_data.community_characteristics import handle_form_submission

# Paths to your JSON files
hazard_data_file = 'hazard_data.json'
baseline_data_file = 'baseline_data.json'

# Function to load data from the baseline_data.json file
def load_baseline_data():
    if os.path.exists(baseline_data_file):
        with open(baseline_data_file, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                st.error("Error loading baseline data: Invalid JSON format.")
                return {}
    else:
        st.error("Baseline data file not found.")
        return {}


# Function to load data from the hazard_data.json file
def load_hazard_data():
    if os.path.exists(hazard_data_file):
        with open(hazard_data_file, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # If the file is empty or contains invalid JSON, return an empty dict
                return {}
    return {}

# Function to save data to the hazard_data.json file
def save_data(page_key, data):
    try:
        # Load existing data from the hazard_data.json file
        if os.path.exists(hazard_data_file):
            with open(hazard_data_file, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Update the data for this page using the page_key
        existing_data[page_key] = data

        # Save updated data back to the file
        with open(hazard_data_file, 'w') as file:
            json.dump(existing_data, file, indent=4)

        st.success("Data saved successfully!")
    except Exception as e:
        st.error(f"Error saving data: {e}")



# Prefill form with baseline data (e.g., Baseline Mortality per Day)
def prefill_form():
    baseline_data = load_baseline_data()
    
    # Example: Prefill "Baseline Mortality per Day" from baseline_data.json  -> total deaths per day
    baseline_mortality = baseline_data.get("total_deaths_per_day", 0.0)  # Default to 0.0 if not found
    baseline_ems_transport = baseline_data.get("total_transports_per_day", 0.0)
    baseline_ed_visists = baseline_data.get("total_ed_visits_per_day", 0.0)
    baseline_primary_care_office = baseline_data.get("total_office_visits_per_day",0.0)
    baseline_trauma_center_injuries = baseline_data.get("total_trauma_injuries_per_day",0.0)

    # Ensure baseline_mortality is a float
    try:
        baseline_mortality = float(baseline_mortality)
        baseline_ems_transport = float(baseline_ems_transport)
        baseline_ed_visists = float(baseline_ed_visists)
        baseline_primary_care_office = float(baseline_primary_care_office)
        baseline_trauma_center_injuries = float(baseline_trauma_center_injuries)
    except ValueError:
        baseline_mortality = 0.0  # Fallback if value can't be converted to float
        baseline_ems_transport = 0.0
        baseline_ed_visists = 0.0
        baseline_primary_care_office =0.0
        baseline_trauma_center_injuries =0.0


    # Prefill the session state for Baseline Mortality
    if "Baseline Mortality per Day" not in st.session_state:
        st.session_state["Baseline Mortality per Day"] = baseline_mortality

    if "Baseline Transports per Day" not in st.session_state:
        st.session_state["Baseline Transports per Day"] = baseline_ems_transport
    
    if "Baseline ED Visits per Day" not in st.session_state:
        st.session_state["Baseline ED Visits per Day"] = baseline_ed_visists

    if "Baseline Primary Care Office Visits" not in st.session_state:
        st.session_state["Baseline Primary Care Office Visits"]= baseline_primary_care_office
    
    if "Baseline Trauma Center Injuries" not in st.session_state:
        st.session_state["Baseline Trauma Center Injuries"]= baseline_trauma_center_injuries


def show():
    # Prefill the form if data exists
    prefill_form()

    st.markdown("""
    <p>An active shooter is an individual actively engaged in killing or attempting to kill people in a confined and other populated area. 
    In most cases, active shooters use firearms and there is no pattern or method to their selection of victims. Active shooter situations 
    are unpredictable and evolve quickly (FEMA, 2011). The shooter in an active shooter scenario may be a sniper. A sniper is a concealed, 
    usually skilled shooter who fires at exposed persons, typically using powerful high-energy, military-style assault rifles. 
    Assault rifles are becoming more available to the public (Ciottone, 2006).</p>
    <p>The following hazard impacts have been estimated using historical data, predictive models, estimations where necessary, and 
    the information entered in the "Baseline Data" worksheets. The information below can be altered as needed to more accurately 
    reflect hazard impacts in your jurisdiction. The impacts should reflect the worst-case reasonable scenario.</p>
    """, unsafe_allow_html=True)

    st.markdown("<p>Briefly describe the worst-case reasonable scenario of this hazard (the scenario to which the following impacts apply) here:</p>", unsafe_allow_html=True)
    st.text_area("", "The proxy scenario used to predict the impacts of an active shooter incident in Southeastern Pennsylvania is the Virginia Tech Massacre of 2007. On April 16, 2007, student Seung Hui Cho murdered 32 and injured 17 students and faculty in two related incidents on the campus of Virginia Polytechnic Institute.")
    
    st.markdown("<h3>Probability</h3>", unsafe_allow_html=True)

    # Define the mapping of probability descriptions to scores
    probability_mapping = {
        "The probability of the occurrence of the hazard is zero.": 0,
        "The hazard is not likely to occur in the system lifecycle (100 years), but it is possible.": 1,
        "The hazard is likely to occur at least once in the system lifecycle (100 years).": 2,
        "The hazard is likely to occur several times in the system lifecycle (100 years).": 3,
        "The hazard is likely to occur cyclically or annually in the system lifecycle (100 years).": 4
    }

    # Get the user's selection and determine the score
    selected_probability = st.selectbox(
        "Probability:",
        list(probability_mapping.keys()),
        index=2,
        key="probability_radio"
    )
    probability_score = probability_mapping[selected_probability]
    
    st.markdown(f"**Probability Score:** {probability_score} {'Occasional' if probability_score == 2 else ''}", unsafe_allow_html=True)


    st.markdown("<h3 style='text-align: center;'>Human Impact</h3>", unsafe_allow_html=True)
    
    # Human Impact Sections
    handle_section("Mortality", "Baseline Mortality per Day", "Hazard-Related Increase in Mortality per Day",   "In the VA Tech Massacre of 2007, 33 died at the scene, including the shooter (Armstrong & Frykberg, 2007).")
    handle_ems_section("EMS Transports", "Baseline Transports per Day", "Hazard-Related Increase in Transports per Day",  "In the VA Tech Massacre of 2007, 17 were transported by EMS (Armstrong & Frykberg, 2007).")
    handle_ed_visits_section("ED Visits", "Baseline ED Visits per Day", "Hazard-Related Increase in ED Visits per Day",   "In the VA Tech Massacre of 2007, 27 were treated at local emergency departments (Virginia Tech Review Panel, 2007).")
    handle_ed_visits_section("Primary Care Office Visits", "Baseline Office Visits per Day", "Hazard-Related Increase in Office Visits per Day", "Please provide data")
    handle_ed_visits_section("Trauma Center Injuries", "Baseline Trauma Injuries per Day", "Hazard-Related Increase in Trauma Injuries per Day",   "In the VA Tech Massacre of 2007, 10 were taken to Level III trauma centers, and 2 to Level I centers (Armstrong & Frykberg, 2007).")

def calculate_magnitude_score(baseline, increase):
    # Convert baseline and increase to floats, and handle any potential non-numeric values
    try:
        baseline = float(baseline)
        increase = float(increase)
    except ValueError:
        return "Not calculated"

    if baseline == 0 or baseline == "NA":
        return "Not calculated"
    
    # Calculate the ratio (Baseline + Hazard-Related Increase) / Baseline
    ratio = (baseline + increase) / baseline
    if ratio <= 1:
        return 0
    elif ratio <= 1.05:
        return 1
    elif ratio <= 1.5:
        return 2
    elif ratio <= 2:
        return 3
    else:
        return 4

def handle_section(section_title, baseline_label, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)
    
    baseline_value = st.session_state.get(baseline_label, "Not Calculated")
    st.markdown(f"**{baseline_label}:** {baseline_value}")

    
    # Hazard-Related Increase (editable by user, converted to float)
    hazard_increase = st.number_input(increase_label, value=0, key=f"{section_title}_hazard_increase")
    
    # Calculate Magnitude Score
    magnitude_score = calculate_magnitude_score(baseline_value, hazard_increase)
    st.markdown(f"**Magnitude Score:** {magnitude_score}")
    st.markdown("""
        <ul>
            <li>0: No change from baseline</li>
            <li>1: ≤ 5% increase</li>
            <li>2: ≤ 50% increase</li>
            <li>3: ≤ 100% increase</li>
            <li>4: > 100% increase</li>
        </ul>
    """, unsafe_allow_html=True)
    
    # Qualitative Magnitude Score (user can select)
    qualitative_option = st.selectbox("OR, Estimate the Magnitude Qualitatively:", 
                                      ["Use Quantitative Value", "No change from baseline (Score = 0)", 
                                       "≤ 5% increase (Score = 1)", "≤ 50% increase (Score = 2)", 
                                       "≤ 100% increase (Score = 3)", ">100% increase (Score = 4)"], 
                                      index=0, key=f"{section_title}_qualitative")
    
    # If qualitative option is not "Use Quantitative Value", extract the score
    if qualitative_option != "Use Quantitative Value":
        qualitative_score = int(qualitative_option.split("Score = ")[-1][0])
    else:
        qualitative_score = None
    
    # Duration of Impact (user can select)
    duration_option = st.selectbox("Duration of Impact:", 
                                   ["No impact (Score = 0)", "≤ 1 day (Score = 1)", 
                                    "≤ 1 week (Score = 2)", "≤ 2 weeks (Score = 3)", 
                                    "> 2 weeks (Score = 4)"], 
                                   index=0, key=f"{section_title}_duration")
    
    # Calculate Duration Score
    duration_score = int(duration_option.split("Score = ")[-1][0])
    
    # Data Source / Explanation (Optional)
    st.text_area("Data Source / Explanation (Optional):", default_explanation, key=f"{section_title}_explanation")
    
    # Calculate final score
    if qualitative_score is None and magnitude_score == "Not calculated":
        final_score = "Not Calculated/NA"
    elif qualitative_score is not None:
        final_score = (qualitative_score + duration_score) / 2
    else:
        final_score = (magnitude_score + duration_score) / 2
    
    # Display the final mortality score
    st.markdown(f"**Mortality Score:** {final_score}")

# New function to handle EMS Transports
def handle_ems_section(section_title, baseline_label, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)

    baseline_value = st.session_state.get(baseline_label, "Not Calculated")
    st.markdown(f"**{baseline_label}:** {baseline_value}")

    # Hazard-Related Increase (editable by user)
    hazard_increase = st.number_input(increase_label, value=0, key=f"{section_title}_hazard_increase")

    # Calculate Magnitude Score based on EMS Transports logic
    magnitude_score = calculate_magnitude_score(baseline_value, hazard_increase)
    st.markdown(f"**Magnitude Score:** {magnitude_score}")
    st.markdown("""
        <ul>
            <li>0: No change from baseline</li>
            <li>1: ≤ 5% increase</li>
            <li>2: ≤ 50% increase</li>
            <li>3: ≤ 100% increase</li>
            <li>4: > 100% increase</li>
        </ul>
    """, unsafe_allow_html=True)

    # Qualitative Magnitude Score (user can select)
    qualitative_option = st.selectbox("OR, Estimate the Magnitude Qualitatively:", 
                                      ["Use Quantitative Value", "No change from baseline (Score = 0)", 
                                       "≤ 5% increase (Score = 1)", "≤ 50% increase (Score = 2)", 
                                       "≤ 100% increase (Score = 3)", ">100% increase (Score = 4)"], 
                                      index=0, key=f"{section_title}_qualitative")

    # If qualitative option is not "Use Quantitative Value", extract the score
    if qualitative_option != "Use Quantitative Value":
        qualitative_score = int(qualitative_option.split("Score = ")[-1][0])
    else:
        qualitative_score = None

    # Duration of Impact (user can select)
    duration_option = st.selectbox("Duration of Impact:", 
                                   ["No impact (Score = 0)", "≤ 1 day (Score = 1)", 
                                    "≤ 1 week (Score = 2)", "≤ 2 weeks (Score = 3)", 
                                    "> 2 weeks (Score = 4)"], 
                                   index=0, key=f"{section_title}_duration")

    # Calculate Duration Score
    duration_score = int(duration_option.split("Score = ")[-1][0])

    # Data Source / Explanation (Optional)
    st.text_area("Data Source / Explanation (Optional):", default_explanation, key=f"{section_title}_explanation")

    # Calculate final score for EMS Transports
    if qualitative_score is None and magnitude_score == "Not calculated":
        final_score = "Not Calculated/NA"
    elif qualitative_score is not None:
        final_score = (qualitative_score + duration_score) / 2
    else:
        final_score = (magnitude_score + duration_score) / 2

    # Display the final EMS Transport score
    st.markdown(f"**{section_title} Score:** {final_score}")


# Function to handle ED Visits section 
def handle_ed_visits_section(section_title, baseline_label, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)
    
    baseline_value = st.session_state.get(baseline_label, "Not Calculated")
    st.markdown(f"**{baseline_label}:** {baseline_value}")

    # Hazard-Related Increase (editable by user)
    hazard_increase = st.number_input(increase_label, value=0, key=f"{section_title}_hazard_increase")

    # Calculate Magnitude Score based on ED Visits logic
    magnitude_score = calculate_magnitude_score(baseline_value, hazard_increase)
    st.markdown(f"**Magnitude Score:** {magnitude_score}")
    st.markdown("""
        <ul>
            <li>0: No change from baseline</li>
            <li>1: ≤ 5% increase</li>
            <li>2: ≤ 50% increase</li>
            <li>3: ≤ 100% increase</li>
            <li>4: > 100% increase</li>
        </ul>
    """, unsafe_allow_html=True)

    # Qualitative Magnitude Score (user can select)
    qualitative_option = st.selectbox("OR, Estimate the Magnitude Qualitatively:", 
                                      ["Use Quantitative Value", "No change from baseline (Score = 0)", 
                                       "≤ 5% increase (Score = 1)", "≤ 50% increase (Score = 2)", 
                                       "≤ 100% increase (Score = 3)", ">100% increase (Score = 4)"], 
                                      index=0, key=f"{section_title}_qualitative")

    # If qualitative option is not "Use Quantitative Value", extract the score
    if qualitative_option != "Use Quantitative Value":
        qualitative_score = int(qualitative_option.split("Score = ")[-1][0])
    else:
        qualitative_score = None

    # Duration of Impact (user can select)
    duration_option = st.selectbox("Duration of Impact:", 
                                   ["No impact (Score = 0)", "≤ 1 day (Score = 1)", 
                                    "≤ 1 week (Score = 2)", "≤ 2 weeks (Score = 3)", 
                                    "> 2 weeks (Score = 4)"], 
                                   index=0, key=f"{section_title}_duration")

    # Calculate Duration Score
    duration_score = int(duration_option.split("Score = ")[-1][0])

    # Data Source / Explanation (Optional)
    st.text_area("Data Source / Explanation (Optional):", default_explanation, key=f"{section_title}_explanation")

    # Calculate final ED Visits score
    if qualitative_score is None and magnitude_score == "Not calculated":
        final_score = "Not Calculated/NA"
    elif qualitative_score is not None:
        final_score = (qualitative_score + duration_score) / 2
    else:
        final_score = (magnitude_score + duration_score) / 2

    # Display the final ED Visits score
    st.markdown(f"**{section_title} Score:** {final_score}")

# Run the function to display the webpage
show()
