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
    baseline_primary_care_office_visits = baseline_data.get("total_office_visits_per_day",0.0)
    baseline_trauma_center_injuries = baseline_data.get("total_trauma_injuries_per_day",0.0)
    ############################################################
    baseline_outpatient_services = baseline_data.get("total_pcps",0.0)
    baseline_ed_services = baseline_data.get("total_ed_beds",0.0)
    baseline_hospital_beds = baseline_data.get("hospital_beds_total",0.0)
    baseline_ancillary_service = baseline_data.get("total_pharmacists",0.0)
    baseline_trauma_center_or= baseline_data.get("total_trauma_units",0.0)
    baseline_mental_health_providers= baseline_data.get("total_mental_health_providers",0.0)
   
    ######################################################################################
    baseline_hospital_personnel=  baseline_data.get("rns_per_shift",0.0)
    baseline_patients_per_day= baseline_data.get("patients_per_day",0.0)
    baseline_patient_nurse_ratio= baseline_data.get("patient_to_nurse_ratio",0.0)
    baseline_facility_water_supply= baseline_data.get("inpatient_beds_total",0.0)
    baseline_facility_electricity= baseline_data.get("inpatient_beds_total",0.0)
    baseline_generator_fuel_supply= baseline_data.get("inpatient_beds_total",0.0)
    # baseline_hospital_it_comm_sys= baseline_data.get("")
    # baseline_smallest_no_of_hrs= baseline_data.get("",0.0)
    # baseline_critical_supplies=baseline_data.get("")
    # baseline_evacuation= baseline_data.get("")
    # baseline_hospital_patient_decontamination= baseline_data.get("")

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
        baseline_hospital_personnel= float(baseline_hospital_personnel) 
        baseline_patients_per_day= float(baseline_patients_per_day)
        baseline_patient_nurse_ratio= float(baseline_patient_nurse_ratio)
        baseline_facility_water_supply= float(baseline_facility_water_supply)
        baseline_facility_electricity= float( baseline_facility_electricity)
        # baseline_generator_fuel_supply= float(baseline_generator_fuel_supply)
        # baseline_smallest_no_of_hrs= float(baseline_smallest_no_of_hrs)
        # baseline_hospital_it_comm_sys=float(baseline_hospital_it_comm_sys)
        # baseline_critical_supplies=float(baseline_critical_supplies)
        # baseline_evacuation= float(baseline_evacuation)
        # baseline_hospital_patient_decontamination=float(baseline_hospital_patient_decontamination)  

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
        baseline_mental_health_providers= 0.0   
        baseline_hospital_personnel=0.0
        baseline_patients_per_day= 0.0
        baseline_patient_nurse_ratio= 0.0
        baseline_facility_water_supply= 0.0
        baseline_facility_electricity=0.0
        # baseline_generator_fuel_supply= 0.0
        # baseline_hospital_it_comm_sys=0.0
        # baseline_critical_supplies=0.0
        # baseline_evacuation= 0.0
        # baseline_hospital_patient_decontamination=0.0

        


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
    
    if "Baseline Hospital-Employed RNs per Shift" not in st.session_state:
        st.session_state["Baseline Hospital-Employed RNs per Shift"]= baseline_hospital_personnel

    if "Baseline Patients Per Day" not in st.session_state:
        st.session_state["Baseline Patients Per Day"]= baseline_patients_per_day
    if "Baseline Patient-to-Nurse Ratio" not in st.session_state:
        st.session_state["Baseline Patient-to-Nurse Ratio"] = baseline_patient_nurse_ratio
    if "Total Regional Inpatient Beds" not in st.session_state:
        st.session_state["Total Regional Inpatient Beds"]= baseline_facility_water_supply
    
    # if "Baseline Generator Fuel Supply" not in st.session_state:
    #     st.session_state["Baseline Generator Fuel Supply"]= baseline_generator_fuel_supply
    # if "Baseline Hospital IT/Communication Systems" not in st.session_state:
    #     st.session_state["Baseline Hospital IT/Communication Systems"] = baseline_hospital_it_comm_sys
    # if "Baseline Critical Supplies" not in st.session_state:
    #     st.session_state ["Baseline Critical Supplies"]= baseline_critical_supplies
    # if "Baseline Evacuation" not in st.session_state: 
    #     st.session_state["Baseline Evacuation"]= baseline_evacuation
    # if "Baseline Hospital Patient Decontamination" not in st.session_state:
    #     st.session_state ["Baseline Hospital Patient Decontamination"] = baseline_hospital_patient_decontamination
def show():
    # Prefill the form if data exists
    prefill_form()
    # Load hazard data from file
    hazard_data = load_hazard_data()

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
    save_data("probability_data", {"probability_score": probability_score})

    st.markdown("<h3 style='text-align: center;'>Human Impact</h3>", unsafe_allow_html=True)
    
    # Human Impact Sections
    handle_section("Mortality", "Baseline Mortality per Day", "Hazard-Related Increase in Mortality per Day",   "In the VA Tech Massacre of 2007, 33 died at the scene, including the shooter (Armstrong & Frykberg, 2007).")
    handle_ems_section("EMS Transports", "Baseline Transports per Day", "Hazard-Related Increase in Transports per Day",  "In the VA Tech Massacre of 2007, 17 were transported by EMS (Armstrong & Frykberg, 2007).")
    handle_ed_visits_section("ED Visits", "Baseline ED Visits per Day", "Hazard-Related Increase in ED Visits per Day",   "In the VA Tech Massacre of 2007, 27 were treated at local emergency departments (Virginia Tech Review Panel, 2007).")
    handle_ed_visits_section("Primary Care Office Visits", "Baseline Office Visits per Day", "Hazard-Related Increase in Office Visits per Day", "Please provide data")
    handle_ed_visits_section("Trauma Center Injuries", "Baseline Trauma Injuries per Day", "Hazard-Related Increase in Trauma Injuries per Day",   "In the VA Tech Massacre of 2007, 10 were taken to Level III trauma centers, and 2 to Level I centers (Armstrong & Frykberg, 2007).")
    handle_mental_health_section("Mental Health Impact", "Mental Health Impact (Percent of population developing psychopathology and behavioral changes after the incident, including PTST, depression, anxiety, alcohol and substance abuse, domestic violence, and loss of social functions)", "After the VA Tech Massacre of 2007, 15.4 percentage of students displayed PTSD symptoms (Hughes et al., 2011).")
    # Calculate and display Human Impact Score
    calculate_human_impact_score(hazard_data)

    # Healthcare Service Impact Sections
    st.markdown("<h3 style='text-align: center;'>Healthcare Service Impact</h3>", unsafe_allow_html=True)
    handle_healthcare_section("Outpatient Services", "Baseline PCPs", "Hazard-Related Loss of PCPs", "Hazard-Related Increase in Demand for PCPs per Day (Increase in Office Visits / 20)")  
    handle_healthcare_section("ED Services", "Baseline ED Beds", "Hazard-Related Loss of ED Beds", "Hazard-Related Increase in Demand for ED Beds (ED Visits / 4.5)")
    handle_healthcare_section("Hospital Beds", "Baseline Hospital Beds", "Hazard-Related Loss of Hospital Beds", "Hazard-Related Increase in Demand for Hospital Beds")
    handle_healthcare_section("Ancillary Services", "Baseline Pharmacists", "Hazard-Related Loss of Pharmacists", "Hazard-Related Increase in Demand for Pharmacists")
    handle_healthcare_section("Trauma Units", "Baseline Trauma Center ORs", "Hazard-Related Loss of Trauma ORs", "Hazard-Related Increase in Demand for Trauma ORs")
    handle_healthcare_section("Mental Health Services", "Baseline Mental Health Providers", "Hazard-Related Loss of Mental Health Providers", "Hazard-Related Increase in Demand for Providers")
    calculate_healthcare_service_impact_score(hazard_data)

    #Inpatient Healthcare Facility Infrastructure Impact	
    st.markdown("<h3 style='text-align: center;'>Inpatient Healthcare Facility Infrastructure Impact</h3>", unsafe_allow_html=True)
    handle_inpatient_section("Hospital Personnel", "Baseline Hospital-Employed RNs per Shift", "Hazard-Related Loss of RNs per Shift", "Baseline Patients Per Day","Hazard-Related Increase in Patients Per Day","Baseline Patient-to-Nurse Ratio","Hazard-Related Patient-to-Nurse Ratio","In the VA Tech Massacre of 2007, 27 were known to have been treated at local hospitals.")
    handle_water_section("Facility Water Supply","Number of Regional Inpatient Beds (Hospital and Nursing Home) Impacted by Water Loss", "Total Regional Inpatient Beds", "Percent of Regional Inpatient Beds Impacted","", "Data Source / Explanation", use_duration=False ) # Indicate no duration score is needed)
    handle_water_section("Facility Electricity", "Number of Regional Inpatient Beds(Hospital and Nursing Home) Impacted by Electricity Loss","Total Regional Inpatient Beds", "Percent of Regional Inpatient Beds Impacted","Hours of Electricity Loss", "Data Source" )
    # handle_inpatient_section("Facility Generator Fuel Supply", "Number of Regional Inpatient Beds (Hospital and Nursing Home) Requiring Additional Fuel Delivery for Back-Up Generators", "Total Regional Inpatient Beds","Percent of Regional Inpatient Beds Requiring Fuel","Smallest Number of Hours of Back-Up Generator Fuel On Hand in Facility","Hrs of Fuel Required","Fuel Supply Loss","Data Source")
    # handle_inpatient_section("Hospital IT/Communication Systems", "Number of Regional Hospital Beds Impacted by Data/Comm Loss","Total Regional Hospital Beds",  "Percent of Regional Hospital Beds Impacted","Enter data Source" )
    # handle_inpatient_section("Facility Critical Supplies", "Number of Regional Inpatient Beds (Hospital and Nursing Home) Impacted by Interruption of Linen Services", "Total Regional Inpatient Beds","Percent of Regional Inpatient Beds Impacted","Smallest Number of Days of Linens On Hand in Facility", "Days of Interruption of Linen Services", "Data source" )
    # handle_inpatient_section("Facility Evacuation", "Number of Regional Inpatient Beds Requiring Evacuation","Total Regional Inpatient Beds", "Percent of Regional Inpatient Beds Requiring Evacuation","Enter your data source")
    # handle_inpatient_section("Hospital Patient Decontamination", "Number of Patients Requiring Decontamination", "Decontamination Procedures","Data Source" )
		


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
    # Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "duration_score": duration_score,
        "hazard_increase": hazard_increase,
        "magnitude_score": magnitude_score
    })
    
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
# Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "duration_score": duration_score,
        "hazard_increase": hazard_increase,
        "magnitude_score": magnitude_score
    })

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
     # Save the baseline, increase, and magnitude score
    save_data(section_title, {
        "baseline": baseline_value,
        "hazard_increase": hazard_increase,
        "magnitude_score": magnitude_score
    })

    # Save final score
    save_data(f"{section_title}_final", {"final_score": final_score})

    # Display the final ED Visits score
    st.markdown(f"**{section_title} Score:** {final_score}")

#mental_health impact section handling 
def handle_mental_health_section(section_title, increase_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)

    # Mental Health Impact dropdown with options based on the image you provided
    magnitude_option = st.selectbox(
        increase_label,
        [
            "Minimal change in population behavior and negligible effects on social functioning.",
            "Effects weak or highly transient; occasional or minor loss of nonessential social functions in a circumscribed geographical area.",
            "Population displays distress with <25% psychopathology.",
            "Population displays distress with 25% - 49% psychopathology.",
            "Population displays distress with ≥ 50% psychopathology."
        ],
        index=4,  # Default to the last option (>= 50%)
        key=f"{section_title}_magnitude"
    )

    # Set Magnitude Score based on dropdown selection
    if magnitude_option == "Minimal change in population behavior and negligible effects on social functioning.":
        magnitude_score = 0
    elif magnitude_option == "Effects weak or highly transient; occasional or minor loss of nonessential social functions in a circumscribed geographical area.":
        magnitude_score = 1
    elif magnitude_option == "Population displays distress with <25% psychopathology.":
        magnitude_score = 2
    elif magnitude_option == "Population displays distress with 25% - 49% psychopathology.":
        magnitude_score = 3
    else:
        magnitude_score = 4

    st.markdown(f"**Magnitude Score:** {magnitude_score}")

    # Duration of Impact (user can select)
    duration_option = st.selectbox(
        "Duration of Impact:",
        ["No impact (Score = 0)", "≤ 1 day (Score = 1)", "≤ 1 week (Score = 2)", "≤ 2 weeks (Score = 3)", "> 2 weeks (Score = 4)"],
        index=2,  # Default to "≤ 1 week"
        key=f"{section_title}_duration"
    )

    # Calculate Duration Score
    duration_score = int(duration_option.split("Score = ")[-1][0])
    st.markdown(f"**Duration Score:** {duration_score}")
    # Data Source / Explanation (Optional)
    st.text_area("Data Source / Explanation (Optional):", default_explanation, key=f"{section_title}_explanation")

    # Calculate Mental Health Score
    if magnitude_score == "NA" or duration_score == "NA":
        final_score = "Not Calculated/NA"
    else:
        final_score = (magnitude_score + duration_score) / 2
    save_data(section_title, {
        "duration_score": duration_score,
        "magnitude_score": magnitude_score
    })
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
    #valid_scores = [score for score in scores if score != "Not Calculated" and score != "NA"]
    valid_scores = None if any( isinstance(score, (str)) for score in scores) else scores

    if len(valid_scores) == len(scores):  # All scores are present and valid
        return sum(valid_scores) / len(valid_scores)
    else:
        return "Not Calculated"

def calculate_human_impact_score(hazard_data):
    """
    Function to calculate Human Impact Score.
    """
    # Retrieve the final scores for each human impact section
    mortality_score = hazard_data.get("Mortality_final", {}).get("final_score", "Not Calculated")
    ems_transports_score = hazard_data.get("EMS Transports_final", {}).get("final_score", "Not Calculated")
    ed_visits_score = hazard_data.get("ED Visits_final", {}).get("final_score", "Not Calculated")
    primary_care_office_visits_score = hazard_data.get("Primary Care Office Visits_final", {}).get("final_score", "Not Calculated")
    trauma_center_injuries_score = hazard_data.get("Trauma Center Injuries_final", {}).get("final_score", "Not Calculated")
    mental_health_score = hazard_data.get("Mental Health Impact_final", {}).get("final_score", "Not Calculated")

    # List of all human impact scores
    human_impact_scores = [
        mortality_score, ems_transports_score, ed_visits_score, 
        primary_care_office_visits_score, trauma_center_injuries_score, mental_health_score
    ]

    # Calculate the Human Impact Score
    human_impact_score = calculate_impact_score(human_impact_scores)
   # Save the Human Impact Score to hazard_data.json
    hazard_data["Human_Impact_Score"] = human_impact_score
    # Save back to the hazard_data.json file
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
    hazard_loss_value = st.number_input(loss_label, value=0, key=f"{section_title}_hazard_loss")

    # Logic for ED Services: Hazard-Related Increase = ED Visits / 4.5
    if section_title == "ED Services":
        hazard_data = load_hazard_data()  # Load data from ED Visits section
        hazard_increase_visits = hazard_data.get("ED Visits", {}).get("hazard_increase", 0)
        hazard_increase_value = hazard_increase_visits / 4.5
        st.markdown(f"**{increase_label}:** {hazard_increase_value}")

    # Logic for Outpatient Services: Hazard-Related Increase = Office Visits / 20
    elif section_title == "Outpatient Services":
        hazard_data = load_hazard_data()  # Load data from Primary Care Office Visits section
        hazard_increase_visits = hazard_data.get("Primary Care Office Visits", {}).get("hazard_increase", 0)
        hazard_increase_value = hazard_increase_visits / 20
        st.markdown(f"**{increase_label}:** {hazard_increase_value}")

    # Logic for Hospital Beds: Editable by user
    elif section_title == "Hospital Beds":
        # Hazard-Related Increase (editable by user)
        hazard_increase_value = st.number_input(increase_label, value=0, key=f"{section_title}_hazard_increase")

    # Logic for Anxillary Services: Editable by user
    elif section_title == "Ancillary Services":
        # Hazard-Related Increase (editable by user)
        hazard_increase_value = st.number_input(increase_label, value=0, key=f"{section_title}_hazard_increase")

    
    elif section_title == "Trauma Units":
        hazard_data = load_hazard_data()  # Load data from Primary Care Office Visits section
        hazard_increase_visits = hazard_data.get("Trauma Center Injuries", {}).get("hazard_increase", 0)
        hazard_increase_value = hazard_increase_visits 
        st.markdown(f"**{increase_label}:** {hazard_increase_value}")
    
    # Logic for Mental Health Services: Editable by user
    elif section_title == "Mental Health Services":
        # Hazard-Related Increase (editable by user)
        hazard_increase_value = st.number_input(increase_label, value=0, key=f"{section_title}_hazard_increase")

    else:
        hazard_increase_value = 0

    # Calculate Magnitude Score
    magnitude_score = calculate_magnitude_score_healthcare(baseline_value, hazard_increase_value, hazard_loss_value)
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
        "hazard_increase": hazard_increase_value,
        "hazard_loss_value": hazard_loss_value,
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
    # valid_scores =  [float(score) for score in scores if score != "Not Calculated" and score != "NA"]
    
    valid_scores = None if any( isinstance(score, (str)) for score in scores) else scores
    
    if valid_scores != None:  # All scores are present and valid
        return sum(valid_scores) / len(valid_scores)

    else:
        return "Not Calculated"

def calculate_healthcare_service_impact_score(hazard_data):
    """
    Function to calculate Healthcare Service Impact Score.
    """
    outpatient_score = hazard_data.get("Outpatient Services_final", {}).get("final_score", "Not Calculated")
    ed_services_score = hazard_data.get("ED Services_final", {}).get("final_score", "Not Calculated")
    hospital_beds_score = hazard_data.get("Hospital Beds_final", {}).get("final_score", "Not Calculated")
    ancillary_services_score = hazard_data.get("Ancillary Services_final", {}).get("final_score", "Not Calculated")
    trauma_units_score = hazard_data.get("Trauma Units_final", {}).get("final_score", "Not Calculated")
    mental_health_score = hazard_data.get("Mental Health Services_final", {}).get("final_score", "Not Calculated")

    # List of all healthcare scores
    healthcare_scores = [
        outpatient_score, ed_services_score, hospital_beds_score, 
        ancillary_services_score, trauma_units_score, mental_health_score
    ]

    # Calculate the Healthcare Service Impact Score
    healthcare_service_impact_score = calculate_impact_score(healthcare_scores)
    #save hazard_data
    hazard_data["Healthcare_Service_Impact_Score"] = healthcare_service_impact_score
    st.markdown(f"**Healthcare Service Impact Score:** {healthcare_service_impact_score}")
    return healthcare_service_impact_score

###################################################################################################################

# Helper function to check if a value is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

# Function to handle the Inpatient Healthcare Facility Infrastructure Impact
def handle_inpatient_section(section_title, baseline_rn_label, loss_label, patients_label, increase_label, ratio_label, hazard_ratio_label, default_explanation=""):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)
    hazard_data = load_hazard_data()
    # Load baseline data
    baseline_rns = st.session_state.get(baseline_rn_label, "Not Calculated")
    st.markdown(f"**{baseline_rn_label}:** {baseline_rns}")

 # Hazard-Related Loss of RNs per Shift (editable by user)
    hazard_loss_rns = st.number_input(loss_label, value=0.0, key=f"{section_title}_hazard_loss")

    baseline_patients = st.session_state.get(patients_label, "Not Calculated")
    st.markdown(f"**{patients_label}:** {baseline_patients}")
    # Hazard-Related Increase in Patients Per Day (from hazard_data.json)
    hazard_increase_patients = hazard_data.get("Hospital Beds", {}).get("hazard_loss_value", 0)
    st.markdown(f"**{increase_label}:** {hazard_increase_patients}")

    baseline_ratio = st.session_state.get(ratio_label, "Not Calculated")
    st.markdown(f"**{ratio_label}:** {baseline_ratio}")

   
    
    # Calculate Hazard-Related Patient-to-Nurse Ratio
    if not is_numeric(baseline_rns) or not is_numeric(hazard_loss_rns):
        hazard_patient_nurse_ratio = "Not Calculated"
    elif baseline_rns - hazard_loss_rns == 0:
        hazard_patient_nurse_ratio = "No Nurses"
    else:
        if is_numeric(baseline_patients) and is_numeric(hazard_increase_patients):
            baseline_rns = float(baseline_rns)
            hazard_loss_rns = float(hazard_loss_rns)
            baseline_patients = float(baseline_patients)
            hazard_increase_patients = float(hazard_increase_patients)
            hazard_patient_nurse_ratio = (baseline_patients + hazard_increase_patients) / (baseline_rns - hazard_loss_rns)
        else:
            hazard_patient_nurse_ratio = "Not Calculated"

    st.markdown(f"**{hazard_ratio_label}:** {hazard_patient_nurse_ratio}")

    # Magnitude Score Calculation
    if not is_numeric(baseline_ratio) or baseline_ratio == 0:
        magnitude_score = "Not Calculated"
    elif hazard_patient_nurse_ratio == "No Nurses":
        magnitude_score = 4
    elif hazard_patient_nurse_ratio == "Not Calculated":
        magnitude_score = 0
    elif hazard_patient_nurse_ratio / baseline_ratio <= 1:
        magnitude_score = 0
    elif hazard_patient_nurse_ratio / baseline_ratio <= 1.1:
        magnitude_score = 1
    elif hazard_patient_nurse_ratio / baseline_ratio <= 1.25:
        magnitude_score = 2
    elif hazard_patient_nurse_ratio / baseline_ratio <= 1.5:
        magnitude_score = 3
    else:
        magnitude_score = 4

    st.markdown(f"**Magnitude Score:** {magnitude_score}")
    st.markdown("""
        <ul>
            <li>0: Patient-to-Nurse Ratio = Baseline</li>
            <li>1: Patient-to-Nurse Ratio ↑ ≤ 10%</li>
            <li>2: Patient-to-Nurse Ratio ↑ ≤ 25%</li>
            <li>3: Patient-to-Nurse Ratio ↑ ≤ 50%</li>
            <li>4: Patient-to-Nurse Ratio ↑ > 50%</li>
        </ul>
    """, unsafe_allow_html=True)

    # Qualitative Magnitude Score (user can select)
    qualitative_option = st.selectbox("OR, Estimate the Magnitude Qualitatively:", 
                                      ["Use Quantitative Value", "No change from baseline (Score = 0)", 
                                       "Ratio increased ≤ 10% (Score = 1)", "Ratio increased ≤ 25% (Score = 2)", 
                                       "Ratio increased ≤ 50% (Score = 3)", "Ratio increased > 50% (Score = 4)"], 
                                      index=0, key=f"{section_title}_qualitative")

    # Extract qualitative score if applicable
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

    # Final Hospital Personnel Score Calculation
    if qualitative_score is None and magnitude_score == "Not Calculated":
        final_score = "Not Calculated/NA"
    elif qualitative_score is not None:
        final_score = (qualitative_score + duration_score) / 2
    else:
        final_score = (magnitude_score + duration_score) / 2

    st.markdown(f"**{section_title} Score:** {final_score}")

    # Save the data
    save_data(section_title, {
        "baseline_rns": baseline_rns,
        "hazard_loss_rns": hazard_loss_rns,
        "hazard_increase_patients": hazard_increase_patients,
        "hazard_patient_nurse_ratio": hazard_patient_nurse_ratio,
        "magnitude_score": magnitude_score,
        "duration_score": duration_score,
        "final_score": final_score
    })

def handle_water_section(section_title, beds_impacted_label, total_beds_label, percent_impacted_label, duration_label, default_explanation="", use_duration=True):
    st.markdown(f"<h4>{section_title}</h4>", unsafe_allow_html=True)

    # Load Total Regional Inpatient Beds from baseline_data.json
    total_beds = st.session_state.get(total_beds_label, "Not Calculated")
    st.markdown(f"**{total_beds_label}:** {total_beds}")

    # Number of Regional Inpatient Beds Impacted by Loss (Editable by user)
    beds_impacted = st.number_input(beds_impacted_label, value=0, key=f"{section_title}_beds_impacted")

    # Calculate Percent of Regional Inpatient Beds Impacted
    if not is_numeric(total_beds) or float(total_beds) == 0:
        percent_impacted = "Not Calculated"
    else:
        percent_impacted = (beds_impacted / float(total_beds)) * 100 if is_numeric(beds_impacted) else "Not Calculated"

    st.markdown(f"**{percent_impacted_label}:** {percent_impacted}")

    # Magnitude Score Calculation
    if percent_impacted == "Not Calculated" or percent_impacted <= 0:
        magnitude_score = 0
    elif percent_impacted <= 1:
        magnitude_score = 1
    elif percent_impacted <= 5:
        magnitude_score = 2
    elif percent_impacted <= 10:
        magnitude_score = 3
    else:
        magnitude_score = 4

    st.markdown(f"**Magnitude Score:** {magnitude_score}")

    # Duration Score Calculation, if applicable
    if use_duration:
        duration_value = st.number_input(duration_label, value=0, key=f"{section_title}_duration_value")
        if duration_value <= 0:
            duration_score = 0
        elif duration_value <= 2:
            duration_score = 1
        elif duration_value <= 6:
            duration_score = 2
        elif duration_value <= 12:
            duration_score = 3
        else:
            duration_score = 4
        st.markdown(f"**Duration Score:** {duration_score}")
    else:
        duration_score = 0  # Default to 0 if duration not applicable

    # Data Source / Explanation (Optional)
    st.text_area("Data Source / Explanation (Optional):", default_explanation, key=f"{section_title}_explanation")

    # Final Facility Score Calculation
    final_score = (magnitude_score + duration_score) / 2
    st.markdown(f"**{section_title} Score:** {final_score}")

    # Save the data
    save_data(section_title, {
        "beds_impacted": beds_impacted,
        "total_beds": total_beds,
        "percent_impacted": percent_impacted,
        "magnitude_score": magnitude_score,
        "duration_score": duration_score,
        "final_score": final_score
    })

# Run the function to display the webpage
show()
