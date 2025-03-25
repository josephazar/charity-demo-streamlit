import streamlit as st
from intro import intro_text
from rfm import rfm
from clv import clv
from predict_donations import predict_donations
from public_data import public_data
from openaiassistant import openaiassistant_intro
from knowledgegraph import knowledge_graph
import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_image_in_sidebar(image_path, width=100):
    image_base64 = get_image_base64(image_path)
    html_str = f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{image_base64}' width='{width}' />
    </div>
    """
    st.sidebar.markdown(html_str, unsafe_allow_html=True)

def intro():
    import streamlit as st
    
    st.write("# Charity Exquitech Round Table")
    st.sidebar.success("Select a topic above.")

    st.markdown(
        """
        Welcome to the charity round table discussion on leveraging AI and machine learning services for fundraising and donor engagement.
        """
    )

    #put image imgs/uk_triumphs.jpeg
    st.image("imgs/uk_triumphs.jpeg", use_column_width=True)

    # table of contents
    st.write("## Agenda")
    st.write("1. Leveraging Azure AI & Machine Learning Services for Nonprofits")
    st.write("2. RFM Analysis")
    st.write("3. Donor Lifetime Value Analysis")
    st.write("4. Predicting Donations with Machine Learning")
    st.write("5. Public Data Mining for Charities")
    st.write("6. Leveraging Azure OpenAI for Fundraising and Donor Discovery")
    st.write("7. Knowledge Graphs for data modeling and insights")


page_names_to_funcs = {
    "—": intro,
    "Introduction": intro_text,
    "RFM Analysis": rfm,
    "Donor Lifetime Value Analysis": clv,
    "Predict Donations": predict_donations,
    "Public Data Mining": public_data,
    "OpenAI Assistant": openaiassistant_intro,
    "Knowledge Graphs": knowledge_graph,
}

display_image_in_sidebar("imgs/exquitech.png", width=100)
demo_name = st.sidebar.selectbox("Choose a topic", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

