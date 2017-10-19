from django.shortcuts import render
import os 

def index(request):
  print(os.getcwd())
  washington_url = ""
  washington_body = ""
  with open("article_samples/washington_article.txt", "r") as textfile:
    washington_url = textfile.readline()
    washington_body = textfile.read()
  
  words = washington_body.split(" ")
  washington_body = ""
  for word in words[:30]:
    washington_body += word + " " 
              
  return render(request, "homepage.html", {"washington_url": washington_url, "washington_body": washington_body})
   
