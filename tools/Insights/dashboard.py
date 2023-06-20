import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_number_texts(chat:pd.DataFrame, size = None):
    num_chats = chat['name'].value_counts()
    
    fig = plt.figure(figsize = size)
    ax = fig.add_subplot()
    
    ax.bar(num_chats.index, num_chats)
    plt.xticks(rotation='vertical', fontsize = 10)
    plt.xlabel('Names')
    plt.ylabel('Number of texts')
    
    return fig
    
def plot_texts_per_weekday(chat:pd.DataFrame):
    weekday = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
               4:'Friday', 5:'Saturday', 6:'Sunday'}
    chats_per_day = chat.groupby(chat['date'].dt.day_of_week).size().reset_index(name='count')
    
    fig, ax = plt.subplots()
    ax.plot(chats_per_day['date'].apply(lambda x: weekday[x]), chats_per_day['count'])
    plt.ylim([0, chats_per_day['count'].max()* 1.2])
    plt.xticks(rotation='vertical')
    plt.xlabel('Weekday')
    plt.ylabel('Number of texts')
    
    return fig

def plot_texts_per_month(chat:pd.DataFrame):
    month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
    11: "November", 12: "December"
    }
    all_months = list(range(1, 13))
    chats_per_month = chat.groupby(chat['date'].dt.month).size().reset_index(name='count')
    chats_per_month = chats_per_month.set_index('date')
    chats_per_month = chats_per_month.reindex(all_months, fill_value=0).reset_index()
    
    fig, ax = plt.subplots()
    ax.plot(chats_per_month['date'].apply(lambda x: month_dict[x]), chats_per_month['count'])

    plt.ylim([0, chats_per_month['count'].max()* 1.2])
    plt.xlim([0, 11])
    plt.xticks(rotation='vertical')
    plt.xlabel('Month')
    plt.ylabel('Number of texts')
    
    return fig
       
def plot_texts_per_hour(chat:pd.DataFrame):
    hours = range(0, 24)
    chats_per_hour = chat.groupby(chat['date'].dt.hour).size().reset_index(name='count')
    chats_per_hour = chats_per_hour.set_index('date')
    chats_per_hour = chats_per_hour.reindex(hours, fill_value=0).reset_index()

    fig, ax = plt.subplots()
    ax.plot(chats_per_hour['date'].apply(lambda x: str(x) + ':00'), chats_per_hour['count'])

    plt.ylim([0, chats_per_hour['count'].max()* 1.2])
    plt.xlim([0, 24])
    plt.xticks(rotation='vertical')
    plt.xlabel('Hour')
    plt.ylabel('Number of texts')
    
    return fig
       
def plot_texts_per_day(chat:pd.DataFrame):
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

    fig, ax = plt.subplots()
    ax.plot(chats_per_day['date'], chats_per_day['count'])

    plt.ylim([0, chats_per_day['count'].max()* 1.2])
    plt.xlim([0, 366])
    plt.xticks(rotation='vertical')
    plt.xlabel('Day of the year')
    plt.ylabel('Number of texts per day')
    
    return fig

def sentiment_mean(chat:pd.DataFrame):
    cols =  ['name', 'neg', 'neu', 'pos', 'compound']
    chat[cols].groupby('name').mean()
    
#inicia conversaciones
#emojis
#palabras más usadas
#ats
#fin de conversacion
#horas del dia
