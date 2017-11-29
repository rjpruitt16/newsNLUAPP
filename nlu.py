#!/usr/bin/env python

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u''
url = '' 
## read file
def getSentiment(article_path):
    with open(article_path, "r") as article_file:
        url = article_file.readline()
        text = unicode(article_file.read(), "utf-8")
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return (sentiment.score, sentiment.magnitude)  

def writeSentiment(article_path, sentiment):
  with open(article_path, "a") as article:
    article.write("\n{} {}".format(sentiment[0], sentiment[1]))

def writeSentimentToAllFile(path):
  files = os.listdir(path)
  for articles in files:
    if articles.endswith(".txt"):
      writeSentiment(path+articles, getSentiment(path+articles))
    
if __name__ == "__main__":
  writeSentimentToAllFile("article_samples/")

