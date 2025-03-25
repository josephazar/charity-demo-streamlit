def public_data():
    import pandas as pd
    import geopandas as gpd
    from shapely.geometry import Point
    import contextily as ctx
    import matplotlib.pyplot as plt
    import streamlit as st


    # Set page title
    st.title("Using Contextual Information and Data Enrichment for Fundraising")

    # Introduction section
    st.markdown("""
    ### Introduction

    Data analytics and publicly available information can be powerful tools for planning successful fundraising events. By leveraging data about house prices, crime rates, and housing transactions, we can gain insights into which areas might have higher potential for fundraising.

    For example, high house prices might indicate wealthier areas, while regions with higher house sales could signal areas of growth or economic activity. Conversely, crime rates can help identify areas to avoid or where more cautious planning is required. By combining these data points with geographical information, we can make data-driven decisions about where to focus our efforts for fundraising events.
    """)

    # Load the data
    st.markdown("### Dataset Overview")
    # Assuming `merged_data` is the dataset with long, lat, and aggregated information

    @st.cache_data
    def load_data():
        # Load your dataset here
        data = pd.read_csv("data/Housing_Data_with_Latitude_and_Longitude.csv")  # Use the dataset you have saved
        return data

    merged_data = load_data()

    # Show top 20 rows
    st.write("Here are the top 20 rows of the dataset:")
    st.dataframe(merged_data.head(20))

    # Step 1: Aggregate the dataset as before
    aggregated_data = merged_data.groupby('area').agg({
        'average_price': 'mean',
        'houses_sold': 'sum',
        'no_of_crimes': 'sum',
        'Longitude': 'first',
        'Latitude': 'first'
    }).reset_index()

    st.markdown("### Aggregated Data Overview")
    st.write("The table below aggregates the data by area, showing average house prices, total houses sold, and the number of crimes.")
    st.dataframe(aggregated_data)

    # Step 2: Convert the aggregated data to a GeoDataFrame
    st.markdown("### Visualizing the Data on Maps")

    # Create a GeoDataFrame from the aggregated data
    geometry = [Point(xy) for xy in zip(aggregated_data['Longitude'], aggregated_data['Latitude'])]
    geo_df = gpd.GeoDataFrame(aggregated_data, geometry=geometry)

    # Function to plot maps
    def plot_map(geo_df, column, title, cmap='coolwarm', label='Value'):
        fig, ax = plt.subplots(figsize=(12, 8))
        geo_df = geo_df.set_crs(epsg=4326).to_crs(epsg=3857)
        geo_df.plot(column=column, cmap=cmap, ax=ax, legend=True, markersize=50)
        ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)
        ax.set_axis_off()
        plt.title(title, fontsize=18)
        colorbar = ax.get_figure().get_axes()[1]
        colorbar.set_ylabel(label, rotation=270, labelpad=20, fontsize=15)
        st.pyplot(fig)

    # Map 1: Average House Price
    st.markdown("#### Map 1: Average House Prices by Area")
    st.write("This map shows the average house prices in different areas. Areas with higher average prices might indicate wealthier regions where fundraising could be more successful.")
    plot_map(geo_df, column='average_price', title='Average House Prices in London Areas', cmap='coolwarm', label='Average Price')

    # Map 2: Total Houses Sold
    st.markdown("#### Map 2: Total Houses Sold by Area")
    st.write("This map shows the total number of houses sold in each area. Areas with high house sales might indicate growing neighborhoods where there is economic activity, making them potential targets for fundraising efforts.")
    plot_map(geo_df, column='houses_sold', title='Total Houses Sold in London Areas', cmap='Blues', label='Houses Sold')

    # Map 3: Total Number of Crimes
    st.markdown("#### Map 3: Total Number of Crimes by Area")
    st.write("This map shows the total number of crimes reported in each area. Areas with higher crime rates might need more caution in planning fundraising events.")
    plot_map(geo_df, column='no_of_crimes', title='Total Number of Crimes in London Areas', cmap='Reds', label='Number of Crimes')
    # Adding CSV download functionality
    st.markdown("### Download Aggregated Data")
    st.write("You can download the aggregated data by area as a CSV file for further analysis.")

    # Convert aggregated data to CSV format
    csv_data = aggregated_data.to_csv(index=False)

    # Streamlit download button
    st.download_button(
        label="Download Aggregated Data as CSV",
        data=csv_data,
        file_name='aggregated_housing_data.csv',
        mime='text/csv'
    )
    # Conclusion
    st.markdown("""
    ### Conclusion

    Using contextual information such as house prices, sales data, and crime rates can provide valuable insights for planning fundraising activities. By understanding the socioeconomic dynamics of different areas, we can strategically select the locations that have higher potential for successful fundraising efforts.
    """)
