import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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