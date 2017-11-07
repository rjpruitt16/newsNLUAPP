# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u''
url = '' 
## read file
def getSentiment(article_file):
    with open("washington_article.txt", "r") as article_file:
        url = article_file.readline()
        text = unicode(article_file.read(), "utf-8")
    
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return (sentiment.score, sentiment.magnitude)  

#print('Text: {}'.format(text.encode('utf-8')))
#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
