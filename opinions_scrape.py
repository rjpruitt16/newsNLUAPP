#!/usr/bin/env python3
import bs4 as bs
from urllib.request import Request, urlopen
from newspaper import Article

def getArticle(url):
  article = Article(url)
  article.download()
  return article

def writeSoupToTextFile(path, soup, article_sauce):
  article_url = soup.find_all('loc')[0].text
  with open(path, "w") as text_file:
     text_file.write(article_url + "\n")

  article = urlopen(article_sauce).read()
  article_soup = bs.BeautifulSoup(article, "lxml")

  for paragraph in article_soup.find_all('p'):
    with open(path, "a") as text_file:
      print(paragraph.text)
      text_file.write(paragraph.text)


def getFirstUrlSoup(sitemap):
  sauce = Request(sitemap, headers={"User-Agent": "Mozilla"})
  webpage = urlopen(sauce).read()
  soup = bs.BeautifulSoup(webpage, 'lxml')
  return soup

def writeArticleToTextFile(article, path):
  with open(path, "w") as text_file:
    text_file.write(article.source_url)
    text_file.write(article.text)


if __name__ == "__main__":
  washington_soup = getFirstUrlSoup("https://www.washingtonpost.com/news-opinions-sitemap.xml")
  washington_url = washington_soup.find_all('loc')[0].text
  article_sauce = Request(washington_url, headers={"User-Agent": "Mozilla"})
  writeSoupToTextFile("article_samples/washington_article.txt", washington_soup, article_sauce)

  cnn_soup = getFirstUrlSoup("http://www.cnn.com/sitemaps/sitemap-index.xml")
  cnn_url = cnn_soup.find_all('loc')[0].text
  cnn_article = getArticle(cnn_url)
  writeArticleToTextFile(cnn_article, "article_samples/cnn_article.txt")  
