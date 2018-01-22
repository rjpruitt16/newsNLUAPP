#!/usr/bin/env python3
import bs4 as bs
from urllib.request import Request, urlopen
from newspaper import Article

def getArticle(url):
  article = Article(url)
  article.download()
  article.parse()
  return article

def writeSoupToTextFile(path, soup, article_sauce):
  article_url = soup.find_all('loc')[0].text
  with open(path, "w") as text_file:
     text_file.write(article_url + "\n")

  article = urlopen(article_sauce).read()
  article_soup = bs.BeautifulSoup(article, "lxml")

  for paragraph in article_soup.find_all('p'):
    with open(path, "a") as text_file:
      text_file.write(paragraph.text)


def makeUrlSoup(url):
  sauce = Request(url, headers={"User-Agent": "Mozilla"})
  webpage = urlopen(sauce).read()
  soup = bs.BeautifulSoup(webpage, 'lxml')
  return soup

def writeArticleToTextFile(article, path, keywords):
  article.download()
  with open(path, "w") as text_file:
    text_file.write('{}\n{}\n{}\n{}'.format(article.url, article.text.replace('\n\n', ' '), keywords, str(article)))

def getListOfArticleLinks(url, soup):
    ## A function to get Article links from front page.
    for article in soup.find_all('article'):
        return article.find_all('a', href=True)

def FindAndWriteArticle(sitemap="", front_page="", article_name=""):
  soup = ""
  url = ""
  if sitemap:
    soup = makeUrlSoup(sitemap)
    url = soup.find_all('loc')[0].text
  elif front_page:
    soup = makeUrlSoup(front_page)
    url = getListOfArticleLinks(front_page, soup)[0]["href"]
    print(url)
  article = getArticle(url)
  writeArticleToTextFile(article, "article_samples/" + article_name, article.keywords)

if __name__ == "__main__":
  ##FindAndWriteArticle("https://www.washingtonpost.com/news-opinions-sitemap.xml", 'washington_article.txt')

  ##FindAndWriteArticle("http://www.cnn.com/sitemaps/sitemap-articles-2017-11.xml", "cnn_article.txt")

  ##FindAndWriteArticle("https://www.huffingtonpost.com/sitemap.xml", "huffington_article.txt")

  FindAndWriteArticle(front_page="https://www.npr.org/sections/politics/", article_name="npr_article.txt")

  ##FindAndWriteArticle("http://www.foxnews.com/sitemap.xml?idx=26", "foxnews_article.txt")

  ##FindAndWriteArticle("https://www.bloomberg.com/feeds/bpol/sitemap_news.xml", "bloomberg_article.txt")
