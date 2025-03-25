import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import lifetimes as lf
from lifetimes.plotting import plot_frequency_recency_matrix
from lifetimes.plotting import plot_probability_alive_matrix
from lifetimes.plotting import plot_period_transactions
from lifetimes.plotting import plot_history_alive

def clv():
    st.title("Donor Lifetime Value Analysis")
    st.markdown("""
        Donor Lifetime Value (DLV) is the total worth of a donor to an organisation over the course of their relationship. 
        This metric is especially important to keep track of for acquiring new donors. It is generally more expensive to acquire new donors than to keep existing donors, so knowing the lifetime value and the costs associated with acquiring new donors is essential in order to build fundraising strategies with a positive ROI. 
    """)

    
    st.header("Dataset")
    st.markdown("The dataset used is the transactions data similar to the following: ")
    data = pd.read_csv("data/Charity_Donations_Dataset.csv")
    data['DonationDate'] = pd.to_datetime(data['DonationDate'])
    st.write(data.head(30))



    st.markdown("<h3 style='color:red'>RFM Calculation</h3>", unsafe_allow_html=True)

    LATESTDATE =   pd.to_datetime('2024-09-04')
    summary = lf.utils.summary_data_from_transaction_data(data, 'DonorID', 'DonationDate', 'DonationAmount' , observation_period_end=LATESTDATE)
    summary = summary.reset_index()
    rfm= data.groupby('DonorID').agg({'DonationDate': lambda InvoiceDate: (LATESTDATE - InvoiceDate.max()).days,
                                        'TransactionID': lambda num: len(num),
                                        'DonationAmount': lambda TotalSales: TotalSales.sum()})
    rfm.columns=['recency','frequency','monetary']
    st.dataframe(rfm.head(15))  
    st.markdown("""
        <hr style="border-top: 2px dashed gray;"/>
    """, unsafe_allow_html=True)                
    

    # Probability of still being alive
    st.markdown("<h4 style='color:blue'>Probability of still being alive</h4>", unsafe_allow_html=True)
    bgf = lf.BetaGeoFitter(penalizer_coef=0.01)
    bgf.fit(summary['frequency'], summary['recency'], summary['T'])
    summary['probability_alive'] = bgf.conditional_probability_alive(summary['frequency'], summary['recency'], summary['T'])
    st.markdown("""
        The probability of being alive is calculated based on the recency and frequency of a customer. 
                
        If a donor has done several donations (frequency) and the time between the first & last transactions is high (recency), then his/her probability of being alive is high. 
                
        Similarly, if a donor has less frequency (donated once or twice) and the time between first & last transaction is low (recency), then his/her probability of being alive is high.
    """)
    fig = plt.figure(figsize=(12,8))
    plot_probability_alive_matrix(bgf)
    st.pyplot(fig)

   # Customer Probability Histories
    st.markdown("<h4 style='color:blue'>Donor Probability Histories</h4>", unsafe_allow_html=True)
    st.markdown("""
        The below plot shows the probability of a customer being alive over time. 
        Given a customer transaction history, we can calculate their historical probability of being alive, according to our trained model. 
    """)
    id = "A1"
 
    st.markdown(f"Donor ID: {id}")
    days_since_birth = 600
    sp_trans = data.loc[data['DonorID'] == id]
    # convert datetime64 in sp_trans to date format
    sp_trans['DonationDate'] =  sp_trans['DonationDate'].dt.date
    
    fig = plt.figure(figsize=(12,8))
    plot_history_alive(bgf, days_since_birth, sp_trans, 'DonationDate')
    st.pyplot(fig)

    id = "B1"
    st.markdown(f"Donor ID: {id}")
    days_since_birth = 600
    sp_trans = data.loc[data['DonorID'] == id]
    # convert datetime64 in sp_trans to date format
    sp_trans['DonationDate'] =  sp_trans['DonationDate'].dt.date
    
    fig = plt.figure(figsize=(12,8))
    plot_history_alive(bgf, days_since_birth, sp_trans, 'DonationDate')
    st.pyplot(fig)

    id = "C1"
    st.markdown(f"Donor ID: {id}")
    days_since_birth = 600
    sp_trans = data.loc[data['DonorID'] == id]
    # convert datetime64 in sp_trans to date format
    sp_trans['DonationDate'] =  sp_trans['DonationDate'].dt.date
    
    fig = plt.figure(figsize=(12,8))
    plot_history_alive(bgf, days_since_birth, sp_trans, 'DonationDate')
    st.pyplot(fig)


    st.markdown("""
    <hr style="border-top: 2px dashed gray;"/>
                    """, unsafe_allow_html=True)  

    #Predict future transactions for 90 days
    st.markdown("<h4 style='color:blue'>Predict future donations for 365 days</h4>", unsafe_allow_html=True)
    #Predict future reservations for the next 90 days based on historical dataa
    t = 90
    summary['pred_num_txn'] = round(bgf.conditional_expected_number_of_purchases_up_to_time(t, summary['frequency'], summary['recency'], summary['T']),2)
    summary.sort_values(by='pred_num_txn', ascending=False).head(10).reset_index()

    # add pred_num_txn and probability_alive from summary to rfm using CustomerID  
    rfm = rfm.reset_index()
    print(rfm.head())
    print(summary.head())
    rfm = rfm.merge(summary[['DonorID', 'probability_alive', 'pred_num_txn']], 
                on='DonorID', 
                how='left')

    st.dataframe(rfm.sort_values(by='pred_num_txn', ascending=False).head(15).reset_index())

    st.markdown("""
    <hr style="border-top: 2px dashed gray;"/>
                    """, unsafe_allow_html=True)  
    # Estimating customer lifetime value
    st.markdown("<h3 style='color:red'>Estimating donor lifetime value</h3>", unsafe_allow_html=True)
    print(summary[['monetary_value', 'frequency']].corr())


    ggf = lf.GammaGammaFitter(penalizer_coef=0.001)
    ggf.fit(summary['frequency'], summary['monetary_value'])
    summary['exp_avg_sales'] = ggf.conditional_expected_average_profit(summary['frequency'],
                                    summary['monetary_value'])
        
    # Checking the expected average value and the actual average value in the data to make sure the values are good
    st.success(f"Actual Average Donations: {summary['monetary_value'].mean()}")
    st.success(f"Expected Average Donations for the next 365 days: {summary['exp_avg_sales'].mean()}")

    st.markdown("### Donor lifetime value (DLV) for the next 365 days")

    # Predicting Customer Lifetime Value for the next 12 months
    summary['predicted_clv_12months'] = ggf.customer_lifetime_value(bgf,
                                                                summary['frequency'],
                                                                summary['recency'],
                                                                summary['T'],
                                                                summary['monetary_value'],
                                                                time=12,     # lifetime in months
                                                                freq='D',   # frequency in which the data is present(T)
                                                                discount_rate=0.001) # discount rate
    rfm = rfm.merge(summary[['DonorID', 'exp_avg_sales', 'predicted_clv_12months']], 
                on='DonorID', 
                how='left')
    st.dataframe(rfm.sort_values(by='predicted_clv_12months', ascending=False).head(15).reset_index())


    # sorting by predicted_clv_3months ascending and displaying the top 10 customers
    st.markdown("Donors with lowest predicted DLV for the next 12 months:")
    st.dataframe(rfm.sort_values(by='predicted_clv_12months', ascending=True).head(10).reset_index())

    