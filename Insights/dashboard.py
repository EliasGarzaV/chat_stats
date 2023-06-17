import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_number_texts(chat:pd.DataFrame):
    num_chats = chat['name'].value_counts()
    plt.bar(num_chats.index, num_chats)
    plt.xticks(rotation='vertical')
    plt.xlabel('Names')
    plt.ylabel('Number of texts')
    
def plot_texts_per_weekday(chat:pd.DataFrame):
    weekday = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    chats_per_day =  chat.groupby(chat['date'].dt.day_of_week).size().reset_index(name='count')
    plt.plot(chats_per_day['date'].apply(lambda x: weekday[x]), chats_per_day['count'])
    plt.ylim([0, chats_per_day['count'].max()* 1.2])
    plt.xticks(rotation='vertical')
    plt.xlabel('Weekday')
    plt.ylabel('Number of texts')

def plot_texts_per_month(chat:pd.DataFrame):
    chats_per_day =  chat.groupby(chat['date'].dt.month).size().reset_index(name='count')
    plt.plot(chats_per_day['date'], chats_per_day['count'])
    plt.ylim([0, chats_per_day['count'].max()* 1.2])
    plt.xticks(rotation='vertical')
    plt.xlabel('Month')
    plt.ylabel('Number of texts')
    
def sentiment_mean(chat:pd.DataFrame):
    cols =  ['name', 'neg', 'neu', 'pos', 'compound']
    chat[cols].groupby('name').mean()