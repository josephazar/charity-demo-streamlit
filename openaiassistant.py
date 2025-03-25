def openaiassistant_intro():
    import streamlit as st
    import pandas as pd

    # Title
    st.title("Leveraging Azure OpenAI for Fundraising and Donor Discovery")

    st.image("imgs/openaiassistant.png", use_column_width=True)

    # Introduction Section
    st.header("Introduction")
    st.write("""
    In today’s competitive landscape, organizations constantly seek innovative solutions to improve their fundraising strategies. 
    Azure OpenAI assistant provides a new dimension in finding potential donors, automating repetitive tasks, 
    and offering personalized communication — all of which can drive greater fundraising success.
    """)

    # Benefits of Azure OpenAI
    st.header("How Azure OpenAI Assistant Can Benefit Fundraising")
    st.write("""
    Azure OpenAI Assistant, powered by advanced machine learning and AI models, can be a game-changer for non-profit organizations and fundraising teams. 
    It helps in the following areas:
    """)

    # Create bullet points for key benefits
    st.subheader("1. Donor Insights & Analysis")
    st.write("""
    Azure OpenAI can process vast amounts of data to uncover patterns in donor behavior. 
    By analyzing donor history, demographics, and interests, it can help fundraising teams identify high-potential donors and segments, ensuring efficient resource allocation.
    """)

    st.subheader("2. Personalized Outreach")
    st.write("""
    Personalized outreach has become a cornerstone of successful fundraising campaigns. 
    Azure OpenAI Assistant can generate customized messages for each donor based on their past interactions, preferences, and potential engagement level. 
    This enhances donor relationships and increases the likelihood of donation.
    """)

    st.subheader("3. Automating Routine Tasks")
    st.write("""
    Reaching out to donors, sending reminders, following up on pledges, and other repetitive tasks can take up a lot of time. 
    Azure OpenAI Assistant can automate these tasks through email generation, campaign follow-ups, and timely reminders, freeing up valuable time for fundraising teams to focus on strategy.
    """)

    st.subheader("4. Predictive Analytics for Donor Targeting")
    st.write("""
    With the power of AI, organizations can leverage predictive analytics to identify donors who are most likely to contribute to a campaign. 
    Azure OpenAI can help build donor profiles, predict donation amounts, and suggest optimal times to approach each donor, thus improving fundraising efficiency.
    """)

    st.subheader("5. Enhancing Data Management and Reporting")
    st.write("""
    Azure OpenAI Assistant can assist in the automation of data entry, cleaning, and analysis tasks, 
    making it easier for organizations to manage large donor databases. 
    It can also generate comprehensive reports, enabling fundraisers to monitor progress and refine their strategies.
    """)

    # Use Cases
    st.header("Use Cases of Azure OpenAI in Fundraising")
    st.write("""
    Azure OpenAI’s capabilities can be applied in a variety of fundraising scenarios:
    """)

    st.subheader("1. Major Donor Identification")
    st.write("""
    By using AI-driven data analysis, Azure OpenAI can help you identify major donor prospects based on their financial capabilities, past contributions, and philanthropic interests.
    """)

    st.subheader("2. Automated Grant Writing Assistance")
    st.write("""
    Azure OpenAI can assist in automating parts of the grant writing process, making it easier for non-profits to produce well-written proposals faster. 
    AI models can also suggest the most appropriate grants to apply for based on the organization's needs and focus areas.
    """)

    st.subheader("3. Event Fundraising")
    st.write("""
    From personalized event invites to post-event follow-up, Azure OpenAI can optimize every aspect of event fundraising. 
    It can track RSVPs, send reminders, and create tailored thank-you notes to boost donor engagement after events.
    """)

    # Call to Action
    st.header("Conclusion")
    st.write("""
    Azure OpenAI offers tremendous potential in streamlining fundraising efforts, enhancing donor engagement, and improving overall efficiency. 
    By leveraging AI for donor discovery, personalized outreach, and automating routine tasks, organizations can significantly increase their fundraising success.
    """)

    st.write("**Ready to take your fundraising efforts to the next level with Azure OpenAI?** Contact us to learn more!")

    st.subheader("Practical use case:")
    data = pd.read_csv("data/sample_donors_data_2159_with_professions.csv", sep=";")

    st.dataframe(data.head(30))

