SentimentAnalyserMINDS
This project analyses the messages about SHIB and DOGE cryptocurrencies between the time period May 1,2021 - May 15, 2021. 
The data can be found in result.json. 

Preprocessing Data: 
The data is preprocessed to contain only messages with keywords SHIB and DOGE and any non english words are removed. 
The sentiment analysis of the messages are done using VADER (Valence Aware Dictionary for Sentiment Reasoning) model provided in nltk library which classifies unlabled text data. It provides a sentiment score by mapping each word in the text with its lexical features with emotion intensities. 

Below is a plot of the total messages per day and average sentiments per day. It can be seen from the plot that the sentiments were neutral and positive. 




