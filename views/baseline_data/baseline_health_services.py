import streamlit as st

def show():
    st.markdown("""
    <div class="input-container">
        <b>Total Population in Jurisdiction:</b>
        <input class="text-input" type="text" placeholder="Enter total population">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 class='header'>Human Impact</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <b>Mortality</b>
        <label>Total Deaths Per Day:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label>Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    <div class="input-container">
        <b>EMS Transports</b>
        <label>Total Transports Per Day:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label>Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    <div class="input-container">
        <b>ED Visits</b>
        <label>Total ED Visits Per Day:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label>Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    <div class="input-container">
        <b>Primary Care Office Visits</b>
        <label>Total Office Visits Per Day:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label>Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    <div class="input-container">
        <b>Trauma Center Injuries</b>
        <label>Total Trauma Center Injuries Per Day:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label>Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)
#######################################################################################
    st.markdown("<h2 class='header'>Healthcare Service Impact</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Outpatient Services</b></div>
        <label class="label">Total PCPs:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">PCPs per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Emergency Department Services</b></div>
        <label class="label">Total ED Beds:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">ED Beds per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Hospital Beds</b></div>
        <label class="label">General Acute Care Hospital Beds:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Specialty Hospital Beds:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Total Hospital Beds:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Hospital Beds per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Ancillary Services</b></div>
        <label class="label">Total Pharmacists:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Pharmacists per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Trauma Units</b></div>
        <label class="label">Total Trauma Center Functioning ORs:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Trauma ORs per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Mental Health Services</b></div>
        <label class="label">Total Mental Health Providers:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Mental Health Providers per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)
##############################################################################
    st.markdown("<h2 class='header'>Inpatient Healthcare Facility Infrastructure Impact</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Hospital Personnel</b></div>
        <label class="label">Total Hospital-Employed FTE RNs:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">RNs per Shift:</label>
        <input class="text-input" type="text" placeholder="0.00">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <label class="label">Total Patient Days of Care Per Year:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Patients Per Day:</label>
        <input class="text-input" type="text" placeholder="0.00">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <label class="label">Patient-to-Nurse Ratio:</label>
        <input class="text-input" type="text" placeholder="N/A" disabled>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Regional Inpatient Facility Beds</b></div>
        <label class="label">Total Hospital Beds:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Total Nursing Home Beds:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Total Inpatient Beds:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Facility Generator Fuel Supply</b></div>
        <label class="label">Smallest Number of Hours of Back-Up Generator Fuel On Hand in Facility:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Facility Critical Supplies</b></div>
        <label class="label">Smallest Number of Days of Linens On Hand in Facility:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)
####################################################################################
    st.markdown("<h2 class='header'>Public Health Service Impact</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Public Health Personnel</b></div>
        <label class="label">Total Public Health Staff:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Public Health Staff per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Surveillance</b></div>
        <label class="label">Number of Case Reports per Day to Health Department (requiring investigation, monitoring, tracking, or other public health action):</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Laboratory Services</b></div>
        <label class="label">No. of Specimens Processed per Day:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Health Communications and Public Information</b></div>
        <label class="label">Number of Personnel Hours per Week Needed to Generate Health Communications to External Partners or the General Public:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Fatality Management</b></div>
        <label class="label">Total Morgue Capacity:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Morgue Capacity per 100,000:</label>
        <input class="text-input" type="text" placeholder="Not Calculated">
        <label class="label">Data source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

# To display the content
show() 




    
    