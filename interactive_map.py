import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim


#Headers
st.markdown("# 💧 These are locations of storm drains in Downtown San Jose 💧")
st.sidebar.markdown("# Page 2: 💧 Stormdrains in Downtown San Jose💧")

# Read the location data from the Excel file
df = pd.read_excel('locations.xlsx')

# Create a text box for street name input
street_name = st.text_input('Enter a stormdrain location based on the chart below:')

# Filter the DataFrame based on the street name
filtered_df = df[df['Location'].str.contains(street_name, case=False, na=False)]

# Display the filtered DataFrame
st.write(filtered_df)

st.write("# This is a map of Downtown San Jose")

# Create a map centered around the first location in the filtered DataFrame
if not filtered_df.empty:
    # If a street name has been entered, use a higher zoom level
    if street_name:
        zoom_start = 15
    else:
        zoom_start = 10

    m = folium.Map(location=[filtered_df.iloc[0]['Latitude'], filtered_df.iloc[0]['Longitude']], zoom_start=zoom_start)

    # Add a marker for each location in the filtered DataFrame
    for index, row in filtered_df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Location'],
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    # Display the map in Streamlit
    folium_static(m)

# Add a button for reporting issues
if st.button('Report an Issue'):
    # Display a form for entering issue details
    issue = st.text_input('Please describe the issue:')
    email = st.text_input('Enter your email (optional):')
    if st.button('Submit Issue'):
        # Handle the issue report here
        # For example, you could send an email, write to a database, etc.
        st.write('Thank you for reporting this issue.')