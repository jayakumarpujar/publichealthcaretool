import streamlit as st
from views.hazard_data import (
    active_shooter,
    biological_terrosim,
    chemical_terrosim,
    accidental_explosive,
    cyber_terrorism,
    drought,
    fire,
    flood,
    hazardous_materials_release,
    infectious_disease,
    intentional_explosive,
    radiation_dispersal_device,
    temperature_extremes,
    tornado,
    utility_interruption,
    winter_storm
)

def show():
    st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='header'>Step 2. Hazard Data</h2>", unsafe_allow_html=True)
    st.write("This section will contain hazard data.")

    option = st.selectbox("Choose an option", [
    "active_shooter",
    "biological_terrosim",
    "chemical_terrosim",
    "accidental_explosive",
    "cyber_terrorism",
    "drought",
    "fire",
    "flood",
    "hazardous_materials_release",
    "infectious_disease",
    "intentional_explosive",
    "radiation_dispersal_device",
    "temperature_extremes",
    "tornado",
    "utility_interruption",
    "winter_storm"
    ])

    if option == "active_shooter":
        active_shooter.show()
    elif option == "biological_terrosim":
        biological_terrosim.show()
    elif option == "chemical_terrosim":
        chemical_terrosim.show()
    elif option == "accidental_explosive":
        accidental_explosive.show()
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
    elif option == "infectious_disease":
        infectious_disease.show()
    elif option == "intentional_explosive":
        intentional_explosive.show()
    elif option == "radiation_dispersal_device":
        radiation_dispersal_device.show()
    elif option == "temperature_extremes":
        temperature_extremes.show()
    elif option == "tornado":
        tornado.show()
    elif option == "utility_interruption":
        utility_interruption.show()
    elif option == "winter_storm":
        winter_storm.show()       