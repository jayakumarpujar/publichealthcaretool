import streamlit as st
import pandas as pd

def show():
    # Load Excel data
    file_path = '/workspaces/publichealthcaretool/PHRAT_Editable.xlsm'
    df = pd.read_excel(file_path, sheet_name='Main Menu', engine='openpyxl')

    st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Welcome to the Public Health Risk Assessment Tool</h3>", unsafe_allow_html=True)
    st.markdown("<h4 class='subtitle'>Please select one of the options below:</h4>", unsafe_allow_html=True)

    # Create central buttons for Overview and Readme
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Overview"):
            st.session_state.page = 'overview'

    with col2:
        if st.button("Readme"):
            st.session_state.page = 'readme'

    # Conditional content based on button clicked
    if 'page' in st.session_state:
        if st.session_state.page == 'overview':
            st.header("Overview of the tool")
            st.write("This section provides an overview of the Public Health Risk Assessment Tool.")
            st.subheader("Sample Data")
            st.dataframe(df.head())
            st.markdown("""
            - **Tool Purpose:** Assess public health risks based on various parameters.
            - **Data Sources:** Epidemiological, demographic, and environmental data.
            - **Features:** Interactive charts, metrics, and predictive models.
            """, unsafe_allow_html=True)
            
        elif st.session_state.page == 'readme':
            st.header("Readme")
            st.markdown("""
            The Pennsylvania Public Health Risk Assessment Tool (PHRAT) was developed by the Center for Public Health Readiness and Communications (CPHRC) at Drexel University School of Public Health, in cooperation with the Pennsylvania Department of Health. 
            
            This publication was supported by Cooperative Agreement Number 2U90TP316967_11 from the Centers for Disease Control and Prevention (CDC). Its contents are solely the responsibility of the authors and do not necessarily represent the official views of CDC. 
            
            The CPHRC worked with preparedness planners, public health agency representatives, and other stakeholders to complete a comprehensive public health risk assessment of the Philadelphia Metropolitan Statistical Area (MSA). CPHRC staff built upon existing approaches to this task, using the UCLA Hazard Risk Assessment Instrument and the Kaiser Permanente Hazard and Vulnerability Analysis to develop a tool to analyze hazards with respect to their public health impact. 
            
            The Pennsylvania PHRAT is designed to be used to assess the public health impact of hazards that can affect a jurisdiction. The tool generates an estimate of hazard-specific risk, based on the probability and impact severity identified for each hazard. Additionally, the PHRAT generates an “adjusted risk,” which incorporates an assessment of the additional planning required to reduce a hazard's impact on at-risk populations. 
            
            The adjusted risk is calculated by assessing the size of at-risk populations in a jurisdiction and the special planning required to address the needs of these populations in specific disasters. A Preparedness Score is generated using the jurisdiction’s current capacity in each of the 15 Public Health Preparedness capabilities and the 8 Healthcare System Preparedness capabilities, as well as the relevance of each capability to specific hazards. 
            
            The final output of the tool is a Planning Priority Score, which reflects both adjusted risk and preparedness. The derivation of the various scores is illustrated in the worksheet "Overview of the Tool." To navigate to this sheet, return to the Main Menu and click the yellow "Overview of the Tool" button in the "Overview" box.
            """, unsafe_allow_html=True)
