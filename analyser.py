import datetime
from tqdm import tqdm
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from statistics import mean
import json
import nltk
import pandas as pd
import plotly.graph_objects as go
sia = SentimentIntensityAnalyzer()
words = set(nltk.corpus.words.words())
filter_words = ['SHIB', 'DOGE', 'shib', 'doge']

#function to remove any non-english words in the messages. This is done
#by tokenizing the message and verfiyiny with the corpus data in nltk
def remove_non_english_words(text):
    return " ".join(w for w in word_tokenize(text)
                    if (w.lower() in words and filter_words) or
                    not w.isalpha())

#preprocessing the telegram messages to filter messages containing the words
#'SHIB' and 'DOGE' and removing any additional non-english words in the messages
def preprocess_messages(messages_dataFrame):
    for index, row in tqdm(messages_dataFrame.iterrows(),
    desc="Removing non-english words and finding messages with SHIB and DOGE"):
        date_time_obj = datetime.datetime.strptime((row['date']),
        '%Y-%m-%dT%H:%M:%S')
        text = row['text']
        if any(word in text for word in filter_words):
            preprocessed_messages[date_time_obj.date()].append(remove_non_english_words(text))
    return preprocessed_messages

#using nltk library support for sentimentanalyser to get the sentiment of the messages
def sentiment_analyser():
    for key in preprocessed_messages:
        scores = [
            sia.polarity_scores(msg)["compound"]
            for msg in tqdm(preprocessed_messages[key],
                desc = "Calculating sentiment scores for messages on "+
                str(key))
        ]
        mean_sentiment = mean(scores)
        avg_sentiment_value[key] = mean_sentiment


if __name__ == "__main__":
    #dict to store the preprocessed chats by date
    preprocessed_messages = defaultdict(list)
    #dict to store average sentiment scores by date
    avg_sentiment_value = {}
    #loading result.json file which contains the chats dated from May1-May15
    with open('result.json') as f:
        telegram_messages = json.load(f)
    f.close()
    telegram_msg_df = pd.DataFrame(telegram_messages['messages'])
    preprocess_messages(telegram_msg_df)
    sentiment_analyser()

    #plotting the graph
    total_messages_per_day = []
    for x in preprocessed_messages:
        total_messages_per_day.append(len(preprocessed_messages[x]))

    dates = list(preprocessed_messages.keys())
    fig = go.Figure(data=[
        go.Bar(name='Total messages per day', x=dates,
        y=list(total_messages_per_day), yaxis='y', offsetgroup=1),
        go.Bar(name='Average sentiment per day', x=dates,
        y=list(avg_sentiment_value.values()), yaxis='y2', offsetgroup=2)
    ],
        layout={
                'yaxis': {'title': 'Total messages per day'},
                'yaxis2': {'title': 'Average sentiment per day', 'overlaying': 'y',
                'side': 'right'}
            }
    )
    fig.update_layout(barmode='group')
    fig.show()
