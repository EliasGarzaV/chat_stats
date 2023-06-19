import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="General Insights",
                #    page_icon= Image.open('boat-removebg-preview.png')
                )
# image = Image.open('Cemex_logo_2023.png')
# boat = Image.open('boat-removebg-preview.png')
# cemexboat = Image.open('cemexandboar-removebg-preview.png')
# with st.sidebar:
#     st.image(cemexboat)

#Streamlit
st.header("General Information")
st.subheader('Client Based Campaign')

st.write("""Recommends a list of top products based on the customer's information and 
            historical purchases to enhance their shopping experience. 
            """)

from PIL import Image

def cb():
    st.session_state.button = True
    
chat = st.session_state['chat']

fig, ax = plt.subplots()

num_chats = chat['name'].value_counts()
ax.bar(num_chats.index, num_chats)
plt.xticks(rotation='vertical')
plt.xlabel('Names')
plt.ylabel('Number of texts')

st.pyplot(fig)

