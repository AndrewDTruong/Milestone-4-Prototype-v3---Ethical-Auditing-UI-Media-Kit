import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.markdown("# 🌊 🗑️ Welcome to EcoFlow 🌊 🗑️")
st.sidebar.markdown("# 🌊 🗑️ Ecoflow 🌊 🗑️")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_image = load_lottieurl("https://lottie.host/38af8faf-9de3-4c03-8d64-ff06a0c8aafd/vikFwfRXdM.json")

cols = st.columns(2)

with cols[1]:
    st_lottie(lottie_image, speed=1, width=450, height=350, key="initial")
    for _ in range(100): 
        st.empty()

message = "# 🌊 Welcome to EcoFlow 🌊 "
message_2 = "## Our mission is to help you understand the importance of storm drain pollutions. As we navigate the intricate ecosystem of our planet, it's crucial to recognize the impact that stormwater runoff can have on our environment. This page serves as a valuable hub for information, solutions, and tools to address this pressing issue. "
message_4 = "## Together, let's embark on a journey to safeguard our water resources, preserve biodiversity, and create a healthier planet for future generations. Explore our resources and join us in the fight again storm drain pollution. "

st.markdown(message)
st.write("")
st.markdown(message_2)
st.write("")
st.markdown(message_4)