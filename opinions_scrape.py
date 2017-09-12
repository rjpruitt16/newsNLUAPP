import bs4 as bs
from urllib.request import Request, urlopen

sauce = Request("https://www.washingtonpost.com/news-opinions-sitemap.xml", headers={"User-Agent": "Mozilla"})
webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

##print(soup.title)

##for paragraph in soup.find_all('p'):
 ## print(paragraph.text)

## print(soup.get_text())
article_url = soup.find_all('loc')[0].text
article_sauce = Request(article_url, headers={"User-Agent": "Mozilla"})
print(article_url)
article = urlopen(article_sauce).read()
article_soup = bs.BeautifulSoup(article, "lxml")

for paragraph in article_soup.find_all('p'):
    print(paragraph)

