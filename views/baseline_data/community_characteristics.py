import streamlit as st
import json
import os

# Path to your JSON file
json_file_path = 'form_data.json'

# Function to save data to a JSON file
def save_data(data):
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Function to load data from a JSON file
def load_data():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        return {}

# Function to handle form submission
def handle_form_submission():
    # Collect all form data
    form_data = {
        "Total Population": st.session_state.total_population,
        "Total Housing Units": st.session_state.total_housing_units,
        "Percent Using Well Water": st.session_state.percent_using_well_water,
        "Percent Under Age 40": st.session_state.percent_under_age_40,
        "Largest City or Population Center": st.session_state.largest_city,
        "Population of Largest City or Population Center": st.session_state.population_of_largest_city,
        "Population Density of Largest City (per sq mile)": st.session_state.population_density_of_largest_city,
        "Largest Hospital": st.session_state.largest_hospital,
        "ED Beds at Largest Hospital": st.session_state.ed_beds_largest_hospital,
        "Total Beds at Largest Hospital": st.session_state.total_beds_largest_hospital,
        "If Largest Hospital is a Trauma Center, Number of ORs": st.session_state.ors_largest_hospital,
        "Another Hospital (Hospital 2)": st.session_state.hospital_2,
        "ED Beds at Hospital 2": st.session_state.ed_beds_hospital_2,
        "Total Beds at Hospital 2": st.session_state.total_beds_hospital_2,
        "If Hospital 2 is a Trauma Center, Number of ORs": st.session_state.ors_hospital_2,
        "Region falls within 50-mile radius of nuclear reactor": st.session_state.within_50_miles_nuclear,
        "Major transportation routes within 10 miles of nuclear reactor": st.session_state.transportation_routes_within_10_miles,
        "Percent of region's businesses within 10 miles of nuclear reactor": st.session_state.businesses_within_10_miles,
        "Population within 10 Miles of a Nuclear Reactor": st.session_state.population_within_10_miles,
        "Hospitals Within 10 Miles of a Nuclear Reactor": st.session_state.hospitals_within_10_miles,
        "Total ED Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor": st.session_state.ed_beds_within_10_miles,
        "Total Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor": st.session_state.total_beds_within_10_miles,
        "FTE Nurses Employed at Hospital(s) Within 10 Miles of a Nuclear Reactor": st.session_state.fte_nurses_within_10_miles,
        "If Hospitals Within 10 Miles of Nuclear Reactor is a Trauma Center, Number of ORs": st.session_state.ors_within_10_miles,
        "Nursing Homes Within 10 Miles of a Nuclear Reactor": st.session_state.nursing_homes_within_10_miles,
        "Total Beds at Nursing Homes Within 10 Miles of a Nuclear Reactor": st.session_state.total_beds_nursing_homes_within_10_miles,
        "PCPs Within 10 Miles of a Nuclear Reactor": st.session_state.pcps_within_10_miles,
        "Pharmacists Within 10 Miles of a Nuclear Reactor": st.session_state.pharmacists_within_10_miles,
        "Mental Health Professionals Within 10 Miles of a Nuclear Reactor": st.session_state.mental_health_professionals_within_10_miles,
        "Morgue Units Located Within 10 Miles of a Nuclear Reactor": st.session_state.morgue_units_within_10_miles,
        "Large College Campus": st.session_state.large_college_campus,
        "Population Living on Large College Campus": st.session_state.population_living_on_campus,
        "Large public building or space target for terrorist attack": st.session_state.terrorist_target,
        "People occupy building/space at its busiest time": st.session_state.people_occupy_space,
        "Residential Population density of surrounding area": st.session_state.residential_population_density,
        "Daytime Population density of surrounding area": st.session_state.daytime_population_density,
    }
    save_data(form_data)
    st.success("Form data saved successfully!")

# Function to prefill form data
def prefill_form():
    form_data = load_data()
    for key, value in form_data.items():
        st.session_state[key.replace(" ", "_").lower()] = value

def show():
    # Initialize session state
    for key in ["total_population", "total_housing_units", "percent_using_well_water", "percent_under_age_40", "largest_city", "population_of_largest_city", "population_density_of_largest_city", "largest_hospital", "ed_beds_largest_hospital", "total_beds_largest_hospital", "ors_largest_hospital", "hospital_2", "ed_beds_hospital_2", "total_beds_hospital_2", "ors_hospital_2", "within_50_miles_nuclear", "transportation_routes_within_10_miles", "businesses_within_10_miles", "population_within_10_miles", "hospitals_within_10_miles", "ed_beds_within_10_miles", "total_beds_within_10_miles", "fte_nurses_within_10_miles", "ors_within_10_miles", "nursing_homes_within_10_miles", "total_beds_nursing_homes_within_10_miles", "pcps_within_10_miles", "pharmacists_within_10_miles", "mental_health_professionals_within_10_miles", "morgue_units_within_10_miles", "large_college_campus", "population_living_on_campus", "terrorist_target", "people_occupy_space", "residential_population_density", "daytime_population_density"]:
        if key not in st.session_state:
            st.session_state[key] = ""
    
    # Prefill data if it exists
    prefill_form()

    #st.markdown("<h2 class='header'>Community Characteristics</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p class='subheader'>The following information will be used to develop hazard scenarios and estimate the impacts of various hazards on the jurisdiction.</p>

    <div class="input-container">
        <label class="label">Total Population:</label>
        <input class="text-input" type="number" placeholder="Enter total population" value="0">
    </div>
    <div class="input-container">
        <label class="label">Total Housing Units:</label>
        <input class="text-input" type="number" placeholder="Enter total housing units">
    </div>
    <div class="input-container">
        <label class="label">Percent Using Well Water:</label>
        <input class="text-input" type="number" placeholder="Enter percentage using well water">
    </div>
    <div class="input-container">
        <label class="label">Percent Under Age 40:</label>
        <input class="text-input" type="number" placeholder="Enter percentage under age 40">
    </div>
    <div class="input-container">
        <label class="label">Largest City or Population Center:</label>
        <input class="text-input" type="text" placeholder="Enter largest city or population center">
    </div>
    <div class="input-container">
        <label class="label">Population of Largest City or Population Center:</label>
        <input class="text-input" type="number" placeholder="Enter population of largest city or population center">
    </div>
    <div class="input-container">
        <label class="label">Population Density of Largest City (per sq mile):</label>
        <input class="text-input" type="number" placeholder="Enter population density of largest city">
    </div>
    <div class="input-container">
        <label class="label">Largest Hospital:</label>
        <input class="text-input" type="text" placeholder="Enter name of largest hospital">
    </div>
    <div class="input-container">
        <label class="label">ED Beds at Largest Hospital:</label>
        <input class="text-input" type="number" placeholder="Enter number of ED beds at largest hospital">
    </div>
    <div class="input-container">
        <label class="label">Total Beds at Largest Hospital:</label>
        <input class="text-input" type="number" placeholder="Enter total beds at largest hospital">
    </div>
    <div class="input-container">
        <label class="label">If Largest Hospital is a Trauma Center, Number of ORs (otherwise, 0):</label>
        <input class="text-input" type="number" placeholder="Enter number of ORs if largest hospital is a trauma center">
    </div>
    <div class="input-container">
        <label class="label">Another Hospital (Hospital 2):</label>
        <input class="text-input" type="text" placeholder="Enter name of another hospital">
    </div>
    <div class="input-container">
        <label class="label">ED Beds at Hospital 2:</label>
        <input class="text-input" type="number" placeholder="Enter number of ED beds at hospital 2">
    </div>
    <div class="input-container">
        <label class="label">Total Beds at Hospital 2:</label>
        <input class="text-input" type="number" placeholder="Enter total beds at hospital 2">
    </div>
    <div class="input-container">
        <label class="label">If Hospital 2 is a Trauma Center, Number of ORs (otherwise, 0):</label>
        <input class="text-input" type="number" placeholder="Enter number of ORs if hospital 2 is a trauma center">
    </div>
    <div class="input-container">
        <label class="label">Does any part of the region fall within a 50-mile radius of a nuclear reactor?</label>
        <input class="text-input" type="text" placeholder="Enter Yes or No">
    </div>
    <div class="input-container">
        <label class="label">Are there major transportation routes in the region within 10 miles of a nuclear reactor?</label>
        <input class="text-input" type="text" placeholder="Enter Yes or No">
    </div>
    <div class="input-container">
        <label class="label">Percent of region's businesses located within 10 miles of a nuclear reactor:</label>
        <input class="text-input" type="number" placeholder="Enter percentage">
    </div>
    <div class="input-container">
        <label class="label">Population within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter population within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="text" placeholder="Enter number of hospitals within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">Total ED Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of ED beds within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">ED Beds per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
        <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
    </div>
    <div class="input-container">
        <label class="label">Total Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of total beds within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">Beds per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
        <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
    </div>
    <div class="input-container">
        <label class="label">FTE Nurses Employed at Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of FTE nurses within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">If Hospital(s) Within 10 Miles of a Nuclear Reactor is a Trauma Center, Number of ORs (otherwise, 0):</label>
        <input class="text-input" type="number" placeholder="Enter number of ORs if hospital within 10 miles is a trauma center">
    </div>
    <div class="input-container">
        <label class="label">Nursing Home(s) Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of nursing homes within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">Total Beds at Nursing Home(s) Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of total beds in nursing homes within 10 miles">
    </div>
    <div class="input-container">
        <label class="label">PCPs Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of PCPs within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">PCPs per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
        <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
    </div>
    <div class="input-container">
        <label class="label">Pharmacists Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of pharmacists within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">Pharmacists per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
        <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
    </div>
    <div class="input-container">
        <label class="label">Mental Health Professionals Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of mental health professionals within 10 miles">
    </div>
    <div class="input-container">
        <label class="label">Mental Health Professionals per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
        <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
    </div>
    <div class="input-container">
        <label class="label">Morgue Units Located Within 10 Miles of a Nuclear Reactor:</label>
        <input class="text-input" type="number" placeholder="Enter number of morgue units within 10 miles of a nuclear reactor">
    </div>
    <div class="input-container">
        <label class="label">Large College Campus:</label>
        <input class="text-input" type="text" placeholder="Enter name of large college campus">
    </div>
    <div class="input-container">
        <label class="label">Population Living on Large College Campus:</label>
        <input class="text-input" type="number" placeholder="Enter population living on large college campus">
    </div>
    <div class="input-container">
        <label class="label">What is a large public building or space that could be the target for a terrorist attack?</label>
        <input class="text-input" type="text" placeholder="Enter name of large public building or space">
    </div>
    <div class="input-container">
        <label class="label">How many people occupy this building/space at its busiest time?</label>
        <input class="text-input" type="number" placeholder="Enter number of people">
    </div>
    <div class="input-container">
        <label class="label"> Residental Population density of surrounding area (per square mile):</label>
        <input class="text-input" type="number" placeholder="Enter number of people">
    </div>
    <div class="input-container">
        <label class="label">Daytime Population density of surrounding area (per square mile):  </label>
        <input class="text-input" type="number" placeholder="Enter number of people">
    </div>              
    
    """, unsafe_allow_html=True)



    # Button to submit and save form data
    if st.button("Save Data"):
        handle_form_submission()

show()















# import streamlit as st

# def show():
#     # Define CSS style for improved visuals
#     st.markdown("""
#     <style>
#         body {
#             background-color: #f5f5f5;
#         }
#         .main {
#             background-color: #e6e6fa;
#             padding: 20px;
#             border-radius: 10px;
#         }
#         .input-container {
#             background-color: #ffe4e1;
#             padding: 20px;
#             border-radius: 10px;
#             margin: 10px 0;
#         }
#         .header {
#             text-align: center;
#             color: #333333;
#             font-size: 24px;
#             margin-top: 10px;
#         }
#         .subheader {
#             color: #333333;
#             font-size: 18px;
#             margin-top: 10px;
#         }
#         .label {
#             font-weight: bold;
#         }
#         .text-input {
#             width: 100%;
#             padding: 10px;
#             margin: 5px 0;
#             border-radius: 5px;
#             border: 1px solid #cccccc;
#         }
#         .text-output {
#             width: 100%;
#             padding: 10px;
#             margin: 5px 0;
#             border-radius: 5px;
#             border: 1px solid #cccccc;
#             background-color: #f5f5f5;
#             color: #333333;
#         }
#         .row {
#             display: flex;
#             flex-wrap: wrap;
#             justify-content: space-between;
#         }
#         .column {
#             flex: 0 0 48%;
#             box-sizing: border-box;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     #st.markdown("<h2 class='header'>Community Characteristics</h2>", unsafe_allow_html=True)
#     st.markdown("""
#     <p class='subheader'>The following information will be used to develop hazard scenarios and estimate the impacts of various hazards on the jurisdiction.</p>

#     <div class="input-container">
#         <label class="label">Total Population:</label>
#         <input class="text-input" type="number" placeholder="Enter total population" value="0">
#     </div>
#     <div class="input-container">
#         <label class="label">Total Housing Units:</label>
#         <input class="text-input" type="number" placeholder="Enter total housing units">
#     </div>
#     <div class="input-container">
#         <label class="label">Percent Using Well Water:</label>
#         <input class="text-input" type="number" placeholder="Enter percentage using well water">
#     </div>
#     <div class="input-container">
#         <label class="label">Percent Under Age 40:</label>
#         <input class="text-input" type="number" placeholder="Enter percentage under age 40">
#     </div>
#     <div class="input-container">
#         <label class="label">Largest City or Population Center:</label>
#         <input class="text-input" type="text" placeholder="Enter largest city or population center">
#     </div>
#     <div class="input-container">
#         <label class="label">Population of Largest City or Population Center:</label>
#         <input class="text-input" type="number" placeholder="Enter population of largest city or population center">
#     </div>
#     <div class="input-container">
#         <label class="label">Population Density of Largest City (per sq mile):</label>
#         <input class="text-input" type="number" placeholder="Enter population density of largest city">
#     </div>
#     <div class="input-container">
#         <label class="label">Largest Hospital:</label>
#         <input class="text-input" type="text" placeholder="Enter name of largest hospital">
#     </div>
#     <div class="input-container">
#         <label class="label">ED Beds at Largest Hospital:</label>
#         <input class="text-input" type="number" placeholder="Enter number of ED beds at largest hospital">
#     </div>
#     <div class="input-container">
#         <label class="label">Total Beds at Largest Hospital:</label>
#         <input class="text-input" type="number" placeholder="Enter total beds at largest hospital">
#     </div>
#     <div class="input-container">
#         <label class="label">If Largest Hospital is a Trauma Center, Number of ORs (otherwise, 0):</label>
#         <input class="text-input" type="number" placeholder="Enter number of ORs if largest hospital is a trauma center">
#     </div>
#     <div class="input-container">
#         <label class="label">Another Hospital (Hospital 2):</label>
#         <input class="text-input" type="text" placeholder="Enter name of another hospital">
#     </div>
#     <div class="input-container">
#         <label class="label">ED Beds at Hospital 2:</label>
#         <input class="text-input" type="number" placeholder="Enter number of ED beds at hospital 2">
#     </div>
#     <div class="input-container">
#         <label class="label">Total Beds at Hospital 2:</label>
#         <input class="text-input" type="number" placeholder="Enter total beds at hospital 2">
#     </div>
#     <div class="input-container">
#         <label class="label">If Hospital 2 is a Trauma Center, Number of ORs (otherwise, 0):</label>
#         <input class="text-input" type="number" placeholder="Enter number of ORs if hospital 2 is a trauma center">
#     </div>
#     <div class="input-container">
#         <label class="label">Does any part of the region fall within a 50-mile radius of a nuclear reactor?</label>
#         <input class="text-input" type="text" placeholder="Enter Yes or No">
#     </div>
#     <div class="input-container">
#         <label class="label">Are there major transportation routes in the region within 10 miles of a nuclear reactor?</label>
#         <input class="text-input" type="text" placeholder="Enter Yes or No">
#     </div>
#     <div class="input-container">
#         <label class="label">Percent of region's businesses located within 10 miles of a nuclear reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter percentage">
#     </div>
#     <div class="input-container">
#         <label class="label">Population within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter population within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="text" placeholder="Enter number of hospitals within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">Total ED Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of ED beds within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">ED Beds per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
#         <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
#     </div>
#     <div class="input-container">
#         <label class="label">Total Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of total beds within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">Beds per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
#         <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
#     </div>
#     <div class="input-container">
#         <label class="label">FTE Nurses Employed at Hospital(s) Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of FTE nurses within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">If Hospital(s) Within 10 Miles of a Nuclear Reactor is a Trauma Center, Number of ORs (otherwise, 0):</label>
#         <input class="text-input" type="number" placeholder="Enter number of ORs if hospital within 10 miles is a trauma center">
#     </div>
#     <div class="input-container">
#         <label class="label">Nursing Home(s) Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of nursing homes within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">Total Beds at Nursing Home(s) Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of total beds in nursing homes within 10 miles">
#     </div>
#     <div class="input-container">
#         <label class="label">PCPs Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of PCPs within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">PCPs per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
#         <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
#     </div>
#     <div class="input-container">
#         <label class="label">Pharmacists Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of pharmacists within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">Pharmacists per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
#         <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
#     </div>
#     <div class="input-container">
#         <label class="label">Mental Health Professionals Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of mental health professionals within 10 miles">
#     </div>
#     <div class="input-container">
#         <label class="label">Mental Health Professionals per 100,000 Within 10 Miles of a Nuclear Reactor:</label>
#         <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
#     </div>
#     <div class="input-container">
#         <label class="label">Morgue Units Located Within 10 Miles of a Nuclear Reactor:</label>
#         <input class="text-input" type="number" placeholder="Enter number of morgue units within 10 miles of a nuclear reactor">
#     </div>
#     <div class="input-container">
#         <label class="label">Large College Campus:</label>
#         <input class="text-input" type="text" placeholder="Enter name of large college campus">
#     </div>
#     <div class="input-container">
#         <label class="label">Population Living on Large College Campus:</label>
#         <input class="text-input" type="number" placeholder="Enter population living on large college campus">
#     </div>
#     <div class="input-container">
#         <label class="label">What is a large public building or space that could be the target for a terrorist attack?</label>
#         <input class="text-input" type="text" placeholder="Enter name of large public building or space">
#     </div>
#     <div class="input-container">
#         <label class="label">How many people occupy this building/space at its busiest time?</label>
#         <input class="text-input" type="number" placeholder="Enter number of people">
#     </div>
#     <div class="input-container">
#         <label class="label"> Residental Population density of surrounding area (per square mile):</label>
#         <input class="text-input" type="number" placeholder="Enter number of people">
#     </div>
#     <div class="input-container">
#         <label class="label">Daytime Population density of surrounding area (per square mile):  </label>
#         <input class="text-input" type="number" placeholder="Enter number of people">
#     </div>              
    
#     """, unsafe_allow_html=True)

# show(