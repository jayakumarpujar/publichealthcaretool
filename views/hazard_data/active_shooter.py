import streamlit as st

def show():
    
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

    st.markdown("<h2 class='subheader'>Mortality</h2>", unsafe_allow_html=True)
    
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
#*************************************************************************************************************
    st.markdown("<h2 class='subheader'>EMS Transports</h2>", unsafe_allow_html=True)
    
    # Input fields
    baseline_transports = st.number_input("Baseline Transports per Day:", value=0)
    hazard_increase_transports = st.number_input("Hazard-Related Increase in Transports per Day:", value=0)
    
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
        key="ems_magnitude_radio"
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
        key="ems_qualitative_select"
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
        key="ems_duration_select"
    )
    duration_score = {
        "No impact (Score = 0)": 0,
        "≤ 1 day (Score = 1)": 1,
        "≤ 1 week (Score = 2)": 2,
        "≤ 2 weeks (Score = 3)": 3,
        "> 2 weeks (Score = 4)": 4,
    }[duration_option]
    
    # Calculate EMS Transports Score
    ems_score = (qualitative_score + duration_score) / 2
    
    # Display Data Source / Explanation
    st.text_area("Data Source / Explanation (Optional):", "In the VA Tech Massacre of 2007, 17 were transported by EMS (Armstrong & Frykberg, 2007).")
    
    # Display Resulting Scores
    st.markdown(f"<span class='result-text'>Qualitative Magnitude Score: {qualitative_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>Duration Score: {duration_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>EMS Transports Score: {ems_score}</span>", unsafe_allow_html=True)


    st.markdown("<h2 class='subheader'>ED Visits</h2>", unsafe_allow_html=True)
    
    # Input fields
    baseline_ed_visits = st.number_input("Baseline ED Visits per Day:", value=0)
    hazard_increase_ed_visits = st.number_input("Hazard-Related Increase in ED Visits per Day:", value=0)
    
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
        key="ed_magnitude_radio"
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
        key="ed_qualitative_select"
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
        key="ed_duration_select"
    )
    duration_score = {
        "No impact (Score = 0)": 0,
        "≤ 1 day (Score = 1)": 1,
        "≤ 1 week (Score = 2)": 2,
        "≤ 2 weeks (Score = 3)": 3,
        "> 2 weeks (Score = 4)": 4,
    }[duration_option]
    
    # Calculate ED Visits Score
    ed_score = (qualitative_score + duration_score) / 2
    
    # Display Data Source / Explanation
    st.text_area("Data Source / Explanation (Optional):", "In the VA Tech Massacre of 2007, 27 are known to have been treated at local emergency departments (Virginia Tech Review Panel, 2007).")
    
    # Display Resulting Scores
    st.markdown(f"<span class='result-text'>Qualitative Magnitude Score: {qualitative_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>Duration Score: {duration_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>ED Visits Score: {ed_score}</span>", unsafe_allow_html=True)

#****************************************************************************************************************************************************************************************************
    
    st.markdown("<h2 class='subheader'>Primary Care Office Visits</h2>", unsafe_allow_html=True)
    
    # Input fields
    baseline_office_visits = st.number_input("Baseline Office Visits per Day:", value=0)
    hazard_increase_office_visits = st.number_input("Hazard-Related Increase in Office Visits per Day:", value=0)
    
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
        key="office_magnitude_radio"
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
        key="office_qualitative_select"
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
        key="office_duration_select"
    )
    duration_score = {
        "No impact (Score = 0)": 0,
        "≤ 1 day (Score = 1)": 1,
        "≤ 1 week (Score = 2)": 2,
        "≤ 2 weeks (Score = 3)": 3,
        "> 2 weeks (Score = 4)": 4,
    }[duration_option]
    
    # Calculate Primary Care Office Visits Score
    office_score = (qualitative_score + duration_score) / 2
    
    # Display Data Source / Explanation
    st.text_area("Data Source / Explanation (Optional):", "")
    
    # Display Resulting Scores
    st.markdown(f"<span class='result-text'>Qualitative Magnitude Score: {qualitative_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>Duration Score: {duration_score}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='result-text'>Primary Care Office Visits Score: {office_score}</span>", unsafe_allow_html=True)
    
    ###############################################
    st.markdown("<h2 class='subheader'>Trauma Center Injuries</h2>", unsafe_allow_html=True)
    baseline_trauma = st.number_input("Baseline Trauma Injuries per Day:", value=0)
    hazard_increase_trauma = st.number_input("Hazard-Related Increase in Trauma Injuries per Day:", value=0)

    magnitude_option_trauma = st.radio(
        "",
        [
            "No change from baseline (Score = 0)",
            "≤ 5% increase (Score = 1)",
            "≤ 50% increase (Score = 2)",
            "≤ 100% increase (Score = 3)",
            "> 100% increase (Score = 4)"
        ],
        index=0,
        key="trauma_magnitude_radio"
    )
    magnitude_score_trauma = calculate_magnitude_score(magnitude_option_trauma)
    st.markdown(f"<span class='result-text'>Magnitude Score: {magnitude_score_trauma}</span>", unsafe_allow_html=True)

    qualitative_option_trauma = st.selectbox(
        "Qualitative Magnitude Score:",
        [
            "No impact (Score = 0)",
            "≤ 1 day (Score = 1)",
            "≤ 1 week (Score = 2)",
            "≤ 2 weeks (Score = 3)",
            "> 2 weeks (Score = 4)"
        ],
        index=0,
        key="trauma_qualitative_select"
    )
    qualitative_score_trauma = calculate_duration_score(qualitative_option_trauma)
    st.markdown(f"<span class='result-text'>Qualitative Magnitude Score: {qualitative_score_trauma}</span>", unsafe_allow_html=True)

    duration_option_trauma = st.selectbox(
        "Duration Score:",
        [
            "No impact (Score = 0)",
            "≤ 1 day (Score = 1)",
            "≤ 1 week (Score = 2)",
            "≤ 2 weeks (Score = 3)",
            "> 2 weeks (Score = 4)"
        ],
        index=0,
        key="trauma_duration_select"
    )
    duration_score_trauma = calculate_duration_score(duration_option_trauma)
    st.markdown(f"<span class='result-text'>Duration Score: {duration_score_trauma}</span>", unsafe_allow_html=True)

    trauma_score = (qualitative_score_trauma + duration_score_trauma) / 2
    st.text_area("Data Source / Explanation (Optional):", "In the VA Tech Massacre of 2007, 10 were taken to surgery at Level III trauma centers, and 2 at a Level I trauma center (Armstrong & Frykberg, 2007).")
    st.markdown(f"<span class='result-text'>Trauma Center Injuries Score: {trauma_score}</span>", unsafe_allow_html=True)

    st.markdown("<h2 class='subheader'>Mental Health Impact</h2>", unsafe_allow_html=True)
    mental_health_option = st.selectbox(
        "Mental Health Impact (Percent of population developing psychopathology and behavioral changes):",
        [
            "Minimal change in population behavior and negligible effects on social functioning.",
            "Effects weak or highly transient; occasional or minor loss of nonessential social functions in a circumscribed geographical area.",
            "Population displays distress with <25% psychopathology.",
            "Population displays distress with 25% - 49% psychopathology.",
            "Population displays distress with ≥50% psychopathology."
        ],
        index=2,
        key="mental_health_select"
    )
    mental_health_score = calculate_magnitude_score(mental_health_option)
    st.markdown(f"<span class='result-text'>Magnitude Score: {mental_health_score}</span>", unsafe_allow_html=True)

    duration_option_mental = st.selectbox(
        "Duration Score:",
        [
            "No impact (Score = 0)",
            "≤ 1 day (Score = 1)",
            "≤ 1 week (Score = 2)",
            "≤ 2 weeks (Score = 3)",
            "> 2 weeks (Score = 4)"
        ],
        index=0,
        key="mental_duration_select"
    )
    duration_score_mental = calculate_duration_score(duration_option_mental)
    st.text_area("Data Source / Explanation (Optional):", "After the VA Tech Massacre of 2007, 15.4% of VA Tech students screened showed high levels of posttraumatic stress symptoms (Hughes et al., 2011).")
    st.markdown(f"<span class='result-text'>Mental Health Score: {(mental_health_score + duration_score_mental) / 2}</span>", unsafe_allow_html=True)

    st.markdown("<h2 class='subheader'>Human Impact Score:</h2>", unsafe_allow_html=True)
    st.markdown("<span class='result-text'>Not Calculated</span>", unsafe_allow_html=True)

def calculate_magnitude_score(option):
    scores = {
        "No change from baseline (Score = 0)": 0,
        "≤ 5% increase (Score = 1)": 1,
        "≤ 50% increase (Score = 2)": 2,
        "≤ 100% increase (Score = 3)": 3,
        "> 100% increase (Score = 4)": 4,
        "Population displays distress with <25% psychopathology.": 1,
        "Population displays distress with 25% - 49% psychopathology.": 3,
        "Population displays distress with ≥50% psychopathology.": 5
    }
    return scores.get(option, 0)

def calculate_duration_score(option):
    scores = {
        "No impact (Score = 0)": 0,
        "≤ 1 day (Score = 1)": 1,
        "≤ 1 week (Score = 2)": 2,
        "≤ 2 weeks (Score = 3)": 3,
        "> 2 weeks (Score = 4)": 4,
    }
    return scores.get(option, 0)


# Run the function to display the webpage
show()
