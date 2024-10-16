import streamlit as st
from views.hazard_data import (
    active_shooter,
    biological_terrosim,
    chemical_terrosim,
    civil_disturbance,
    coastal_storm,
    conventional_explosive,
    cyber_terrorism,
    drought,
    fire,
    flood,
    hazardous_materials_release,
    localized_infectious_disease,
    nuclear_facility_accident,
    pandemic,
    radiation_disperal_device,
    temperature_extremes,
    tornado,
    utility_interruption,
    winter_strom
)

def show():
    st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='header'>Step 2. Hazard Data</h2>", unsafe_allow_html=True)
    st.write("This section will contain hazard data.")

    option = st.selectbox("Choose an option", [
    "active_shooter",
    "biological_terrosim",
    "chemical_terrosim",
    "civil_disturbance",
    "coastal_storm",
    "conventional_explosive",
    "cyber_terrorism",
    "drought",
    "earthquake",
    "fire",
    "flood",
    "hazardous_materials_release",
    "localized_infectious_disease",
    "nuclear_facility_accident",
    "pandemic",
    "radiation_disperal_device",
    "temperature_extremes",
    "tornado",
    "utility_interruption",
    "winter_strom"
    ])

    if option == "active_shooter":
        active_shooter.show()
    elif option == "biological_terrosim":
        biological_terrosim.show()
    elif option == "chemical_terrosim":
        chemical_terrosim.show()
    elif option == "civil_disturbance":
        civil_disturbance.show()
    elif option == "coastal_storm":
        coastal_storm.show()
    elif option == "conventional_explosive":
        conventional_explosive.show()
    elif option == "cyber_terrorism":
        cyber_terrorism.show()
    elif option == "drought":
        drought.show()
    elif option == "fire":
        fire.show()
    elif option == "flood":
        flood.show()
    elif option == "hazardous_materials_release":
        hazardous_materials_release.show()
    elif option == "localized_infectious_disease":
        localized_infectious_disease.show()
