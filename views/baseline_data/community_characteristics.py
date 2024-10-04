import streamlit as st
import json
import os

# Path to the JSON file
json_file_path = 'baseline_data.json'

# Function to save data to a JSON file
def save_data(data, key):
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    else:
        existing_data = {}

    # Save form data under the provided key
    existing_data[key] = data

    # Write updated data back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

# Function to load data from a JSON file
def load_data(key):
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            return data.get(key, {})
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

    save_data(form_data, key="community_characteristics")
    st.success("Form data saved successfully!")

# Function to prefill form data
def prefill_form():
    form_data = load_data("community_characteristics")
    for key, value in form_data.items():
        st.session_state[key.replace(" ", "_").lower()] = value

def show():
    # Initialize session state
    for key in ["total_population", "total_housing_units", "percent_using_well_water", "percent_under_age_40", "largest_city", "population_of_largest_city", "population_density_of_largest_city", "largest_hospital", "ed_beds_largest_hospital", "total_beds_largest_hospital", "ors_largest_hospital", "hospital_2", "ed_beds_hospital_2", "total_beds_hospital_2", "ors_hospital_2", "within_50_miles_nuclear", "transportation_routes_within_10_miles", "businesses_within_10_miles", "population_within_10_miles", "hospitals_within_10_miles", "ed_beds_within_10_miles", "total_beds_within_10_miles", "fte_nurses_within_10_miles", "ors_within_10_miles", "nursing_homes_within_10_miles", "total_beds_nursing_homes_within_10_miles", "pcps_within_10_miles", "pharmacists_within_10_miles", "mental_health_professionals_within_10_miles", "morgue_units_within_10_miles", "large_college_campus", "population_living_on_campus", "terrorist_target", "people_occupy_space", "residential_population_density", "daytime_population_density"]:
        if key not in st.session_state:
            st.session_state[key] = ""
    
    # Prefill data if it exists
    prefill_form()

    st.markdown("<h2 class='header'>Community Characteristics</h2>", unsafe_allow_html=True)

    # Add input fields
    st.text_input("Total Population", key="total_population")
    st.text_input("Total Housing Units", key="total_housing_units")
    st.text_input("Percent Using Well Water", key="percent_using_well_water")
    st.text_input("Percent Under Age 40", key="percent_under_age_40")
    st.text_input("Largest City or Population Center", key="largest_city")
    st.text_input("Population of Largest City or Population Center", key="population_of_largest_city")
    st.text_input("Population Density of Largest City (per sq mile)", key="population_density_of_largest_city")
    st.text_input("Largest Hospital", key="largest_hospital")
    st.text_input("ED Beds at Largest Hospital", key="ed_beds_largest_hospital")
    st.text_input("Total Beds at Largest Hospital", key="total_beds_largest_hospital")
    st.text_input("If Largest Hospital is a Trauma Center, Number of ORs", key="ors_largest_hospital")
    st.text_input("Another Hospital (Hospital 2)", key="hospital_2")
    st.text_input("ED Beds at Hospital 2", key="ed_beds_hospital_2")
    st.text_input("Total Beds at Hospital 2", key="total_beds_hospital_2")
    st.text_input("If Hospital 2 is a Trauma Center, Number of ORs", key="ors_hospital_2")
    st.text_input("Region falls within 50-mile radius of nuclear reactor", key="within_50_miles_nuclear")
    st.text_input("Major transportation routes within 10 miles of nuclear reactor", key="transportation_routes_within_10_miles")
    st.text_input("Percent of region's businesses within 10 miles of nuclear reactor", key="businesses_within_10_miles")
    st.text_input("Population within 10 Miles of a Nuclear Reactor", key="population_within_10_miles")
    st.text_input("Hospitals Within 10 Miles of a Nuclear Reactor", key="hospitals_within_10_miles")
    st.text_input("Total ED Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor", key="ed_beds_within_10_miles")
    st.text_input("Total Beds at Hospital(s) Within 10 Miles of a Nuclear Reactor", key="total_beds_within_10_miles")
    st.text_input("FTE Nurses Employed at Hospital(s) Within 10 Miles of a Nuclear Reactor", key="fte_nurses_within_10_miles")
    st.text_input("If Hospitals Within 10 Miles of Nuclear Reactor is a Trauma Center, Number of ORs", key="ors_within_10_miles")
    st.text_input("Nursing Homes Within 10 Miles of a Nuclear Reactor", key="nursing_homes_within_10_miles")
    st.text_input("Total Beds at Nursing Homes Within 10 Miles of a Nuclear Reactor", key="total_beds_nursing_homes_within_10_miles")
    st.text_input("PCPs Within 10 Miles of a Nuclear Reactor", key="pcps_within_10_miles")
    st.text_input("Pharmacists Within 10 Miles of a Nuclear Reactor", key="pharmacists_within_10_miles")
    st.text_input("Mental Health Professionals Within 10 Miles of a Nuclear Reactor", key="mental_health_professionals_within_10_miles")
    st.text_input("Morgue Units Located Within 10 Miles of a Nuclear Reactor", key="morgue_units_within_10_miles")
    st.text_input("Large College Campus", key="large_college_campus")
    st.text_input("Population Living on Large College Campus", key="population_living_on_campus")
    st.text_input("Large public building or space target for terrorist attack", key="terrorist_target")
    st.text_input("People occupy building/space at its busiest time", key="people_occupy_space")
    st.text_input("Residential Population density of surrounding area", key="residential_population_density")
    st.text_input("Daytime Population density of surrounding area", key="daytime_population_density")

    # Button to submit and save form data
    if st.button("Save Data"):
        handle_form_submission()

# Run the page
show()
