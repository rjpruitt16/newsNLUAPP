import bs4 as bs
from urllib.request import Request, urlopen

sauce = Request("https://www.washingtonpost.com/news-opinions-sitemap.xml", headers={"User-Agent": "Mozilla"})
webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

article_url = soup.find_all('loc')[0].text
article_sauce = Request(article_url, headers={"User-Agent": "Mozilla"})
print(article_url + "\n")
with open("article_samples/washington_article.txt", "w") as text_file:
    text_file.write(article_url + "\n")

article = urlopen(article_sauce).read()
article_soup = bs.BeautifulSoup(article, "lxml")

for paragraph in article_soup.find_all('p'):
    with open("article_samples/washington_article.txt", "a") as text_file:
        print(paragraph.text)
        text_file.write(paragraph.text)

