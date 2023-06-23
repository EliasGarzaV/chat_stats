import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import sys
sys.path.append("../")

from tools.Insights.dashboard import *

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
# st.write("""Recommends a list of top products based on the customer's information and 
#             historical purchases to enhance their shopping experience. 
#             """)

from PIL import Image

def cb():
    st.session_state.button = True
    
chat = st.session_state['chat']

st.subheader('Chat activity per User')

st.plotly_chart(plot_number_texts(chat))

st.subheader('Conversation starts per user')
st.write('If the group is inactive for 6 hours. The next person to send a text '+
         'adds one to their conversation starts. ')

st.plotly_chart(plot_conv_starts(chat))

st.subheader('Seasonal traffic')

st.plotly_chart(plot_texts_per_hour(chat))
st.plotly_chart(plot_texts_per_weekday(chat))
st.plotly_chart(plot_texts_per_month(chat))
st.plotly_chart(plot_texts_per_day(chat))
    

