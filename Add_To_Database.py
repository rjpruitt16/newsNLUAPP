from models import article
from os import listdir
from os.path import isfile, join

def getArticleFileName(mypath)
  return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def AddTextFileToDB(filename):
  with open(filename, "r") as textfile:
    url = textfile.readline()
    date = textfile.readline()
    score = textfile.readline()
    magnitude = textfile.readline()
    article_content = textfile.read()
    article_file = article(title=url,date=date,score=score, magnitude=magnitude, article_content=article_content)
    article_file.save()
