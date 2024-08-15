import streamlit as st

def show():
    st.markdown("<h2 class='header'>Baseline Healthcare Preparedness Capability</h2>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='header'>Healthcare System Preparedness</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Develop, refine, or sustain Healthcare Coalitions.</div>
                <p>Consisting of a collaborative network of healthcare organizations and their respective public and private sector response partners within a defined region. Healthcare Coalitions serve as a multi-agency coordinating group that assists Emergency Management and Emergency Support Function (ESF) #8 with preparedness, response, recovery, and mitigation activities related to healthcare organization disaster operations. The primary function of the Healthcare Coalition includes sub-state regional, healthcare system emergency preparedness activities involving the member organizations. Healthcare Coalitions also may provide multiagency coordination to interface with the appropriate level of emergency operations in order to assist with the provision of situational awareness and the coordination of resources for healthcare organizations during a response.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Coordinate with emergency management.</div>
                <p>To develop local and state emergency operations plans that address the concerns and unique needs of healthcare organizations. Plans should encompass the ability to deliver essential healthcare services during a response. This includes the assessment phases of planning to determine needs and priorities of healthcare organizations and the development of operational courses of action used during responses.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 3: Identify and prioritize healthcare assets and essential services.</div>
                <p>Within a healthcare delivery area or region (Healthcare Coalition area). Coordinate planning to protect and enhance priority healthcare assets and essential services in order to ensure continued healthcare delivery to the community during a disaster.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 4: Perform resource assessments and develop plans.</div>
                <p>To assist healthcare organizations address gaps associated with planning, training, staffing, and equipping that improve resource availability during response and recovery. This is an ongoing process in the preparedness cycle guided by healthcare organization resource needs. These needs are based on the outcome of gap analysis, the evaluation of training, exercises, and actual incidents or events, and subsequent corrective actions.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 5: Coordinate training for healthcare responders.</div>
                <p>And supporting agencies in order to provide the required knowledge, skills, and abilities needed to prepare and respond to a disaster. Training curriculums are based on assessments, strategies, improvement plans, and ongoing evaluation efforts. Training is coordinated with ongoing training initiatives from healthcare and response partners. Training should include appropriate National Incident Management System (NIMS) or equivalent training.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 6: Coordinate an exercise, evaluation, and corrective action program.</div>
                <p>To continuously improve healthcare preparedness, response, and recovery. Exercises should assess and validate the effectiveness and efficiency of capabilities and the adequacy of policies, plans, procedures, and protocols. Exercises should be coordinated vertically and horizontally with healthcare and emergency response partners. Evaluation and improvement planning should track corrective actions associated with identified healthcare capability deficiencies observed during exercises and incidents. Corrective actions provide the means to improve medical operational preparedness to perform critical healthcare response tasks. Corrective actions also contribute to the continuous preparedness cycle by ensuring updated strategies and plans are incorporated into new preparedness-building activities.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 7: Participate with planning to address at-risk individuals.</div>
                <p>And those with special medical needs whose care can only occur at healthcare facilities. This includes coordination with public health and ESF #6 mass care planning to determine the transfer and transport options for individuals with special medical needs to and from shelters/healthcare facilities. It also includes continued involvement with public health planning initiatives for at-risk individuals with functional needs so that assistance or guidance can be provided to healthcare organizations regarding activity that may affect healthcare.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Healthcare System Preparedness Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

########################################################################################

    st.markdown("<h2 class='header'>Healthcare System Recovery</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Identify healthcare organization recovery needs.</div>
                <p>And develop priority recovery processes to support a return to normalcy of operations or a new standard of normalcy for the provision of healthcare delivery to the community.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Maintain continuity of the healthcare delivery.</div>
                <p>By coordinating recovery across functional healthcare organizations and encouraging business continuity planning. COOP guides how key resources from governmental, non-governmental, and private sector agencies can be used to support the sustainment and reestablishment of essential services for healthcare organizations. This coordination assists healthcare organizations to maintain their functional capabilities during, and after an all hazards incident and enables a rapid and more effective recovery.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Healthcare System Recovery Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

#####################################################################################

    st.markdown("<h2 class='header'>Emergency Operations Coordination</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Coordinate the protocols and criteria.</div>
                <p>For the multi-agency representation of healthcare organizations into local and state emergency operations during an incident response.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Assess the incident’s impact on healthcare delivery.</div>
                <p>In order to determine immediate healthcare organization resource needs and the status of healthcare delivery during an incident response. This includes assisting with the creation of the incident common operating picture and developing the processes for notification and information exchange between relevant response partners, stakeholders, and healthcare organizations.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 3: Coordinate resource allocation for healthcare organizations.</div>
                <p>By assisting incident management with decisions regarding resource availability and needs. This process should continue throughout incident response and recovery; including ongoing coordination to track resources for decision-making and optimal resource allocation.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 4: The processes that assist healthcare organizations with the return of resources.</div>
                <p>That are no longer required to support the incident. This includes the return of shared resources through incident management processes or directly to the providing healthcare organization. Following the return of assets, incorporate best practices and lessons learned into the continuous improvement process (after action reports/improvement plans/corrective actions).</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Emergency Operations Coordination Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
######################################################################################

    st.markdown("<h2 class='header'>Fatality Management</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Coordinate with agencies responsible for fatality management.</div>
                <p>(e.g., medical examiner, coroner’s office, emergency management) to assist with the temporary storage of human remains during periods of death surges at healthcare organizations when morgue space is exceeded or unavailable.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Coordination with the agency responsible to provide assistance.</div>
                <p>To the community regarding ante-mortem data to provide assistance to healthcare organizations for the processes to direct family and community members seeking information about missing family members to the right locations that are available in the community.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 3: Coordinate with the lead jurisdictional authority.</div>
                <p>And jurisdictional and regional mental/behavioral health partners to assist healthcare organizations with the processes to solicit support for the provision of non-intrusive, culturally sensitive mental/behavioral health support services to family members of the deceased, incident survivors, and responders, if requested.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Fatality Management Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

###############################################################################

    st.markdown("<h2 class='header'>Medical Surge</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Develop, refine, and sustain processes.</div>
                <p>To ensure incident management decisions during medical surge incidents are coordinated through multi-agency collaboration representative of the community healthcare organizations’ priorities and needs. Coordination is achieved by ensuring that there are plans and protocols in place to guide the decisions made by incident management. It may also be achieved through real time multi-agency coordination by healthcare organizations during a response.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Coordination between the State, healthcare organizations, and Healthcare Coalitions.</div>
                <p>With EMS operations and medical oversight to develop, refine, and sustain protocols for information sharing and communications. These protocols should assist with the coordination of transport decisions and options during a medical surge incident. These protocols also assist healthcare organizations understand the EMS disaster triage, transport, documentation, and CBRNE treatment methodologies during mass casualty incidents resulting in medical surge.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 3: The rapid expansion of the capacity and capability of the healthcare system.</div>
                <p>To provide the appropriate and timely clinical level of care in response to an incident that causes increased numbers (capacity) or special types of patients (capability) that overwhelm the day-to-day acute-care medical resources. This encompasses the appropriate decisions regarding patient care that require multi-agency coordination between healthcare organizations and incident management during medical surge operations.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 4: Provide State guidance and protocols on crisis standards of care.</div>
                <p>In order to enable a substantial change in routine healthcare operations including delivery of the optimal level of patient care for a pervasive (e.g., pandemic influenza) or catastrophic (e.g., earthquake, hurricane) disaster. The need for crisis standards is justified by specific circumstances and may or may not be triggered by the formal declaration of emergency, disaster, or public health emergency (with input from local, Healthcare Coalition, and regional authorities), in recognition that crisis operations will be in effect for a sustained period. If an emergency declaration is made, it changes the legal environment and enables specific legal and regulatory powers and protections for public health and healthcare providers concerning their actions and omissions associated with allocating and utilizing scarce medical resources and implementing crisis standards of care. This guidance provides a delineated continuum of care from normal operations to eventual crisis standards of care. The continuum involves the scarcity of all other resource options until it is no longer feasible to provide normal care, including strategies to reduce demand, optimize existing resources, and augment existing resources.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 5: Support healthcare organizations during evacuation and shelter in place operations.</div>
                <p>In which no warning or ample warning is received prior to the occurrence. This assists healthcare organizations with the safe and effective care of patients, use of equipment, and utilization of staff during relocation to another facility within a region or outside of the region in response to an incident. This includes the provision of assistance to healthcare organizations that have decided to shelter-in-place during the incident.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Medical Surge Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

###############################################################################################
    st.markdown("<h2 class='header'>Responder Safety and Health</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Develop, refine, and sustain processes.</div>
                <p>To assist healthcare organizations to provide the timely distribution of critical medication such as prophylaxis or immediate treatment for healthcare workers and their families during an exposure incident (e.g., CBRNE).</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Assist healthcare organizations with the ability to access the appropriate types of caches of Personal Protective Equipment (PPE).</div>
                <p>Needed for the safety of healthcare responders based on incident/event-specific conditions.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Responder Safety and Health Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

##############################################################################################

    st.markdown("<h2 class='header'>Volunteer Management</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Participate with volunteer planning.</div>
                <p>To assess the situations in which volunteers may be needed by healthcare organizations to determine the type and quantity of volunteers that may be used by healthcare organizations during a response. The coordinated planning involves medical considerations for the recruitment, identification, and training of volunteers that can support a healthcare organization response.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 2: Initiate the volunteer request process.</div>
                <p>So that prospective volunteers are mobilized in the appropriate health professional role for the healthcare organization’s response.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 3: Identify the process for allocating volunteers.</div>
                <p>That are needed simultaneously across several healthcare organizations. This process should include the placement of volunteers through the appropriate deployment channels and match the assignment of volunteers to the needs of the requesting healthcare organizations (i.e., based on volunteer availability).</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 4: Coordinate the release of volunteers.</div>
                <p>Based on evolving incident requirements or incident status. This includes coordination with the appropriate partner agencies to ensure provision of medical and mental/behavioral health support needed for the volunteers’ physical and mental well-being.</p>
            </div>
            <div class="column">
                <label class="label">Current Status:</label>
                <textarea class="text-input" placeholder="Enter current status"></textarea>
            </div>
            <div class="column">
                <label class="label">Status Score:</label>
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Volunteer Management Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# To display the content
show()