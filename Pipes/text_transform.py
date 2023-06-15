import pandas as pd
import re

def text_to_df(file_path:str) -> pd.DataFrame:
    """Translates a .txt file that comes from a whatsapp export to a pandas Dataframe"""
    
    whatsapp_regex = r"(\d{2}/\d{2}/\d{2} \d{1,2}:\d{2} [ap]\. m\.) - ([^:]+): (.*)"
    text = open(file_path, "r", encoding="utf8").read()
    matches = re.findall(whatsapp_regex, text, re.MULTILINE)
    
    chat = pd.DataFrame(matches, columns=["date", "name", "message"])
    chat['date'] = pd.to_datetime(chat['date'])
    
    return chat

