import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static

#Headers
st.markdown("# 💧 These are locations of storm drains in Downtown San Jose 💧")
st.sidebar.markdown("# Page 2: 💧 Stormdrains in Downtown San Jose💧")


# Read the location data from the Excel file
df = pd.read_excel('locations.xlsx')

# Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Write the DataFrame to Streamlit to check it
st.write(df)

st.write("# This is a map of Downtown San Jose")

# Create a text box for street name input
street_name = st.text_input('Enter a street name:')

# Filter the DataFrame based on the street name
filtered_df = df[df['Location'].str.contains(street_name, case=False, na=False)]

# Display the filtered DataFrame
st.write(filtered_df)

# Create a map centered around the first location in the filtered DataFrame
if not filtered_df.empty:
    m = folium.Map(location=[filtered_df.iloc[0]['Latitude'], filtered_df.iloc[0]['Longitude']], zoom_start=10)

    # Add a marker for each location in the filtered DataFrame
    for index, row in filtered_df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Location'],
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    # Display the map in Streamlit
    folium_static(m)