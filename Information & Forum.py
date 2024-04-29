import os
import openai
import streamlit as st
from openai import OpenAI

st.markdown("# Ask any question about storm drains 🌊🗑️")
st.sidebar.markdown("# Page 1: Information & Forum 🌊🗑️")

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

# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_area("Enter a concept you would like me to explain: ") 
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))

# New section: Community Reporting and Engagement Platform
st.markdown("# Community Reporting and Engagement Platform 🌊🗑️")


# Create a discussion board for users to engage with their community
st.markdown("## Community Discussion Board")
discussion_prompt = st.text_input('Enter a topic or question for discussion')
if st.button('Post to Discussion Board'):
    st.write(f'New Discussion Topic: {discussion_prompt}')