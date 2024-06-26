import os
import openai
import streamlit as st
from openai import OpenAI

import requests
from streamlit_lottie import st_lottie

# new code (to access json data of animation)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_image = load_lottieurl("https://lottie.host/8248687f-b968-4f31-8da4-c75a3237d0ea/LpnedDtJIu.json")

st.markdown("# Learn More About Storm Drains 🌊🗑️")
st.sidebar.markdown("# Page 2: Text Generation 🌊🗑️")

openai.api_key = os.environ["OPENAI_API_KEY"]



client = OpenAI()


# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your responsibility is to help users understand more about storm drains, and how to prevent trash from entering them along with understanding the effects of trash in these water systems"},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

# Load Assets
lottie_image = load_lottieurl("https://lottie.host/8248687f-b968-4f31-8da4-c75a3237d0ea/LpnedDtJIu.json")

# create our streamlit app
# create our streamlit app
cols = st.columns(2)

with cols[0].form(key = "chat1"):
    for _ in range(100):  
        st.empty()
    prompt = st.text_area("Enter a concept you would like me to explain: ", height=200) 
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))

with cols[1]:
    st_lottie(lottie_image, speed=1, width=400, height=300, key="initial")
    for _ in range(100): 
        st.empty()

        # adjust text box to expad with the text along with animations 