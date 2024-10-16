import streamlit as st
import json


# Function to collect and store baseline data
def store_baseline_data():
    # Collect all baseline data into a dictionary
    baseline_data = {}
    # Total Population in Jurisdiction
    baseline_data["total_population"] = st.text_input("Total Population in Jurisdiction:", value=1000000)
    st.markdown("<h2 class='header'>Human Impact</h2>", unsafe_allow_html=True)

    # Mortality Section
    st.markdown("<b>Mortality</b>", unsafe_allow_html=True)
    baseline_data["total_deaths_per_day"] = st.number_input("Total Deaths Per Day:", value=0.0, min_value=0.0, step=0.1)
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["deaths_data_source"] = st.text_input("Data source for Total Deaths")

    # EMS Transports Section
    st.markdown("<b>EMS Transports</b>", unsafe_allow_html=True)
    baseline_data["total_transports_per_day"] = st.text_input("Total Transports Per Day:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["transports_data_source"] = st.text_input("Data source for EMS Transports")

    # ED Visits Section
    st.markdown("<b>ED Visits</b>", unsafe_allow_html=True)
    baseline_data["total_ed_visits_per_day"] = st.text_input("Total ED Visits Per Day:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["ed_visits_data_source"] = st.text_input("Data source for ED Visits")

    # Primary Care Office Visits Section
    st.markdown("<b>Primary Care Office Visits</b>", unsafe_allow_html=True)
    baseline_data["total_office_visits_per_day"] = st.text_input("Total Office Visits Per Day:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["office_visits_data_source"] = st.text_input("Data source for Office Visits")

    # Trauma Center Injuries Section
    st.markdown("<b>Trauma Center Injuries</b>", unsafe_allow_html=True)
    baseline_data["total_trauma_injuries_per_day"] = st.text_input("Total Trauma Center Injuries Per Day:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["trauma_injuries_data_source"] = st.text_input("Data source for Trauma Center Injuries")

    st.markdown("<h2 class='header'>Healthcare Service Impact</h2>", unsafe_allow_html=True)

    # Outpatient Services Section
    st.markdown("<b>Outpatient Services</b>", unsafe_allow_html=True)
    baseline_data["total_pcps"] = st.text_input("Total PCPs:", value="Not Calculated")
    baseline_data["pcps_per_100k"] = st.text_input("PCPs per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["pcps_data_source"] = st.text_input("Data source for PCPs")

    # Emergency Department Services Section
    st.markdown("<b>Emergency Department Services</b>", unsafe_allow_html=True)
    baseline_data["total_ed_beds"] = st.text_input("Total ED Beds:", value="Not Calculated")
    baseline_data["ed_beds_per_100k"] = st.text_input("ED Beds per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["ed_beds_data_source"] = st.text_input("Data source for ED Beds")

    # Hospital Beds Section
    st.markdown("<b>Hospital Beds</b>", unsafe_allow_html=True)
    baseline_data["total_hospital_beds"] = st.text_input("General Acute Care Hospital Beds:", value="Not Calculated")
    baseline_data["specialty_hospital_beds"] = st.text_input("Specialty Hospital Beds:", value="Not Calculated")
    baseline_data["hospital_beds_total"] = st.text_input("Total Hospital Beds:", value="Not Calculated")
    baseline_data["hospital_beds_per_100k"] = st.text_input("Hospital Beds per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["hospital_beds_data_source"] = st.text_input("Data source for Hospital Beds")

    # Ancillary Services Section
    st.markdown("<b>Ancillary Services</b>", unsafe_allow_html=True)
    baseline_data["total_pharmacists"] = st.text_input("Total Pharmacists:", value="Not Calculated")
    baseline_data["pharmacists_per_100k"] = st.text_input("Pharmacists per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["pharmacists_data_source"] = st.text_input("Data source for Pharmacists")

    # Trauma Units Section
    st.markdown("<b>Trauma Units</b>", unsafe_allow_html=True)
    baseline_data["total_trauma_units"] = st.text_input("Total Trauma Center Functioning ORs:", value="Not Calculated")
    baseline_data["trauma_units_per_100k"] = st.text_input("Trauma ORs per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["trauma_units_data_source"] = st.text_input("Data source for Trauma ORs")

    # Mental Health Services Section
    st.markdown("<b>Mental Health Services</b>", unsafe_allow_html=True)
    baseline_data["total_mental_health_providers"] = st.text_input("Total Mental Health Providers:", value="Not Calculated")
    baseline_data["mental_health_providers_per_100k"] = st.text_input("Mental Health Providers per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["mental_health_providers_data_source"] = st.text_input("Data source for Mental Health Providers")

    st.markdown("<h2 class='header'>Inpatient Healthcare Facility Infrastructure Impact</h2>", unsafe_allow_html=True)

    # Hospital Personnel Section
    st.markdown("<b>Hospital Personnel</b>", unsafe_allow_html=True)
    baseline_data["total_hospital_employed_fte_rns"] = st.text_input("Total Hospital-Employed FTE RNs:", value="Not Calculated")
    baseline_data["rns_per_shift"] = st.text_input("RNs per Shift:", value="0.00")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["rns_data_source"] = st.text_input("Data source for RNs")

    # Total Patient Days Section
    st.markdown("<b>Total Patient Days of Care Per Year</b>", unsafe_allow_html=True)
    baseline_data["total_patient_days_per_year"] = st.text_input("Total Patient Days of Care Per Year:", value="Not Calculated")
    baseline_data["patients_per_day"] = st.text_input("Patients Per Day:", value="0.00")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["patients_data_source"] = st.text_input("Data source for Patients")

    baseline_data["patient_to_nurse_ratio"] = st.text_input("Patient-to-Nurse Ratio:", value="N/A")

    # Regional Inpatient Facility Beds Section
    st.markdown("<b>Regional Inpatient Facility Beds</b>", unsafe_allow_html=True)
    baseline_data["total_inpatient_beds"] = st.text_input("Total Hospital Beds:", value="0")
    baseline_data["nursing_home_beds"] = st.text_input("Total Nursing Home Beds:", value="0")
    baseline_data["inpatient_beds_total"] = st.text_input("Total Inpatient Beds:", value="0")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["inpatient_beds_data_source"] = st.text_input("Data source for Inpatient Beds")

    # Facility Generator Fuel Supply Section
    st.markdown("<b>Facility Generator Fuel Supply</b>", unsafe_allow_html=True)
    baseline_data["generator_fuel_hours"] = st.text_input("Smallest Number of Hours of Back-Up Generator Fuel On Hand in Facility:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["generator_fuel_data_source"] = st.text_input("Data source for Generator Fuel")

    # Facility Critical Supplies Section
    st.markdown("<b>Facility Critical Supplies</b>", unsafe_allow_html=True)
    baseline_data["linens_on_hand"] = st.text_input("Smallest Number of Days of Linens On Hand in Facility:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["linens_data_source"] = st.text_input("Data source for Linens")

    st.markdown("<h2 class='header'>Public Health Service Impact</h2>", unsafe_allow_html=True)

    # Public Health Personnel Section
    st.markdown("<b>Public Health Personnel</b>", unsafe_allow_html=True)
    baseline_data["total_public_health_staff"] = st.text_input("Total Public Health Staff:", value="Not Calculated")
    baseline_data["public_health_staff_per_100k"] = st.text_input("Public Health Staff per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["public_health_staff_data_source"] = st.text_input("Data source for Public Health Staff")

    # Surveillance Section
    st.markdown("<b>Surveillance</b>", unsafe_allow_html=True)
    baseline_data["case_reports_per_day"] = st.text_input("Number of Case Reports per Day to Health Department:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["case_reports_data_source"] = st.text_input("Data source for Case Reports")

    # Laboratory Services Section
    st.markdown("<b>Laboratory Services</b>", unsafe_allow_html=True)
    baseline_data["specimens_processed_per_day"] = st.text_input("Number of Specimens Processed per Day:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["specimens_data_source"] = st.text_input("Data source for Specimens")

    # Health Communications Section
    st.markdown("<b>Health Communications</b>", unsafe_allow_html=True)
    baseline_data["health_comm_hours_per_week"] = st.text_input("Number of Personnel Hours per Week Needed to Generate Health Communications:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["health_comm_data_source"] = st.text_input("Data source for Health Communications")

    # Fatality Management Section
    st.markdown("<b>Fatality Management</b>", unsafe_allow_html=True)
    baseline_data["morgue_capacity"] = st.text_input("Total Morgue Capacity:", value="Not Calculated")
    baseline_data["morgue_capacity_per_100k"] = st.text_input("Morgue Capacity per 100,000:", value="Not Calculated")
    st.markdown("<b>Data source:</b>", unsafe_allow_html=True)
    baseline_data["morgue_capacity_data_source"] = st.text_input("Data source for Morgue Capacity")

    # Save the baseline data to a JSON file
    json_file_path = "baseline_data.json"
    with open(json_file_path, 'w') as f:
        json.dump(baseline_data, f)
    
    st.success(f"Baseline data saved to {json_file_path}!")

# Function to display the UI
def show():
    #st.title("Baseline Health Services Data")
    
    # Store baseline data
    store_baseline_data()

# Run the baseline page
show()