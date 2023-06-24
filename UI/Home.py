import streamlit as st
from PIL import Image
import pandas as pd
import re
from io import StringIO
import sys
sys.path.append("../")
from tools.Pipes.text_transform import *

st.set_page_config(
    page_title="Chat Stats",
    page_icon= Image.open('figures\LogoChat_Stats.png')
)

st.image('figures\LogoChat_Stats.png', width= 200)

# boat = Image.open('cemexandboar.png')

# st.image(boat, width=500)
st.header("Chat Stats")
st.subheader('Hola')

st.write()
st.info(
    """
    __Chat Stats__ helps you find insights of your whatsapp groups and contacts. 
    """
)


@st.cache_data
def load(text) -> pd.DataFrame:
    """Translates a .txt file that comes from a whatsapp export to a pandas Dataframe"""

    text = StringIO(chat_file.getvalue().decode('utf-8')).read()
    
    return str_to_df(text)

label = 'To start, please upload the exported .txt file of the exported chat. You can get it from your phone in the Whatsapp app.'
chat_file = st.file_uploader(label, type='txt', accept_multiple_files=False,
                key=None, help=None, on_change=None, args=None,
                kwargs=None, disabled=False, label_visibility="visible")

if(chat_file is not None):
    st.session_state['chat'] = load(chat_file)
    st.write(st.session_state['chat'])
    

    