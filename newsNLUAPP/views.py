from django.shortcuts import render
import os 

def getWords(article, number_of_words):
  if number_of_words > len(article):
    return article
  words = article.split(" ")
  summary = ""
  for word in words[:number_of_words]:
    summary += word + " "
  return summary 

def ReadAndAddUrl(article_dict, path, name):
  data = ParseArticleData(path)
  print(data.keys())
  data["article"] = getWords(data["article"], 30)
  article_dict = {}
  for key in data.keys():
    article_dict[name+"_"+key] = data[key]
  return article_dict

def ParseArticleData(path):
  data = {}
  with open(path, "r") as textfile:
    data["url"] = textfile.readline()
    data["article"] = textfile.readline()
    sentiment = textfile.readline().rstrip()
    sentiment = sentiment.split(" ")
    print(sentiment)
    print("SENTIMENT ABOVE")
    data["sentiment_x"] = float(sentiment[0])
    data["sentiment_y"] = float(sentiment[1])
  return data

def index(request):
  #print(os.listdir('.'))
  data_articles = os.listdir("article_samples/")
  article_dict = {}
  for article in data_articles:
    if article.endswith(".txt"):
      name = article.split("_")
      ## TODO find out how to pass dict by reference
      article_dict.update(ReadAndAddUrl(article_dict, "article_samples/"+article, name[0]))
  print(article_dict.keys())
              
  return render(request, "homepage.html", article_dict)
   
