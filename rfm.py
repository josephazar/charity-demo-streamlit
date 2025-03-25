import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import lifetimes as lf

def rfm():
    st.title("RFM Analysis")
     
    st.markdown("RFM analysis quantitatively groups donors based on the recency, frequency and monetary value of donations.")
    st.markdown("RFM analysis is used to inform marketing campaigns and targeting for promotions etc.") 


    st.header("Dataset")
    st.markdown("The dataset used is the transactions data similar to the following: ")
    data = pd.read_csv("data/Charity_Donations_Dataset.csv")
    data['DonationDate'] = pd.to_datetime(data['DonationDate'])
    st.write(data.head(30))

    st.markdown("""
        <hr style="border-top: 2px dashed gray;"/>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:red'>RFM Calculation</h3>", unsafe_allow_html=True)
    st.markdown("""
        RFM (Recency, Frequency, Monetary) is a marketing analysis tool used to identify a company's or an organization's best donors by using certain measures. 
        The RFM model is based on three quantitative factors:
        - Recency: How recently a donor has made a transaction
        - Frequency: How often a donor makes a transaction.
        - Monetary Value: How much money a donor spends .
        - Tenure (T): The length of time since a donor's first transaction. This helps in understanding the donor's lifecycle stage with the business. A higher value indicates a longer relationship with the donor.
                
        We will apply the RFM model to the dataset to segment donors based on these factors.
    """)



    #st.dataframe(summary.head(15))
    # get current date (today date now)
    LATESTDATE =     pd.to_datetime('2024-09-04')
    summary = lf.utils.summary_data_from_transaction_data(data, 'DonorID', 'DonationDate', 'DonationAmount' , observation_period_end=LATESTDATE)
    summary = summary.reset_index()
    rfm= data.groupby('DonorID').agg({'DonationDate': lambda InvoiceDate: (LATESTDATE - InvoiceDate.max()).days,
                                        'TransactionID': lambda num: len(num),
                                        'DonationAmount': lambda TotalSales: TotalSales.sum()})
    rfm.columns=['recency','frequency','monetary']
    st.dataframe(rfm.head(15))  

    # plot interquartile range for recency
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Recency", "Frequency", "Monetary"))
    fig.add_trace(go.Box(y=rfm['recency'], name='Recency'), row=1, col=1)
    fig.add_trace(go.Box(y=rfm['frequency'], name='Frequency'), row=1, col=2)
    fig.add_trace(go.Box(y=rfm['monetary'], name='Monetary'), row=1, col=3)
    fig.update_layout(height=600, width=1000, title_text="RFM interquartile range")
    st.plotly_chart(fig)

    st.markdown("""
        <hr style="border-top: 2px dashed gray;"/>
    """, unsafe_allow_html=True)
    # Write the above explanation in a markdown cell
    st.markdown("""
        <h3 style='color:red'>Donors Segmentation using Machine Learning</h3>
        <ul>
            <li><b>Regular Donors:</b>  Donations made recently. Regular purchases. High total purchase value. </li>
            <li><b>At-risk Donors:</b> Donations occurred a long time ago. Decreased transaction frequency. Spending has decreased. Lower total purchase value. Action: Re-engage through personalized emails, special attention</li>
            <li><b>High-value Donors:</b> Donations made recently. Regular Donations. High total donations value. </li>
        </ul>
    """, unsafe_allow_html=True)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    rfm_scaled = rfm[['recency', 'frequency', 'monetary']]
    rfm_scaled = scaler.fit_transform(rfm_scaled)
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=3, random_state=0).fit(rfm_scaled)
    rfm['cluster'] = kmeans.labels_

    # show clusters in 2D plot with PCA 
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    rfm['pca1'] = pca.fit_transform(rfm_scaled)[:,0]
    rfm['pca2'] = pca.fit_transform(rfm_scaled)[:,1]

    # Assuming rfm dataframe and clusters are defined
    fig = go.Figure()

    # Iterate through each cluster and create a scatter trace
    for cluster in rfm['cluster'].unique():
        fig.add_trace(go.Scatter(
            x=rfm[rfm['cluster'] == cluster]['pca1'], 
            y=rfm[rfm['cluster'] == cluster]['pca2'], 
            mode='markers', 
            marker=dict(size=45),  # Adjust the size of the points here
            name=f'Cluster {cluster}'
        ))

    # Update the layout for the figure
    fig.update_layout(
        height=600, 
        width=1000, 
        title_text="RFM Clusters"
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)


    # plot the clusters
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Recency", "Frequency", "Monetary"))
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 0]['recency'], name='Cluster 0'), row=1, col=1)
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 1]['recency'], name='Cluster 1'), row=1, col=1)
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 2]['frequency'], name='Cluster 2'), row=1, col=1)

    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 0]['frequency'], name='Cluster 0'), row=1, col=2)
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 1]['frequency'], name='Cluster 1'), row=1, col=2)
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 2]['frequency'], name='Cluster 2'), row=1, col=2)

    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 0]['monetary'], name='Cluster 0'), row=1, col=3)
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 1]['monetary'], name='Cluster 1'), row=1, col=3)
    fig.add_trace(go.Box(y=rfm[rfm['cluster'] == 2]['monetary'], name='Cluster 2'), row=1, col=3)

    fig.update_layout(height=600, width=1000, title_text="Clusters")
    st.plotly_chart(fig)

