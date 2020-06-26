import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.pravda.com.ua/news/')
# print(request.text)

soup = BeautifulSoup(request.text, features="html.parser")
print(soup.li)

for child in soup.recursiveChildGenerator():
    if child.name:
        # print(child.name)
        pass


result = soup.find("div",{"class":"news news_all"})

articles = soup.find_all("div",{"class":"article"})
#
# for article in articles:
#     print(article.text)

articles = soup.select('div .news.news_all>div.article>div.article__title>a' )
for article in articles:
    print(article.attrs['href'])
    print(article.string)

    # print(article_url)
# print(result)