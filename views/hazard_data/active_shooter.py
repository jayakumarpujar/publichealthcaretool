import streamlit as st

def show():
    
    
    st.markdown("<h1 class='header'>Pennsylvania Public Health Risk Assessment Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Human Impact</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='section-title'>Mortality</h3>", unsafe_allow_html=True)
    
    # Input fields
    baseline_mortality = st.number_input("Baseline Mortality per Day:", value=0)
    hazard_increase_mortality = st.number_input("Hazard-Related Increase in Mortality per Day:", value=0)
    
    st.markdown("<span class='input-label'>Magnitude Score:</span>", unsafe_allow_html=True)
    magnitude_option = st.radio(
        "",
        [
            "No change from baseline (Score = 0)",
            "≤ 5% increase (Score = 1)",
            "≤ 50% increase (Score = 2)",
            "≤ 100% increase (Score = 3)",
            "> 100% increase (Score = 4)"
        ],
        index=0,
        key="mortality_magnitude_radio"
    )
    magnitude_score = {
        "No change from baseline (Score = 0)": 0,
        "≤ 5% increase (Score = 1)": 1,
        "≤ 50% increase (Score = 2)": 2,
        "≤ 100% increase (Score = 3)": 3,
        "> 100% increase (Score = 4)": 4,
    }[magnitude_option]
    st.markdown(f"<span class='result-text'>Magnitude Score: {magnitude_score}</span>", unsafe_allow_html=True)

    st.markdown("**OR, Estimate the Magnitude Qualitatively:**", unsafe_allow_html=True)
    qualitative_option = st.selectbox(
        "Qualitative Magnitude Score:",
        [
            "No impact (Score = 0)",
            "≤ 1 day (Score = 1)",
            "≤ 1 week (Score = 2)",
            "≤ 2 weeks (Score = 3)",
            "> 2 weeks (Score = 4)"
        ],
        index=0,
        key="mortality_qualitative_select"
    )
    qualitative_score = {
        "No impact (Score = 0)": 0,
        "≤ 1 day (Score = 1)": 1,
        "≤ 1 week (Score = 2)": 2,
        "≤ 2 weeks (Score = 3)": 3,
        "> 2 weeks (Score = 4)": 4,
    }[qualitative_option]
    
    # Display the calculated Duration Score
    st.markdown("<span class='input-label'>Duration of Impact:</span>", unsafe_allow_html=True)
    duration_option = st.selectbox(
        "Duration Score:",
        [
            "No impact (Score = 0)",
            "≤ 1 day (Score = 1)",
            "≤ 1 week (Score = 2)",
            "≤ 2 weeks (Score = 3)",
            "> 2 weeks (Score = 4)"
        ],
        index=0,
        key="mortality_duration_select"
    )
    duration_score = {
        "No impact (Score = 0)": 0,
        "≤ 1 day (Score = 1)": 1,
        "≤ 1 week (Score = 2)": 2,
        "≤ 2 weeks (Score = 3)": 3,
        "> 2 weeks (Score = 4)": 4,
    }[duration_option]
    
    # Calculate Mortality Score
    mortality_score = (qualitative_score + duration_score) / 2
    
    # Display Data Source / Explanation
    st.text_area("Data Source / Explanation (Optional):", "In the VA Tech Massacre of 2007, 33 died at the scene, including the shooter (Armstrong & Frykberg, 2007).")
    
    # Display Resulting Scores
    st.markdown(f"<span class='result-text'>Qualitative Magnitude Score: {qualitative_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>Duration Score: {duration_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>Mortality Score: {mortality_score}</span>", unsafe_allow_html=True)

# Run the function to display the webpage
show()
