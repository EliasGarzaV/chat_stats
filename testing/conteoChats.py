#%%
import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

def text_to_df(file_path:str) -> pd.DataFrame:
    """Translates a .txt file that comes from a whatsapp export to a pandas Dataframe"""
    
    whatsapp_regex = r"(\d{2}/\d{2}/\d{2} \d{1,2}:\d{2} [ap]\. m\.) - ([^:]+): (.*)"
    text = open(file_path, "r", encoding="utf8").read()
    matches = re.findall(whatsapp_regex, text, re.MULTILINE)
    
    chat = pd.DataFrame(matches, columns=["date", "name", "message"])
    chat['date'] = pd.to_datetime(chat['date'], dayfirst = True)
    
    return chat

def analyze_chat(chat:pd.DataFrame) -> pd.DataFrame:
    """This function performs a sentiment analysis on all the sentences in the chat and evaluates
    each one of them. After that, it concatenates them into the dataframe and that is what it returns. 

    Args:
        chat (pd.DataFrame): The chat dataframe. (It should come in the format given by the `text_to_df()` function)

    Returns:
        pd.DataFrame: A concatenation of the input dataframe and the evaluations. 
    """
    analyzer = SentimentIntensityAnalyzer()
    analysis = pd.DataFrame(list(
        chat['message'].apply(lambda x : analyzer.polarity_scores(x))))
    
    return pd.concat([chat, analysis], axis = 1)

chat = text_to_df(r'..\Chats\Maza.txt')

chat = analyze_chat(chat)
