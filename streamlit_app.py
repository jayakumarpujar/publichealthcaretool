# import streamlit as st
# import pandas as pd

# # Load Excel data
# file_path = '/workspaces/publichealthcaretool/PHRAT_Editable.xlsm'
# df = pd.read_excel(file_path, sheet_name='Main Menu', engine='openpyxl')

# # Set page configuration
# st.set_page_config(page_title="Public Health Care Risk Assessment Tool", layout="centered")

# # Define CSS style for red and white color scheme and enhancing page visuals
# st.markdown("""
#     <style>
#         .main {
#             background-color: #f5f5f5;
#             padding: 20px;
#             color: black;
#         }
#         .stButton button {
#             background-color: red;
#             color: white;
#             text-align: center;
#             font-size: 20px;
#             border-radius: 10px;
#             margin: 20px;
#             align-items: center;
#             padding: 20px;
#             width: 300px;
#             height: 60px;
#             border: none;
#             transition: 0.2s;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.7);
#         }
#         .text-input {
#             margin-top: -10px;
#             background-color: white;
#             color: black;
#             padding: 10px;
#             border: 1px solid #ccc;
#             border-radius: 5px;
#         }
#         .input-container {
#             display: flex;
#             flex-direction: column;
#             gap: 7px;
#             margin-bottom: 15px;
#         }
#         .title {
#             text-align: center;
#             color: red;
#             font-size: 40px;
#             margin-top: 20px;
#         }
#         .subtitle {
#             text-align: center;
#             color: black;
#             font-size: 20px;
#         }
#         .content {
#             color: black;
#             background-color: white;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.7);
#         }
#         .header { color: black; font-size: 24px; text-align: center; }
#         .footer {
#             text-align: center;
#             margin-top: 20px;
#             color: grey;
#         }
#         .back-option {
#             position: absolute;
#             top: 20px;
#             right: 20px;
#             font-size: 18px;
#             color: blue;
#             cursor: pointer;
#         }
#         .back-option:hover {
#             text-decoration: underline;
#         }
        
#     </style>
#     """, unsafe_allow_html=True)

# # Function to display back button
# def back_option():
#     if st.session_state.page != 'main_menu':
#         st.markdown("""
#         <div class="back-option" onclick="window.location.href='/';">Back</div>
#         """, unsafe_allow_html=True)

# # Initialize session state for page navigation
# if 'page' not in st.session_state:
#     st.session_state.page = 'main_menu'

# # Initialize session state for button clicks
# if 'button_clicked' not in st.session_state:
#     st.session_state.button_clicked = 'main_menu'

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Main Menu", "Baseline Data", "Hazard Data", "Analysis Options"])

# if page == "Main Menu":
#     st.session_state.button_clicked = 'main_menu'
# elif page == "Baseline Data":
#     st.session_state.button_clicked = 'baseline_data'
# elif page == "Hazard Data":
#     st.session_state.button_clicked = 'hazard_data'
# elif page == "Analysis Options":
#     st.session_state.button_clicked = 'analysis_options'

# # Main page content
# if st.session_state.button_clicked == 'main_menu':
#     st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
#     st.markdown("<h3 class='subtitle'>Welcome to the Public Health Risk Assessment Tool</h3>", unsafe_allow_html=True)
#     st.markdown("<h4 class='subtitle'>Please select one of the options below:</h4>", unsafe_allow_html=True)

#     # Create central buttons for Overview and Readme
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Overview"):
#             st.session_state.button_clicked = 'overview'

#     with col2:
#         if st.button("Readme"):
#             st.session_state.button_clicked = 'readme'

#     # Conditional content based on button clicked
#     if 'button_clicked' in st.session_state:
#         if st.session_state.button_clicked == 'overview':
            
#             st.header("Overview of the tool")
#             st.write("This section provides an overview of the Public Health Risk Assessment Tool.")
            
#             # Example of displaying data from the .xlsm file
#             st.subheader("Sample Data")
#             st.dataframe(df.head())
            
#             # Add your overview content here
#             st.markdown("""
#             - **Tool Purpose:** Assess public health risks based on various parameters.
#             - **Data Sources:** Epidemiological, demographic, and environmental data.
#             - **Features:** Interactive charts, metrics, and predictive models.
#             """)
#             st.markdown("</div>", unsafe_allow_html=True)
            
#         elif st.session_state.button_clicked == 'readme':
            
#             st.header("Readme")
#             st.markdown("""
#             The Pennsylvania Public Health Risk Assessment Tool (PHRAT) was developed by the Center for Public Health Readiness and Communications (CPHRC) at Drexel University School of Public Health, in cooperation with the Pennsylvania Department of Health. 
            
#             This publication was supported by Cooperative Agreement Number 2U90TP316967_11 from the Centers for Disease Control and Prevention (CDC). Its contents are solely the responsibility of the authors and do not necessarily represent the official views of CDC. 
            
#             The CPHRC worked with preparedness planners, public health agency representatives, and other stakeholders to complete a comprehensive public health risk assessment of the Philadelphia Metropolitan Statistical Area (MSA). CPHRC staff built upon existing approaches to this task, using the UCLA Hazard Risk Assessment Instrument and the Kaiser Permanente Hazard and Vulnerability Analysis to develop a tool to analyze hazards with respect to their public health impact. 
            
#             The Pennsylvania PHRAT is designed to be used to assess the public health impact of hazards that can affect a jurisdiction. The tool generates an estimate of hazard-specific risk, based on the probability and impact severity identified for each hazard. Additionally, the PHRAT generates an “adjusted risk,” which incorporates an assessment of the additional planning required to reduce a hazard's impact on at-risk populations. 
            
#             The adjusted risk is calculated by assessing the size of at-risk populations in a jurisdiction and the special planning required to address the needs of these populations in specific disasters. A Preparedness Score is generated using the jurisdiction’s current capacity in each of the 15 Public Health Preparedness capabilities and the 8 Healthcare System Preparedness capabilities, as well as the relevance of each capability to specific hazards. 
            
#             The final output of the tool is a Planning Priority Score, which reflects both adjusted risk and preparedness. The derivation of the various scores is illustrated in the worksheet "Overview of the Tool." To navigate to this sheet, return to the Main Menu and click the yellow "Overview of the Tool" button in the "Overview" box.
#             """, unsafe_allow_html=True)
#             st.markdown("</div>", unsafe_allow_html=True)
            

# elif st.session_state.button_clicked == 'baseline_data':
    
#     st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)

# # Baseline Data section header
#     st.markdown("<h2 class='header'>Step 1. Baseline Data</h2>", unsafe_allow_html=True)

#     if st.button("Baseline Health, Services, and Infrastructure"):
        
#         st.markdown("""
#         <div class="input-container">
#         Total Population in Jurisdiction:
#         <input class="text-input" type="text" placeholder="Enter total population">
#         </div>""", unsafe_allow_html=True)

#         st.markdown("<h2 class='header'>Human Impact</h2>", unsafe_allow_html=True)

#         st.markdown("""
#         <div class="input-container">
#             <b>Mortality</b>
#             <label>Total Deaths Per Day:</label>
#             <input class="text-input" type="text" placeholder="Not Calculated">
#             <label>Data source:</label>
#             <input class="text-input" type="text" placeholder="Enter data source">
#         </div>
#         <div class="input-container">
#             <b>EMS Transports</b>
#             <label>Total Transports Per Day:</label>
#             <input class="text-input" type="text" placeholder="Not Calculated">
#             <label>Data source:</label>
#             <input class="text-input" type="text" placeholder="Enter data source">
#         </div>
#         <div class="input-container">
#             <b>ED Visits</b>
#             <label>Total ED Visits Per Day:</label>
#             <input class="text-input" type="text" placeholder="Not Calculated">
#             <label>Data source:</label>
#             <input class="text-input" type="text" placeholder="Enter data source">
#         </div>
#         <div class="input-container">
#             <b>Primary Care Office Visits</b>
#             <label>Total Office Visits Per Day:</label>
#             <input class="text-input" type="text" placeholder="Not Calculated">
#             <label>Data source:</label>
#             <input class="text-input" type="text" placeholder="Enter data source">
#         </div>
#         <div class="input-container">
#             <b>Trauma Center Injuries</b>
#             <label>Total Trauma Center Injuries Per Day:</label>
#             <input class="text-input" type="text" placeholder="Not Calculated">
#             <label>Data source:</label>
#             <input class="text-input" type="text" placeholder="Enter data source">
#         </div> """, unsafe_allow_html=True)
        
#     elif st.button("Baseline At-Risk Populations"):
#         st.markdown("</div>", unsafe_allow_html=True)
        
#     elif st.button("Baseline Public Health Preparedness Capability Status"):
#         st.markdown("</div>", unsafe_allow_html=True)
        
#     elif st.button("Community Characteristics"):
#         st.markdown("</div>", unsafe_allow_html=True)
    
# elif st.session_state.button_clicked == 'hazard_data':
#     st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
#     st.markdown("<h2 class='header'>Step 2. Hazard Data</h2>", unsafe_allow_html=True)
#     st.write("This section will contain hazard data.")
#     # Add specific content for Hazard Data here
#     st.markdown("</div>", unsafe_allow_html=True)
    
# elif st.session_state.button_clicked == 'analysis_options':
#     st.markdown("<h1 class='title'>Public Health Care Risk Assessment Tool</h1>", unsafe_allow_html=True)
#     st.markdown("<h2 class='header'>Step 3. Analysis </h2>", unsafe_allow_html=True)
#     st.write("This section will contain analysis data.")
#     # Add specific content for Analysis here
#     st.markdown("</div>", unsafe_allow_html=True)
    
# # Footer
# st.markdown("<div class='footer'>© 2024 Public Health Risk Assessment Tool</div>", unsafe_allow_html=True)

# # Optional: Add a footer in the main area
# st.markdown("""
#     ---
# """)
