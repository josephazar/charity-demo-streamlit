import streamlit as st

def intro_text():
    # Introduction: AI and Nonprofits
    st.title("Artificial Intelligence in Nonprofits")
    st.write("""
    Artificial Intelligence (AI) has emerged as a transformative technology, revolutionizing industries and reshaping how we interact with various applications and services. Nonprofits are increasingly turning to AI to streamline operations, improve efficiency, and deliver better outcomes. 
    One of the key players in the AI space is **Microsoft Azure**, a comprehensive cloud computing platform offering a wide range of AI services.
    """)

    # Azure Cognitive Services section
    st.subheader("Azure Cognitive Services for Nonprofits")
    st.write("""
    **Azure Cognitive Services** provides pre-trained AI models and APIs that can be easily integrated into nonprofit applications. These services enable nonprofits to incorporate vision, speech, language, and decision-making capabilities without requiring in-depth AI expertise.
    """)

    # Use Cases for Azure Cognitive Services
    st.subheader("Use Cases")
    st.write("Here are a few ways nonprofits can leverage Azure Cognitive Services:")

    # Image recognition for organizational efficiency
    st.markdown("""
    - **Image Recognition for Organizational Efficiency**: 
    A wildlife conservation organization can use Azure's Computer Vision API to analyze and classify images from camera traps, identify species, track population numbers, and monitor biodiversity hotspots.
    """)

    # Multilingual content delivery
    st.markdown("""
    - **Multilingual Content Delivery**: 
    Nonprofits working in multicultural communities or international settings can use Azure Translator to deliver multilingual content. For instance, a healthcare nonprofit can provide educational materials in multiple languages, ensuring equal access to vital resources.
    """)

    # Highlight key Azure Cognitive Services
    st.subheader("Key Azure Cognitive Services")
    st.write("""
    - **Computer Vision**: Analyze images to extract valuable insights such as image recognition and content moderation.
    - **Text Analytics**: Extract insights from text data like social media posts, surveys, and feedback using sentiment analysis and key phrase extraction.
    - **Translator Text**: Bridge language barriers by translating text from one language to another, especially in international development or refugee support efforts.
    """)

    st.image("imgs/computervision.png", use_column_width=True)
    st.image("imgs/nlp.png", use_column_width=True)
    st.image("imgs/speech.png", use_column_width=True)
    st.image("imgs/knowledgemining.png", use_column_width=True)

    # Azure Machine Learning section
    st.subheader("Azure Machine Learning for Predictive Analytics")
    st.write("""
    **Azure Machine Learning** empowers nonprofits to build, deploy, and manage machine learning models. It enables data scientists and developers to collaborate on predictive models that can help nonprofits forecast outcomes and make data-driven decisions.
    """)

    # Predictive analytics for donor retention
    st.subheader("Use Case: Predictive Analytics for Donor Retention")
    st.write("""
    Nonprofits can use Azure Machine Learning to predict which donors are most likely to disengage, allowing for proactive outreach to retain valuable contributors.
    """)

    st.image("imgs/azureml.png", use_column_width=True)
    # Azure Machine Learning Features
    st.write("""
    - **Predictive Analytics**: Forecast outcomes like donor behavior or resource demand.
    - **Anomaly Detection**: Identify unusual patterns, such as disease outbreaks in healthcare nonprofits.
    - **Automated ML**: Automate building and deploying models, even without extensive data science expertise.
    """)

    # Azure Bot Services
    st.subheader("Azure Bot Services and OpenAI for Nonprofits")
    st.write("""
    **Azure Bot Services** allows nonprofits to develop intelligent chatbots that interact with users through various platforms. These chatbots can handle routine inquiries, improving efficiency and freeing up staff for other critical tasks.
    """)

    st.image("imgs/gptmodels.png", use_column_width=True)

    # Use cases for Azure Bot Services
    st.subheader("Use Case: Virtual Assistant for Program Enrollment")
    st.write("""
    A nonprofit offering educational programs can deploy a chatbot powered by Azure Bot Services to guide applicants through the registration process, answer frequently asked questions, and provide updates on program availability.
    """)

    # Highlight key uses for Azure Bot Services
    st.write("""
    - **Informational Support**: Provide immediate answers about programs, services, or events, reducing staff workload.
    - **Volunteer Engagement**: Manage volunteers by automating sign-ups, updates, and responses to queries.
    - **Fundraising Support**: Use chatbots to facilitate online donations and provide updates on campaigns.
    - **Event Registration**: Simplify the registration process for events and send reminders to attendees.
    """)

    # Summary: Leveraging Azure AI for Nonprofits
    st.subheader("Leveraging Azure AI for Nonprofits")
    st.write("""
    **Azure AI Services** offers affordable and user-friendly solutions for nonprofits with limited budgets, allowing them to harness the power of artificial intelligence and machine learning. 
    From analyzing text data to creating predictive models and interactive chatbots, nonprofits can streamline operations, improve decision-making, and maximize their impact. 
    By embracing these technologies, nonprofits can unlock new opportunities and achieve their mission more effectively.
    """)

    # Conclusion
    st.write("""
    In conclusion, AI is not only for large enterprises but also a game-changer for nonprofits. The future of nonprofits lies in how well they adapt to and leverage AI-driven tools, such as Microsoft Azure’s AI suite, to better serve their communities.
    """)

    # Final note
    st.image("https://via.placeholder.com/800x400.png?text=Thank+You+for+Joining", use_column_width=True)
