# SentimentAnalyserMINDS

This project analyses the messages about SHIB and DOGE cryptocurrencies between the time period May 1,2021 - May 15, 2021. 
The data can be found in result.json. 

Preprocessing Data: 
The data is preprocessed to contain only messages with keywords SHIB and DOGE and any non english words are removed. 
The sentiment analysis of the messages are done using VADER (Valence Aware Dictionary for Sentiment Reasoning) model provided in nltk library which classifies unlabled text data. It provides a sentiment score by mapping each word in the text with its lexical features with emotion intensities. 

Below is a plot of the total messages per day and average sentiments per day. It can be seen from the plot that the sentiments were neutral and positive. The majority of the sentiments were not negative as we can see in the plot.
![alt text](https://github.com/kprakash06/SentimentAnalyserMINDS/blob/main/plot.png?raw=true)

## Requirements:
nltk==3.6.1
pandas==1.2.4
plotly==5.3.1
tqdm==4.59.0

## Steps:
1. clone repo
2. run requirements.txt
3. Execute analyser.py

## Files in Repo:
result.json - contains the telegram messages 
plot.png - screenshot of the plot of total message per day and average sentiment per day
analyer.py - includes the driver code to perform sentiment analysis



