import streamlit as st
import os
import json

from views.baseline_data.community_characteristics import handle_form_submission

# Paths to your JSON files
AccExp_data_file = 'AccExp_data.json'
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


# Function to load data from the AccExp_data.json file
def load_AccExp_data():
    if os.path.exists(AccExp_data_file):
        with open(AccExp_data_file, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # If the file is empty or contains invalid JSON, return an empty dict
                return {}
    return {}

# Function to save data to the AccExp_data.json file
def save_data(page_key, data):
    try:
        # Load existing data from the AccExp_data.json file
        if os.path.exists(AccExp_data_file):
            with open(AccExp_data_file, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Update the data for this page using the page_key
        existing_data[page_key] = data

        # Save updated data back to the file
        with open(AccExp_data_file, 'w') as file:
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
    baseline_primary_care_office_visits = baseline_data.get("total_office_visits_per_day",0.0)
    baseline_trauma_center_injuries = baseline_data.get("total_trauma_injuries_per_day",0.0)
    ############################################################
    baseline_outpatient_services = baseline_data.get("total_pcps",0.0)
    baseline_ed_services = baseline_data.get("total_ed_beds",0.0)
    baseline_hospital_beds = baseline_data.get("hospital_beds_total",0.0)
    baseline_ancillary_service = baseline_data.get("total_pharmacists",0.0)
    baseline_trauma_center_or= baseline_data.get("total_trauma_units",0.0)
    baseline_mental_health_providers= baseline_data.get("total_mental_health_providers",0.0)

    # Ensure baseline_mortality is a float
    try:
        baseline_mortality = float(baseline_mortality)
        baseline_ems_transport = float(baseline_ems_transport)
        baseline_ed_visists = float(baseline_ed_visists)
        baseline_primary_care_office_visits = float(baseline_primary_care_office_visits)
        baseline_trauma_center_injuries = float(baseline_trauma_center_injuries)
        baseline_outpatient_services = float(baseline_outpatient_services)
        baseline_ed_services = float(baseline_ed_services)
        baseline_hospital_beds = float(baseline_hospital_beds)
        baseline_ancillary_service= float(baseline_ancillary_service)
        baseline_trauma_center_or= float(baseline_trauma_center_or)
        baseline_mental_health_providers= float(baseline_mental_health_providers)

    except ValueError:
        baseline_mortality = 0.0  # Fallback if value can't be converted to float
        baseline_ems_transport = 0.0
        baseline_ed_visists = 0.0
        baseline_primary_care_office_visits =0.0
        baseline_trauma_center_injuries =0.0
        baseline_outpatient_services =0.0
        baseline_ed_services =0.0
        baseline_hospital_beds = 0.0
        baseline_ancillary_service =0.0
        baseline_mental_health_providers=0.0
        baseline_trauma_center_or=0.0
        


    # Prefill the session state for Baseline Mortality
    if "Baseline Mortality per Day" not in st.session_state:
        st.session_state["Baseline Mortality per Day"] = baseline_mortality

    if "Baseline Transports per Day" not in st.session_state:
        st.session_state["Baseline Transports per Day"] = baseline_ems_transport
    
    if "Baseline ED Visits per Day" not in st.session_state:
        st.session_state["Baseline ED Visits per Day"] = baseline_ed_visists

    if "Baseline Office Visits per Day" not in st.session_state:
        st.session_state["Baseline Office Visits per Day"]= baseline_primary_care_office_visits
    
    if "Baseline Trauma Injuries per Day" not in st.session_state:
        st.session_state["Baseline Trauma Injuries per Day"]= baseline_trauma_center_injuries
    
    if "Baseline PCPs" not in st.session_state:
        st.session_state["Baseline PCPs"]= baseline_outpatient_services
    
    if "Baseline ED Beds" not in st.session_state:
        st.session_state["Baseline ED Beds"]= baseline_ed_services

    if  "Baseline Hospital Beds" not in st.session_state:
        st.session_state["Baseline Hospital Beds"]= baseline_hospital_beds
    
    if "Baseline Pharmacists" not in st.session_state:
        st.session_state["Baseline Pharmacists"]= baseline_ancillary_service
    
    if "Baseline Trauma Center ORs" not in st.session_state:
        st.session_state["Baseline Trauma Center ORs"]= baseline_trauma_center_or

    if "Baseline Mental Health Providers" not in st.session_state:
        st.session_state["Baseline Mental Health Providers"]=  baseline_mental_health_providers

def show():
    # Prefill the form if data exists
    prefill_form()
    # Load hazard data from file
    AccExp_data = load_AccExp_data()

    st.markdown("""
    <p>Any chemical compound, mixture, or device, the primary or common purpose of which is to function by explosion, i.e., with 
    substantially instantaneous release of gas and heat, unless such compound, mixture, or device is otherwise specifically classified 
    by the U.S. Department of Transportation; see 49 CFR chapter I. The term “explosives” shall include all material which is classified 
    as Class A, Class B, and Class C explosives by the U.S. Department of Transportation, and includes, but is not limited to dynamite,
    black powder, pellet powders, initiating explosives, blasting caps, electric blasting caps, safety fuse, fuse lighters, fuse igniters, 
    squibs, cordeau detonant fuse, instantaneous fuse, igniter cord, igniters, small arms ammunition, small arms ammunition primers, 
    smokeless propellant, cartridges for propellant-actuated power devices, and cartridges for industrial guns. Commercial explosives are 
    those explosives which are intended to be used in commercial or industrial operations (U.S. Department of Labor, n.d.).</p>
    <p>The following hazard impacts have been estimated using historical data, predictive models, estimations where necessary, and 
    the information entered in the "Baseline Data" worksheets. The information below can be altered as needed to more accurately 
    reflect hazard impacts in your jurisdiction. The impacts should reflect the worst-case reasonable scenario.</p>
    """, unsafe_allow_html=True)

    st.markdown("<p>Briefly describe the worst-case reasonable scenario of this hazard (the scenario to which the following impacts apply) here:</p>", unsafe_allow_html=True)
    st.text_area("", "The proxy scenario used to predict the impact of an accidental explosion in South Dakota is the following: The 2013  Fertilizer Plant Explosion and Fire in West, Texas. A fire had erupted at a fertilizer plant (Chemical Saftey Board, 2016). The explosion was caused by large quantities of ammonium nitrate at the plant facility. This chemical is used to make fertilizer, but it known to be highly unstable and dangerous when heated. The blast killed 15 people and injured 260.")
    
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
    save_data("probability_data", {"probability_score": probability_score})

    st.markdown("<h3 style='text-align: center;'>Human Impact</h3>", unsafe_allow_html=True)
    
    # Human Impact Sections
    handle_section("Mortality", "Baseline Mortality per Day", "Hazard-Related Increase in Mortality per Day",   "Please provide data")
    handle_ems_section("EMS Transports", "Baseline Transports per Day", "Hazard-Related Increase in Transports per Day",  "Please provide data")
    handle_ed_visits_section("ED Visits", "Baseline ED Visits per Day", "Hazard-Related Increase in ED Visits per Day",   "Please provide data")
    handle_ed_visits_section("Primary Care Office Visits", "Baseline Office Visits per Day", "Hazard-Related Increase in Office Visits per Day", "Please provide data")
    handle_ed_visits_section("Trauma Center Injuries", "Baseline Trauma Injuries per Day", "Hazard-Related Increase in Trauma Injuries per Day",   "Please provide data")
# Calculate and display Human Impact Score
    calculate_human_impact_score(AccExp_data)

    # Healthcare Service Impact Sections
    st.markdown("<h3 style='text-align: center;'>Healthcare Service Impact</h3>", unsafe_allow_html=True)
    handle_healthcare_section("Outpatient Services", "Baseline PCPs", "Hazard-Related Loss of PCPs", "Hazard-Related Increase in Demand for PCPs per Day (Increase in Office Visits / 20)")  
    handle_healthcare_section("ED Services", "Baseline ED Beds", "Hazard-Related Loss of ED Beds", "Hazard-Related Increase in Demand for ED Beds (ED Visits / 4.5)")
    handle_healthcare_section("Hospital Beds", "Baseline Hospital Beds", "Hazard-Related Loss of Hospital Beds", "Hazard-Related Increase in Demand for Hospital Beds")
    handle_healthcare_section("Ancillary Services", "Baseline Pharmacists", "Hazard-Related Loss of Pharmacists", "Hazard-Related Increase in Demand for Pharmacists")
    handle_healthcare_section("Trauma Units", "Baseline Trauma Center ORs", "Hazard-Related Loss of Trauma ORs", "Hazard-Related Increase in Demand for Trauma ORs")
    handle_healthcare_section("Mental Health Services", "Baseline Mental Health Providers", "Hazard-Related Loss of Mental Health Providers", "Hazard-Related Increase in Demand for Providers")
    calculate_healthcare_service_impact_score(AccExp_data)


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
    AccExp_increase = st.number_input(increase_label, value=0, key=f"{section_title}_AccExp_increase")
    
    # Calculate Magnitude Score
    magnitude_score = calculate_magnitude_score(baseline_value, AccExp_increase)
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
    # Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "AccExp_increase": AccExp_increase,
        "magnitude_score": magnitude_score
    })
    
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
    
    # Save final score
    save_data(f"{section_title}_final", {"final_score": final_score})
    # Display the final mortality score
    st.markdown(f"**Mortality Score:** {final_score}")
    
    


# New function to handle EMS Transports
def handle_ems_section(section_title, baseline_label, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)

    baseline_value = st.session_state.get(baseline_label, "Not Calculated")
    st.markdown(f"**{baseline_label}:** {baseline_value}")

    # Hazard-Related Increase (editable by user)
    AccExp_increase = st.number_input(increase_label, value=0, key=f"{section_title}_AccExp_increase")

    # Calculate Magnitude Score based on EMS Transports logic
    magnitude_score = calculate_magnitude_score(baseline_value, AccExp_increase)
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
    # Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "AccExp_increase": AccExp_increase,
        "magnitude_score": magnitude_score
    })

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

    # Save final score
    save_data(f"{section_title}_final", {"final_score": final_score})
    # Display the final EMS Transport score
    st.markdown(f"**{section_title} Score:** {final_score}")
    
    

# Function to handle ED Visits section 
def handle_ed_visits_section(section_title, baseline_label, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)
    
    baseline_value = st.session_state.get(baseline_label, "Not Calculated")
    st.markdown(f"**{baseline_label}:** {baseline_value}")

    # Hazard-Related Increase (editable by user)
    AccExp_increase = st.number_input(increase_label, value=0, key=f"{section_title}_AccExp_increase")

    # Calculate Magnitude Score based on ED Visits logic
    magnitude_score = calculate_magnitude_score(baseline_value, AccExp_increase)
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

    # # Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "AccExp_increase": AccExp_increase,
        "magnitude_score": magnitude_score
    })

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

    # Save final score
    save_data(f"{section_title}_final", {"final_score": final_score})

    # Display the final ED Visits score
    st.markdown(f"**{section_title} Score:** {final_score}")
    
def calculate_impact_score(scores):
    """
    Function to calculate the impact score based on individual component scores.
    If any score is "Not Calculated", return "Not Calculated".
    Otherwise, return the average of the scores.
    """
    valid_scores = [score for score in scores if score != "Not Calculated" and score != "NA"]
    
    if len(valid_scores) == len(scores):  # All scores are present and valid
        return sum(valid_scores) / len(valid_scores)
    else:
        return "Not Calculated"

def calculate_human_impact_score(AccExp_data):
    """
    Function to calculate Human Impact Score.
    """
    # Retrieve the final scores for each human impact section
    mortality_score = AccExp_data.get("Mortality_final", {}).get("final_score", "Not Calculated")
    ems_transports_score = AccExp_data.get("EMS Transports_final", {}).get("final_score", "Not Calculated")
    ed_visits_score = AccExp_data.get("ED Visits_final", {}).get("final_score", "Not Calculated")
    primary_care_office_visits_score = AccExp_data.get("Primary Care Office Visits_final", {}).get("final_score", "Not Calculated")
    trauma_center_injuries_score = AccExp_data.get("Trauma Center Injuries_final", {}).get("final_score", "Not Calculated")
    mental_health_score = AccExp_data.get("Mental Health_final", {}).get("final_score", "Not Calculated")

    # List of all human impact scores
    human_impact_scores = [
        mortality_score, ems_transports_score, ed_visits_score, 
        primary_care_office_visits_score, trauma_center_injuries_score, mental_health_score
    ]

    # Calculate the Human Impact Score
    human_impact_score = calculate_impact_score(human_impact_scores)
   # Save the Human Impact Score to AccExp_data.json
    AccExp_data["Human_Impact_Score"] = human_impact_score
    # Save back to the AccExp_data.json file
    save_data("Human Impact Score", {"final_score": human_impact_score})
    st.markdown(f"**Human Impact Score:** {human_impact_score}")
    return human_impact_score

#######################################################################
#healthcare service impact section 

def calculate_magnitude_score_healthcare(baseline, increase, loss):
    # Convert to float and handle potential non-numeric values
    try:
        baseline = float(baseline)
        increase = float(increase)
        loss = float(loss)
    except ValueError:
        return "Not calculated"

    if baseline == 0 or baseline == "Not Calculated":
        return "Not calculated"

    # Ensure (baseline - loss) is greater than zero to avoid division by zero
    if baseline - loss <= 0:
        return 4

    # Calculate the ratio
    ratio = (baseline + increase) / (baseline - loss)
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


def handle_healthcare_section(section_title, baseline_label, loss_label, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)
    
    # Fetch Baseline (prefilled from session and converted to float)
    baseline_value = st.session_state.get(baseline_label, "Not Calculated")
    st.markdown(f"**{baseline_label}:** {baseline_value}")

    # Hazard-Related Loss (editable by user)
    AccExp_loss_value = st.number_input(loss_label, value=0, key=f"{section_title}_AccExp_loss")

    # Logic for ED Services: Hazard-Related Increase = ED Visits / 4.5
    if section_title == "ED Services":
        AccExp_data = load_AccExp_data()  # Load data from ED Visits section
        AccExp_increase_visits = AccExp_data.get("ED Visits", {}).get("AccExp_increase", 0)
        AccExp_increase_value = AccExp_increase_visits / 4.5
        st.markdown(f"**{increase_label}:** {AccExp_increase_value}")

    # Logic for Outpatient Services: Hazard-Related Increase = Office Visits / 20
    elif section_title == "Outpatient Services":
        AccExp_data = load_AccExp_data()  # Load data from Primary Care Office Visits section
        AccExp_increase_visits = AccExp_data.get("Primary Care Office Visits", {}).get("AccExp_increase", 0)
        AccExp_increase_value = AccExp_increase_visits / 20
        st.markdown(f"**{increase_label}:** {AccExp_increase_value}")

    # Logic for Hospital Beds: Editable by user
    elif section_title == "Hospital Beds":
        # Hazard-Related Increase (editable by user)
        AccExp_increase_value = st.number_input(increase_label, value=0, key=f"{section_title}_AccExp_increase")

    # Logic for Anxillary Services: Editable by user
    elif section_title == "Ancillary Services":
        # Hazard-Related Increase (editable by user)
        AccExp_increase_value = st.number_input(increase_label, value=0, key=f"{section_title}_AccExp_increase")

    
    elif section_title == "Trauma Units":
        AccExp_data = load_AccExp_data()  # Load data from Primary Care Office Visits section
        AccExp_increase_visits = AccExp_data.get("Trauma Center Injuries", {}).get("AccExp_increase", 0)
        AccExp_increase_value = AccExp_increase_visits 
        st.markdown(f"**{increase_label}:** {AccExp_increase_value}")
    
    # Logic for Mental Health Services: Editable by user
    elif section_title == "Mental Health Services":
        # Hazard-Related Increase (editable by user)
        AccExp_increase_value = st.number_input(increase_label, value=0, key=f"{section_title}_AccExp_increase")

    else:
        AccExp_increase_value = 0

    # Calculate Magnitude Score
    magnitude_score = calculate_magnitude_score_healthcare(baseline_value, AccExp_increase_value, AccExp_loss_value)
    st.markdown(f"**Magnitude Score:** {magnitude_score}")
    st.markdown("""
        <ul>
            <li>0: No change from baseline</li>
            <li>1: (Baseline + ↑ demand) / (Baseline - ↓ supply) ≤ 1.05</li>
            <li>2: (Baseline + ↑ demand) / (Baseline - ↓ supply) ≤ 1.5</li>
            <li>3: (Baseline + ↑ demand) / (Baseline - ↓ supply) ≤ 2</li>
            <li>4: (Baseline + ↑ demand) / (Baseline - ↓ supply) > 2</li>
        </ul>
    """, unsafe_allow_html=True)

    # Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "AccExp_increase": AccExp_increase_value,
        "AccExp_loss_value": AccExp_loss_value,
        "magnitude_score": magnitude_score
    })

    # Qualitative Magnitude Score (user can select)
    qualitative_option = st.selectbox("OR, Estimate the Magnitude Qualitatively:", 
                                      ["Use Quantitative Value", "No change from baseline (Score = 0)", 
                                       "(Baseline + ↑ demand) / (Baseline - ↓ supply) ≤ 1.05 (Score = 1)", 
                                       "(Baseline + ↑ demand) / (Baseline - ↓ supply) ≤ 1.5 (Score = 2)", 
                                       "(Baseline + ↑ demand) / (Baseline - ↓ supply) ≤ 2 (Score = 3)", 
                                       "(Baseline + ↑ demand) / (Baseline - ↓ supply) > 2 (Score = 4)"], 
                                      index=0, key=f"{section_title}_qualitative")

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

    # Calculate final Score
    if qualitative_score is None and magnitude_score == "Not calculated":
        final_score = "Not Calculated/NA"
    elif qualitative_score is not None:
        final_score = (qualitative_score + duration_score) / 2
    else:
        final_score = (magnitude_score + duration_score) / 2

    # Save final score
    save_data(f"{section_title}_final", {"final_score": final_score})

    st.markdown(f"**{section_title} Score:** {final_score}")

def calculate_impact_score(scores):
    """
    Function to calculate the impact score based on individual component scores.
    If any score is "Not Calculated", return "Not Calculated".
    Otherwise, return the average of the scores.
    """
    valid_scores = [score for score in scores if score != "Not Calculated" and score != "NA"]
    
    if len(valid_scores) == len(scores):  # All scores are present and valid
        return sum(valid_scores) / len(valid_scores)
    else:
        return "Not Calculated"

def calculate_healthcare_service_impact_score(AccExp_data):
    """
    Function to calculate Healthcare Service Impact Score.
    """
    outpatient_score = AccExp_data.get("Outpatient Services_final", {}).get("final_score", "Not Calculated")
    ed_services_score = AccExp_data.get("ED Services_final", {}).get("final_score", "Not Calculated")
    hospital_beds_score = AccExp_data.get("Hospital Beds_final", {}).get("final_score", "Not Calculated")
    ancillary_services_score = AccExp_data.get("Ancillary Services_final", {}).get("final_score", "Not Calculated")
    trauma_units_score = AccExp_data.get("Trauma Units_final", {}).get("final_score", "Not Calculated")
    mental_health_score = AccExp_data.get("Mental Health Services_final", {}).get("final_score", "Not Calculated")

    # List of all healthcare scores
    healthcare_scores = [
        outpatient_score, ed_services_score, hospital_beds_score, 
        ancillary_services_score, trauma_units_score, mental_health_score
    ]

    # Calculate the Healthcare Service Impact Score
    healthcare_service_impact_score = calculate_impact_score(healthcare_scores)
    #save AccExp_data
    AccExp_data["Healthcare_Service_Impact_Score"] = healthcare_service_impact_score
    st.markdown(f"**Healthcare Service Impact Score:** {healthcare_service_impact_score}")
    return healthcare_service_impact_score



# Run the function to display the webpage
show()