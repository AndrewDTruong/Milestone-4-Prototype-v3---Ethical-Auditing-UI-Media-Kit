import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


#Headers
st.markdown("# 💧 This is an Interactive Simulation! 💧")
st.sidebar.markdown("# Page 3: Interactive Simulation💧")

def main():
    # Create sliders to control the parameters
    rainfall = st.slider('Average daily rainfall (in mm)', 0, 200, 50)
    litter = st.slider('Average daily litter (in kg)', 0, 200, 20)
    population_density = st.slider('Population density (people per sq km)', 0, 10000, 1000)
    industrial_waste = st.slider('Average daily industrial waste (in kg)', 0, 1000, 200)
    waste_treatment = st.slider('Waste treatment efficiency (%)', 0, 100, 50)

    # Calculate the level of pollution based on the parameters
    # This is a more complex model that includes non-linear relationships and interactions between parameters
    pollution = (np.sqrt(litter) + np.log1p(population_density) * 0.01 + np.power(industrial_waste, 2) * 0.1) / (np.sqrt(rainfall) + 1 + waste_treatment / 100)

    # Create a bar chart to represent the level of pollution
    plt.bar(['Pollution'], [pollution])
    plt.ylim(0, 100)  # Set the y-axis limits to a fixed range for consistency

    # Display the chart in Streamlit
    st.pyplot(plt)

    # Display some text explaining the results
    if pollution > 80:
        st.write('The pollution level is very high. Immediate action is required.')
    elif pollution > 60:
        st.write('The pollution level is high. Measures should be taken to reduce pollution.')
    elif pollution > 40:
        st.write('The pollution level is moderate. Keep an eye on the situation and take action if it worsens.')
    else:
        st.write('The pollution level is low. Keep up the good work!')

if __name__ == "__main__":
    main()