import streamlit as st

def show():

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Hearing Disability</b></div>
        <label class="label">Percent of Population with a Hearing Disability:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Vision Disability</b></div>
        <label class="label">Percent of Population with a Vision Disability:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Ambulatory Disability</b></div>
        <label class="label">Percent of Population with an Ambulatory Disability:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Cognitive Disability</b></div>
        <label class="label">Percent of Population with a Cognitive Disability:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Limited English Proficiency</b></div>
        <label class="label">Percent of Population with Limited English Proficiency:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Poverty</b></div>
        <label class="label">Percent of Population in Poverty:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Chronic Diseases (Diabetes)</b></div>
        <label class="label">Percent of Population with Diabetes:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Children Under 18</b></div>
        <label class="label">Percent of Population Under Age 18:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="subheader"><b>Elderly 65 and Older</b></div>
        <label class="label">Percent of Population Age 65 and Older:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Population Size Score:</label>
        <input class="text-input" type="text" placeholder="0">
        <label class="label">Data Source:</label>
        <input class="text-input" type="text" placeholder="Enter data source">
    </div>
    """, unsafe_allow_html=True)

# To display the content
show()
