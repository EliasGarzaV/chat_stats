#%%
import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#%%
def text_to_df(file_path:str) -> pd.DataFrame:
    """Translates a .txt file that comes from a whatsapp export to a pandas Dataframe"""
    
    whatsapp_regex = r"(\d{2}/\d{2}/\d{2} \d{1,2}:\d{2} [ap]\. m\.) - ([^:]+): (.*)"
    text = open(file_path, "r", encoding="utf8").read()
    matches = re.findall(whatsapp_regex, text, re.MULTILINE)
    
    chat = pd.DataFrame(matches, columns=["date", "name", "message"])
    chat['date'] = pd.to_datetime(chat['date'])
    
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

# %%
chat = text_to_df(r'..\Chats\cemex_team.txt')

chat = analyze_chat(chat)

#%%
#* Get number of text by user
import matplotlib.pyplot as plt
import seaborn as sns

num_chats = chat['name'].value_counts()
plt.bar(num_chats.index, num_chats)
plt.xticks(rotation='vertical')
plt.xlabel('Names')
plt.ylabel('Number of texts')

plt.show()
#%%
weekday = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
chats_per_day =  chat.groupby(chat['date'].dt.day_of_week).size().reset_index(name='count')
plt.plot(chats_per_day['date'].apply(lambda x: weekday[x]), chats_per_day['count'])
plt.ylim([0, chats_per_day['count'].max()* 1.2])
plt.xticks(rotation='vertical')
plt.xlabel('Weekday')
plt.ylabel('Number of texts')

#%%
#days per month
chats_per_day =  chat.groupby(chat['date'].dt.month).size().reset_index(name='count')
plt.plot(chats_per_day['date'], chats_per_day['count'])
plt.ylim([0, chats_per_day['count'].max()* 1.2])
plt.xticks(rotation='vertical')
plt.xlabel('Month')
plt.ylabel('Number of texts')

#%%
cols =  ['name', 'neg', 'neu', 'pos', 'compound']
chat[cols].groupby('name').mean()
