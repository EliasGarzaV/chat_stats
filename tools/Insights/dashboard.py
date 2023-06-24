import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import emoji
from wordcloud import WordCloud

def plot_number_texts(chat:pd.DataFrame, size = None, format:str='plotly'):
    num_chats = chat['name'].value_counts()
    
    if(format == 'matplotlib'):
        fig = plt.figure(figsize = size)
        ax = fig.add_subplot()
        
        ax.bar(num_chats.index, num_chats)
        plt.xticks(rotation='vertical', fontsize = 10)
        plt.xlabel('Names')
        plt.ylabel('Number of texts')
    else:
        fig = px.bar(num_chats, labels = {'name': 'Name', 'value':'Number of Texts'})
        fig.update(layout_showlegend=False)
        
    return fig

def plot_texts_per_weekday(chat:pd.DataFrame, format:str='plotly'):
    weekday = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
               4:'Friday', 5:'Saturday', 6:'Sunday'}
    chats_per_day = chat.groupby(chat['date'].dt.day_of_week).size().reset_index(
        name='count')
    chats_per_day['date'] = chats_per_day['date'].apply(lambda x: weekday[x])
    
    if(format == 'matplotlib'):
        fig, ax = plt.subplots()
        ax.plot(chats_per_day['date'], chats_per_day['count'])
        plt.ylim([0, chats_per_day['count'].max()* 1.2])
        plt.xticks(rotation='vertical')
        plt.xlabel('Weekday')
        plt.ylabel('Number of texts')
        plt.title('Texts per Day of the Week')
    else:
        fig = px.line(chats_per_day, x = 'date', y = 'count', labels={
            'date':'Day of the week', 'count':'Number of Texts'})
        fig.update(layout_showlegend=False)
        fig.update_layout(title = 'Texts per Weekday', title_x = 0.5)
        
    return fig

def plot_texts_per_month(chat:pd.DataFrame, format:str='plotly'):
    month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December"
    }
    all_months = list(range(1, 13))
    chats_per_month = chat.groupby(chat['date'].dt.month).size().reset_index(name='count')
    chats_per_month = chats_per_month.set_index('date')
    chats_per_month = chats_per_month.reindex(all_months, fill_value=0).reset_index()
    chats_per_month['date'] = chats_per_month['date'].apply(lambda x: month_dict[x])
    
    if(format == 'matplotlib'):
        fig, ax = plt.subplots()
        ax.plot(chats_per_month['date'], chats_per_month['count'])

        plt.ylim([0, chats_per_month['count'].max()* 1.2])
        plt.xlim([0, 11])
        plt.xticks(rotation='vertical')
        plt.xlabel('Month')
        plt.ylabel('Number of texts')
        plt.title('Texts per Month')
    else:
        fig = px.line(chats_per_month, x='date', y='count', 
                      labels={'date':'Month', 'count':'Number of Texts'})
        fig.update(layout_showlegend=False)
        fig.update_layout(title = 'Texts per Month', title_x = 0.5)
    return fig
       
def plot_texts_per_hour(chat:pd.DataFrame, format:str='plotly'):
    hours = range(0, 24)
    chats_per_hour = chat.groupby(chat['date'].dt.hour).size().reset_index(name='count')
    chats_per_hour = chats_per_hour.set_index('date')
    chats_per_hour = chats_per_hour.reindex(hours, fill_value=0).reset_index()
    chats_per_hour['date'] = chats_per_hour['date'].apply(lambda x: str(x) + ':00')
    
    if(format == 'matplotlib'):
        fig, ax = plt.subplots()
        ax.plot(chats_per_hour['date'], chats_per_hour['count'])

        plt.ylim([0, chats_per_hour['count'].max()* 1.2])
        plt.xlim([0, 24])
        plt.xticks(rotation='vertical')
        plt.xlabel('Hour')
        plt.ylabel('Number of texts')
        plt.title('Texts per Hour of the Day')   
    else:
        fig = px.line(chats_per_hour, x='date', y='count', 
                      labels={'date':'Hour', 'count':'Number of Texts'})
        fig.update(layout_showlegend=False)
        fig.update_layout(title = 'Texts per Hour', title_x = 0.5)

    return fig
       
def plot_texts_per_day(chat:pd.DataFrame, format:str='plotly'):
    """This always includes 29 of february!!!
    """
    month_to_days = {
        1: 0,
        2: 31,
        3: 60,
        4: 91,
        5: 121,
        6: 152,
        7: 182,
        8: 213,
        9: 244,
        10: 274,
        11: 305,
        12: 335
    }

    days = range(1, 367)
    chats_per_day = chat.groupby(chat['date'].apply(lambda x: (x.month, x.day))).size().reset_index(name='count')
    chats_per_day['date'] = chats_per_day['date'].apply(lambda x: month_to_days[x[0]] + x[1])
    chats_per_day = chats_per_day.set_index('date')
    chats_per_day = chats_per_day.reindex(days, fill_value=0).reset_index()

    if(format == 'matplotlib'):
        fig, ax = plt.subplots()
        ax.plot(chats_per_day['date'], chats_per_day['count'])

        plt.ylim([0, chats_per_day['count'].max()* 1.2])
        plt.xlim([0, 366])
        plt.xticks(rotation='vertical')
        plt.xlabel('Day of the year')
        plt.ylabel('Number of texts per day')
        plt.title('Texts per Day')
    else:
        fig = px.line(chats_per_day, x='date', y='count', 
                      labels={'date':'Day of the year', 'count':'Number of Texts'})
        fig.update(layout_showlegend=False)
        fig.update_layout(title = 'Texts per Day', title_x = 0.5)
    return fig

def sentiment_mean(chat:pd.DataFrame):
    cols =  ['name', 'neg', 'neu', 'pos', 'compound']
    chat[cols].groupby('name').mean()

def plot_conv_starts(chat:pd.DataFrame, size = None, format:str='plotly'):
    chat['time_diff'] = chat['date'].diff().apply(lambda x: x.total_seconds() / 3600)
    
    new_convs = chat[chat['time_diff'] > 6]
    
    num_chats = new_convs['name'].value_counts()
    
    if(format == 'matplotlib'):
        fig = plt.figure(figsize = size)
        ax = fig.add_subplot()
        
        ax.bar(num_chats.index, num_chats)
        plt.xticks(rotation='vertical', fontsize = 10)
        plt.xlabel('Names')
        plt.ylabel('Number of texts')
    else:
        fig = px.bar(num_chats, labels = {'name': 'Name', 'value':'Number of Conversation Starts'})
        fig.update(layout_showlegend=False)
    
    return fig
     
def plot_most_used_emojis(chat, num_emojis:int=6):
    text = ''.join(chat['message'])
    emoji_count = pd.Series([s['emoji']
            for s in emoji.emoji_list(text)]).value_counts().head(num_emojis)
    
    fig = px.bar(emoji_count, labels = {'index': 'Emoji', 'value':'Times Used'})
    fig.update(layout_showlegend=False)
    fig.update_layout(title = 'Most used Emojis', title_x = 0.5)
    
    return fig
    
def plot_word_cloud(chat:pd.DataFrame, size=(1500,700),num_words:int=50):
    text = ' '.join(chat['message']).split()
    text = filter(lambda x: len(x)>3, text)

    word_count = pd.Series(text).value_counts()
    word_count = word_count.drop(['<Multimedia', 'omitido>'])
    
    wc = WordCloud(background_color="white", width=size[0], height=size[1])
    wc.generate_from_frequencies(word_count.head(num_words))
    
    fig = px.imshow(wc)
    fig.update_layout(title = 'Most used Words', title_x = 0.5)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return fig
