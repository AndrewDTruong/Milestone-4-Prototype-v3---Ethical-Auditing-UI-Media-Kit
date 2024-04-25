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

# Create a map centered around the first location in the file
m = folium.Map(location=[df.iloc[0]['Latitude'], df.iloc[0]['Longitude']], zoom_start=10)

# Add a marker for each location in the file
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Location'],
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)

# Display the map in Streamlit
folium_static(m)