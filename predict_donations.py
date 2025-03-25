def predict_donations():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
    import seaborn as sns
    import numpy as np


    # Title and Introduction
    st.title("Using Machine Learning to Predict Charity Donations")
    st.write("""
    Many charities face uncertainty about whether individuals will donate based on limited data. 
    Machine learning can help analyze patterns in data, such as age, income, work class, and other factors, 
    to predict whether a person is likely to donate.
    """)

    # Load the dataset
    census_data = pd.read_csv('data/census.csv')


    # Show the first 20 rows of the dataset
    st.header("Understanding the Dataset")
    st.write("Here are the first 20 rows of the dataset, which contains information about individuals such as their age, education, work class, and income:")
    st.dataframe(census_data.head(20))

    # Preprocessing the Data
    st.write("The features of the dataset include the following:")
    st.write(census_data.columns.tolist())

    # Dropping rows with missing values for simplicity
    census_data = census_data.dropna()

    # Encoding categorical columns
    label_encoders = {}
    for column in ['workclass', 'education_level', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'income']:
        le = LabelEncoder()
        census_data[column] = le.fit_transform(census_data[column])
        label_encoders[column] = le

    # Feature and target separation
    X = census_data.drop('income', axis=1)  # Features
    y = census_data['income']  # Target variable (1: >50K, 0: <=50K)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Scaling numerical features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train a simple logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Generate predicted probabilities for the test data
    probabilities = model.predict_proba(X_test)[:, 1]  # Only taking the probability for class 1 (>50K)





    # Create a new dataframe with test set results and probabilities
    results_df = pd.DataFrame(X_test, columns=census_data.columns[:-1])
    results_df['probability_donation'] = probabilities
    results_df['donation_pred'] = np.where(probabilities >= 0.5, 1, 0)

    # Display Pie Chart
    st.header("Who is Likely to Donate?")
    st.write("Based on the model's predictions, we can estimate who is likely to donate:")
    donation_counts = results_df['donation_pred'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(donation_counts, labels=['No Donation', 'Likely to Donate'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    st.pyplot(plt)


    census_data = pd.read_csv('data/census.csv')
    # Dropping rows with missing values for simplicity
    census_data = census_data.dropna()

    # Encoding categorical columns
    label_encoders = {}
    for column in ['workclass', 'education_level', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'income']:
        le = LabelEncoder()
        census_data[column] = le.fit_transform(census_data[column])
        label_encoders[column] = le

    # Feature and target separation
    X = census_data.drop('income', axis=1)  # Features
    y = census_data['income']  # Target variable (1: >50K, 0: <=50K)

    # Scaling numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train a simple logistic regression model
    model = LogisticRegression()
    model.fit(X_scaled, y)

    census_data['probability_donation'] = model.predict_proba(X_scaled)[:, 1]

    # Decode the label-encoded columns for readability in output
    for column in label_encoders:
        if column != 'income':  # Skip income column since it's the target variable
            census_data[column] = label_encoders[column].inverse_transform(census_data[column])

    # Sorting the data by probability in descending and ascending order
    top_20_donors = census_data.sort_values(by='probability_donation', ascending=False).head(20)
    bottom_20_donors = census_data.sort_values(by='probability_donation', ascending=True).head(20)

    # Display top 20 and bottom 20 rows sorted by probability of donation
    st.header("Top 20 Likely Donors")
    st.dataframe(top_20_donors)

    st.header("Bottom 20 Likely Donors")
    st.dataframe(bottom_20_donors)

    # Focusing on individuals likely to donate (those with probability > 0.5)
    likely_donors = census_data[census_data['probability_donation'] > 0.5]

    # Separating numeric and categorical features
    numeric_features = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    categorical_features = ['workclass', 'education_level', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']

    # Analysis of Likely Donors
    st.header("Analysis of Likely Donors")

    # Plotting numeric features using box plots
    st.subheader("Numeric Feature Analysis (Box Plots)")
    for feature in numeric_features:
        st.subheader(f"Distribution of {feature} for Likely Donors")
        plt.figure(figsize=(8, 4))
        sns.boxplot(data=likely_donors, x=feature)
        plt.title(f"Distribution of {feature} for Likely Donors")
        st.pyplot(plt)

    # Displaying unique values for categorical features
    st.subheader("Categorical Feature Analysis (Unique Values)")
    for feature in categorical_features:
        st.subheader(f"Unique Values of {feature} for Likely Donors")
        unique_values = likely_donors[feature].unique()
        st.write(unique_values)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    By using machine learning, we can predict whether someone earns more than \$50K with a decent level of accuracy. 
    This helps charities target potential donors more effectively, ensuring their outreach is better directed.
    """)
