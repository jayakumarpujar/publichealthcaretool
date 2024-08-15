import streamlit as st

def show():
    
    st.markdown("<h2 class='header'><b>Community Preparedness</b></h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Determine risks to the health of the jurisdiction.</div>
                <p>Identify the potential hazards, vulnerabilities, and risks in the community that relate to the jurisdiction’s public health, medical, and mental/behavioral health systems, the relationship of those risks to human impact, interruption of public health, medical, and mental/behavioral health services, and the impact of those risks on the jurisdiction’s public health, medical, and mental/behavioral health infrastructure.</p>
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
                <div class="subheader"><b>Function 2:</b> Build community partnerships to support health preparedness.</div>
                <p>Identify and engage with public and private community partners who can do the following:</p>
                <ul>
                    <li>Assist with the mitigation of identified health risks</li>
                    <li>Be integrated into the jurisdiction’s all-hazards emergency plans with defined community roles and responsibilities related to the provision of public health, medical, and mental/behavioral health as directed under the Emergency Support Function #8 definition at the state or local level.</li>
                </ul>
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
                <div class="subheader"><b>Function 3:</b> Engage with community organizations to foster public health, medical, and mental/behavioral health social networks.
                Engage with community organizations to foster social connections that assure public health, medical and mental/behavioral health services in a community before, during, and after an incident.</div>
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
                <div class="subheader"><b>Function 4:</b> Coordinate training or guidance to ensure community engagement in preparedness efforts.</div>
                <p>Coordinate with emergency management, community organizations, businesses, and other partners to provide public health preparedness and response training or guidance to community partners for the specific risks identified in the jurisdictional risk assessment.</p>
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
                <div class="subheader"><b>Community Preparedness Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
###########################################################################################

    st.markdown("<h2 class='header'>Community Recovery</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Identify and monitor public health, medical, and mental/behavioral health system recovery needs.</div>
                <p>Assess the impact of an incident on the public health system in collaboration with the jurisdictional government and community and faith-based partners, in order to determine and prioritize the public health, medical, or mental/behavioral health system recovery needs. This function addresses the intent of National Health Security Strategy Outcome 8 that there should be a collaborative effort within a jurisdiction that results in the identification of public health, medical, and mental/behavioral assets, facilities, and other resources which either need to be rebuilt after an incident or which can be used to guide post-incident reconstitution activities.</p>
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
                <div class="subheader"><b>Function 2:</b> Coordinate community public health, medical, and mental/behavioral health system recovery operations.</div>
                <p>Facilitate interaction among community and faith-based organizations (e.g., businesses and non-governmental organizations) to build a network of support services which will minimize any negative public health effects of the incident. This function addresses the National Health Security Strategy Objective 8 outcome recommendation that jurisdictions should have an integrated plan as to how post-incident public health, medical, and mental/behavioral services can be coordinated with organizations responsible for community restoration.</p>
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
                <div class="subheader"><b>Function 3:</b> Implement corrective actions to mitigate damages from future incidents.</div>
                <p>Incorporate observations from the current incident to describe actions needed to return to a level of public health, medical, and mental/behavioral health system function at least comparable to pre-incident levels or improved levels where appropriate. Document these items in a written after action report and improvement plan, and implement those corrective actions that are within the purview of public health. This function addresses the intent of the National Health Security Strategy Outcome 8 recommendation that jurisdictions should have a monitoring and evaluation plan for recovery efforts.</p>
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
                <div class="subheader"><b>Community Recovery Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

####################################################################################

    st.markdown("<h2 class='header'>Emergency Operations Coordination</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Conduct preliminary assessment to determine need for public activation.</div>
                <p>Define the public health impact of an event or incident and gather subject matter experts to make recommendations on the need for, and scale of, incident command operations.</p>
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
                <div class="subheader"><b>Function 2:</b> Activate public health emergency operations</div>
                <p>In preparation for an event, or in response to an incident of public health significance, engage resources (e.g., human, technical, physical space, and physical assets) to address the incident or event in accordance with the National Incident Management System and consistent with jurisdictional standards and practices.</p>
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
                <div class="subheader"><b>Function 3:</b> Develop incident response strategy</div>
                <p>Produce or provide input to an Incident Commander or Unified Command approved, written Incident Action Plan, as dictated by the incident, containing objectives reflecting the response strategy for managing Type 1, Type 2, and Type 3 events or incidents, as described in the National Incident Management System, during one or more operational periods.</p>
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
                <div class="subheader"><b>Function 4:</b> Manage and sustain the public health response</div>
                <p>Direct ongoing public health emergency operations to sustain the public health and medical response for the duration of the response, including multiple operational periods and multiple concurrent responses.</p>
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
                <div class="subheader"><b>Function 5:</b> Demobilize and evaluate public health emergency operations</div>
                <p>Release and return resources that are no longer required by the event or incident to their pre-ready state and conduct an assessment of the efforts, resources, actions, leadership, coordination, and communication utilized during the incident for the purpose of identifying and implementing continuous improvement activities.</p>
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
                <div class="subheader"><b>Emergency Operations Coordination Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

######################################################################################

    st.markdown("<h2 class='header'>Emergency Public Info and Warning</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Activate the emergency public information system</div>
                <p>Notify and assemble key public information personnel and potential spokespersons, which were identified prior to an incident, to provide information to the public during an incident.</p>
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
                <div class="subheader"><b>Function 2:</b> Determine the need for a joint public information system</div>
                <p>Determine the need for, and scale of, a joint public information system, including if appropriate, activation of a Joint Information Center within the public health agency. Participate with other jurisdictional Joint Information Centers in order to combine information sharing abilities and coordinate messages.</p>
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
                <div class="subheader"><b>Function 3:</b> Establish and participate in information system operations</div>
                <p>Monitor jurisdictional media, conduct press briefings, and provide rumor control for media outlets, utilizing a National Incident Management System compliant framework for coordinating incident-related communications.</p>
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
                <div class="subheader"><b>Function 4:</b> Establish avenues for public interaction and information exchange</div>
                <p>Provide methods for the public to contact the health department with questions and concerns through call centers, help desks, hotlines, social media, web chat or other communication platforms.</p>
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
                <div class="subheader"><b>Function 5:</b> Issue public information, alerts, warnings, and notifications</div>
                <p>Utilizing crisis and emergency risk communication principles, disseminate critical health and safety information to alert the media, public, and other stakeholders to potential health risks and reduce the risk of exposure to ongoing and potential hazards.</p>
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
                <div class="subheader"><b>Emergency Public Info and Warning Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

#####################################################################################
    st.markdown("<h2 class='header'>Fatality Management</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Determine role for public health in fatality management.</div>
                <p>Coordinate with the lead jurisdictional authority (e.g., coroner, medical examiner, sheriff, or other agent) to identify the roles and responsibilities of jurisdictional public health entities in fatality management activities.</p>
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
                <div class="subheader"><b>Function 2:</b> Activate public health fatality management operations.</div>
                <p>Facilitate access to resources (e.g., human, record keeping, and physical space) to address the fatalities from an incident in accordance with public health jurisdictional standards and practices and as requested by lead jurisdictional authority.</p>
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
                <div class="subheader"><b>Function 3:</b> Assist in the collection and dissemination of ante mortem data.</div>
                <p>Assist, if requested, the lead jurisdictional authority and jurisdictional and regional partners to gather and disseminate ante mortem data through a Family Assistance Center Model or other mechanism.</p>
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
                <div class="subheader"><b>Function 4:</b> Participate in survivor mental/behavioral health services.</div>
                <p>Coordinate with the lead jurisdictional authority and jurisdictional and regional partners to support the provision of non-intrusive, culturally sensitive mental/behavioral health support services to family members of the deceased, incident survivors, and responders, if requested.</p>
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
                <div class="subheader"><b>Function 5:</b> Participate in fatality processing and storage operations.</div>
                <p>Assist the lead jurisdictional authority and partners in ensuring that human remains and associated personal effects are safely recovered, processed, transported, tracked, stored, and disposed of or released to authorized person(s), if requested.</p>
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
                <div class="subheader"><b>Fatality Management Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

#########################################################################################

    st.markdown("<h2 class='header'>Information Sharing</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Identify stakeholders to be incorporated into information flow.</div>
                <p>Identify stakeholders within the jurisdiction across public health, medical, law enforcement, and other disciplines that should be included in information exchange, and identify inter-jurisdictional public health stakeholders that should be included in information exchange. Determine the levels of security clearance needed for information access across and between these stakeholders.</p>
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
                <div class="subheader"><b>Function 2:</b> Identify and develop rules and data elements for sharing.</div>
                <p>Define minimum requirements for information sharing for the purpose of developing and maintaining situational awareness. Minimum requirements include the following elements:
                    <ul>
                        <li>When data should be shared</li>
                        <li>Who is authorized to receive data</li>
                        <li>Who is authorized to share data</li>
                        <li>What types of data can be shared</li>
                        <li>Data use and re-release parameters</li>
                        <li>What data protections are sufficient</li>
                        <li>Legal, statutory, privacy, and intellectual property considerations</li>
                    </ul>
                </p>
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
                <div class="subheader"><b>Function 3:</b> Exchange information to determine a common operating picture.</div>
                <p>Share information (both send and receive) within the public health agency, with other identified intra-jurisdictional stakeholders, and with identified inter-jurisdictional stakeholders, following available national standards for data vocabulary, storage, transport, security, and accessibility.</p>
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
                <div class="subheader"><b>Information Sharing Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

########################################################################################

    st.markdown("<h2 class='header'>Mass Care</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Determine public health role in mass care operations.</div>
                <p>In conjunction with Emergency Support Function #6, #8, and #11 partners, emergency management, and other partner agencies, determine the jurisdictional public health roles and responsibilities in providing medical care, health services, and shelter services during a mass care incident.</p>
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
                <div class="subheader"><b>Function 2:</b> Determine mass care needs of the impacted population.</div>
                <p>In conjunction with Emergency Support Function #6, #8, and #11 partners, emergency management and other partner agencies, determine the public health, medical, mental/behavioral health needs of those impacted by the incident.</p>
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
                <div class="subheader"><b>Function 3:</b> Coordinate public health, medical, and mental/behavioral health services.</div>
                <p>Coordinate with partner agencies to provide access to health services, medication and consumable medical supplies (e.g., hearing aid batteries and incontinence supplies), and durable medical equipment for the impacted population.</p>
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
                <div class="subheader"><b>Function 4:</b> Monitor mass care population health.</div>
                <p>Monitor ongoing health-related mass care support, and ensure health needs continue to be met as the incident response evolves.</p>
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
                <div class="subheader"><b>Mass Care Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

######################################################################################

    st.markdown("<h2 class='header'>Medical Countermeasure Dispensing</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Identify and initiate medical countermeasure dispensing strategies.</div>
                <p>Notify and coordinate with partners to identify roles and responsibilities consistent with the identified agent or exposure and within a time frame appropriate to the incident.</p>
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
                <div class="subheader"><b>Function 2:</b> Receive medical countermeasures.</div>
                <p>Identify dispensing sites and/or intermediary distribution sites and prepare these modalities to receive medical countermeasures in a time frame applicable to the agent or exposure.</p>
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
                <div class="subheader"><b>Function 3:</b> Activate dispensing modalities.</div>
                <p>Ensure resources (e.g., human, technical, and space) are activated to initiate dispensing modalities that support a response requiring the use of medical countermeasures for prophylaxis and/or treatment.</p>
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
                <div class="subheader"><b>Function 4:</b> Dispense medical countermeasures to identified population.</div>
                <p>Provide medical countermeasures to individuals in the target population, in accordance with public health guidelines and/or recommendations for the suspected or identified agent or exposure.</p>
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
                <div class="subheader"><b>Function 5:</b> Report adverse events.</div>
                <p>Report adverse event notifications (e.g., negative medical countermeasure side effects) received from an individual, healthcare provider, or other source.</p>
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
                <div class="subheader"><b>Medical Countermeasure Dispensing Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

########################################################################################

    st.markdown("<h2 class='header'>Medical Materiel Management & Distribution</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Direct and activate medical materiel management and distribution.</div>
                <p>Coordinate logistical operations and medical materiel requests when an incident exceeds the capacity of the jurisdiction's normal supply chain, including the support and activation of staging operations to receive and/or transport additional medical materiel. This should be accomplished at the request of the incident commander and in coordination with jurisdictional emergency management.</p>
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
                <div class="subheader"><b>Function 2:</b> Acquire medical materiel.</div>
                <p>Obtain medical materiel from jurisdictional caches and request materiel from jurisdictional, private, regional, or federal partners, as necessary.</p>
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
                <div class="subheader"><b>Function 3:</b> Maintain updated inventory management and reporting system.</div>
                <p>Maintain inventory system for the jurisdiction's medical materiel for the life of the materiel, including acquisition, receipt, storage, transport, recovery, disposal, and return or loss.</p>
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
                <div class="subheader"><b>Function 4:</b> Establish and maintain security.</div>
                <p>In coordination with emergency management and jurisdictional law enforcement, secure personnel and medical materiel during all phases of transport and ensure security for receiving site and distribution personnel.</p>
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
                <div class="subheader"><b>Function 5:</b> Distribute medical materiel.</div>
                <p>Distribute medical materiel to modalities (e.g., dispensing sites, treatment locations, intermediary distribution sites, and/or closed sites).</p>
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
                <div class="subheader"><b>Function 6:</b> Recover medical materiel and demobilize distribution operations.</div>
                <p>Recover remaining medical materiel in accordance with jurisdictional policies and federal regulations and demobilize distribution operations as required by incident needs.</p>
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
                <div class="subheader"><b>Medical Materiel Management & Distribution Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

###################################################################################################

    st.markdown("<h2 class='header'>Medical Surge</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader"><b>Function 1:</b> Assess the nature and scope of the incident.</div>
                <p>In conjunction with jurisdictional partners, coordinate with the jurisdiction's healthcare response through the collection and analysis of health data (e.g., from emergency medical services, fire service, law enforcement, public health, medical, public works, utilization of incident command system, mutual aid agreements, and activation of Emergency Management Assistance Compact agreements) to define the needs of the incident and the available healthcare staffing and resources.</p>
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
                <div class="subheader"><b>Function 2:</b> Support activation of medical surge.</div>
                <p>Support healthcare coalitions and response partners in the expansion of the jurisdiction's healthcare system (includes additional staff, beds, and equipment) to provide access to additional healthcare services (e.g., call centers, alternate care systems, emergency medical services, emergency department services, and inpatient services) in response to the incident.</p>
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
                <div class="subheader"><b>Function 3:</b> Support jurisdictional medical surge operations.</div>
                <p>In conjunction with health care coalitions and response partners, coordinate healthcare resources in conjunction with response partners, including access to care and medical service, and the tracking of patients, medical staff, equipment and supplies (from intra or interstate and federal partners, if necessary) in quantities necessary to support medical response operations.</p>
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
                <div class="subheader"><b>Function 4:</b> Support demobilization of medical surge operations.</div>
                <p>In conjunction with other jurisdictional partners, return health care system to pre-incident operations by incrementally decreasing surge staffing, equipment needs, alternate care facilities, and other systems, and transition patients from acute care services into their pre-incident medical environment or other applicable medical setting.</p>
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
                <div class="subheader"><b>Medical Surge Score</b></div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

##############################################################################################

    st.markdown("<h2 class='header'>Non-Pharmaceutical Interventions</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Engage partners and identify factors that impact non-pharmaceutical interventions.</div>
                <p>Identify and engage with health partners, government agencies, and community sectors (e.g., education, social services, faith-based, and business/industry) to identify the community factors that affect the ability to recommend and implement non-pharmaceutical interventions.</p>
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
                <div class="subheader">Function 2: Determine non-pharmaceutical interventions.</div>
                <p>Work with subject matter experts (e.g., epidemiology, laboratory, surveillance, medical, chemical, biological, radiological, social service, emergency management, and legal) to recommend the non-pharmaceutical intervention(s) to be implemented.</p>
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
                <div class="subheader">Function 3: Implement non-pharmaceutical interventions.</div>
                <p>Coordinate with health partners, government agencies, community sectors (e.g., education, social services, faith-based, and business), and jurisdictional authorities (e.g., law enforcement, jurisdictional officials, and transportation) to make operational, and if necessary, enforce, the recommended non-pharmaceutical intervention(s).</p>
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
                <div class="subheader">Function 4: Monitor non-pharmaceutical interventions.</div>
                <p>Monitor the implementation and effectiveness of interventions, adjust intervention methods and scope as the incident evolves, and determine the level or point at which interventions are no longer needed.</p>
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
                <div class="subheader">Non-Pharmaceutical Interventions Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

##########################################################################################

    st.markdown("<h2 class='header'>Public Health Laboratory Testing</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Manage laboratory activities.</div>
                <p>Manage and coordinate communications and resource sharing with the jurisdiction's network of human, food, veterinary, and environmental testing laboratory efforts in order to respond to chemical, biological, radiological, nuclear, explosive, and other public health threats.</p>
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
                <div class="subheader">Function 2: Perform sample management.</div>
                <p>Implement LRN-established protocols and procedures where available and applicable [and other mandatory protocols such as those for the International Air Transport Association (IATA) and the U.S. Department of Transportation (DOT)] for sample collection, handling, packaging, processing, transport, receipt, storage, retrieval, and disposal.</p>
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
                <div class="subheader">Function 3: Conduct testing and analysis for routine and surge capacity.</div>
                <p>Perform, or coordinate with the applicable lead agency, testing of chemical, biological, radiological, nuclear, and explosive samples, utilizing CDC-established protocols and procedures (e.g., LRN), where available and applicable, to provide detection, characterization and confirmatory testing to identify public health incidents. This testing may include clinical, food, and environmental samples.</p>
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
                <div class="subheader">Function 4: Support public health investigations.</div>
                <p>Provide analytical and investigative support to epidemiologists, healthcare providers, law enforcement, environmental health, food safety, and poison control efforts to help determine cause and origin of, and definitively characterize, a public health incident.</p>
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
                <div class="subheader">Function 5: Report results.</div>
                <p>Provide notification of laboratory results and send laboratory data to public health officials, healthcare providers, and other institutions, agencies, or persons as permitted by all applicable laws, rules, and regulations.</p>
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
                <div class="subheader">Public Health Laboratory Testing Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

#########################################################################################################

    st.markdown("<h2 class='header'>Public Health Surveillance and Epidemiology</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Conduct public health surveillance and detection.</div>
                <p>Conduct ongoing systematic collection, analysis, interpretation, and management of public health-related data to verify a threat or incident of public health concern, and to characterize and manage it effectively through all phases of the incident.</p>
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
                <div class="subheader">Function 2: Conduct public health and epidemiological investigations.</div>
                <p>Identify the source of a case or outbreak of disease, injury, or exposure and its determinants in a population (e.g., time, place, person, disability status, living status, or other indices) to coordinate and report the summary results of the analysis to jurisdictional and federal partners, as appropriate.</p>
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
                <div class="subheader">Function 3: Recommend, monitor, and analyze mitigation actions.</div>
                <p>Recommend, implement, or support public health interventions that contribute to the mitigation of a threat or incident as well as monitor the effectiveness of the interventions.</p>
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
                <div class="subheader">Function 4: Improve public health surveillance and epidemiological investigation systems.</div>
                <p>Assess internal agency surveillance and epidemiologic investigation both during and after an incident and implement quality improvement measures that are within jurisdictional public health agency control.</p>
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
                <div class="subheader">Public Health Surveillance and Epi. Score</div>
            </div>
            <div class="column">
                <textarea class="text-output" placeholder="Not Calculated" disabled></textarea>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

##############################################################################################

    st.markdown("<h2 class='header'>Responder Safety and Health</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Identify responder safety and health risks.</div>
                <p>Assist in the identification of the medical and mental/behavioral health risks (routine and incident-specific) to responders and communicate this information prior to, during, and after an incident.</p>
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
                <div class="subheader">Function 2: Identify safety and personal protective needs.</div>
                <p>Coordinate with occupational health and safety and other subject matter experts, based on incident-specific conditions, to determine the necessary personal protective equipment, medical countermeasures, mental/behavioral health support services and other items and services, and distribute these, as applicable, to protect the health of public health responders.</p>
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
                <div class="subheader">Function 3: Coordinate with partners to facilitate risk-specific safety and health training.</div>
                <p>In conjunction with partner agencies, facilitate the inclusion of risk-specific physical safety, mental/behavioral health, and personal protective equipment topics (based on jurisdictional risk assessment) into public health responder training to prepare responders for the incident.</p>
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
                <div class="subheader">Function 4: Monitor responder safety and health actions.</div>
                <p>Conduct or participate in monitoring and surveillance activities to identify any potential adverse health effects of public health responders.</p>
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

####################################################################################

    st.markdown("<h2 class='header'>Volunteer Management</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="input-container">
        <div class="row">
            <div class="column">
                <div class="subheader">Function 1: Coordinate volunteers.</div>
                <p>Recruit, identify, and train volunteers who can support the public health agency's response to an incident. Volunteers identified prior to an incident must be registered with the Emergency System for Advance Registration of Volunteer Health Professionals (ESAR-VHP), Medical Reserve Corps, or other pre-identified partner groups (e.g., Red Cross or Community Emergency Response Teams).</p>
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
                <div class="subheader">Function 2: Notify volunteers.</div>
                <p>At the time of an incident, utilize redundant communication systems where available (e.g., reverse 911 or text messaging) to request that prospective volunteers participate in the public health agency's response.</p>
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
                <div class="subheader">Function 3: Organize, assemble, and dispatch volunteers.</div>
                <p>Coordinate the assignment of public health agency volunteers to public health, medical, mental/behavioral health, and non-specialized tasks as directed by the incident, including the integration of inter-jurisdictional (e.g., cross-border or federal) volunteer response teams into the jurisdictional public health agency's response efforts.</p>
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
                <div class="subheader">Function 4: Demobilize volunteers.</div>
                <p>Release volunteers based on evolving incident requirements or incident-action plan and coordinate with partner agencies to assure provision of any medical and mental/behavioral health support needed for volunteers to return to pre-incident status.</p>
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
