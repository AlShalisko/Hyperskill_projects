import requests
import string
from bs4 import BeautifulSoup
url = "https://www.nature.com/nature"
url_start = "/articles?sort=PubDate&year=2020&page=3"
headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'My User Agent 1.0'
}
translator = str.maketrans('', '', string.punctuation)

response = requests.get((url + url_start), headers=headers)
#print(response)
if (response.status_code == 200):
    try:
        beautiful_soup = BeautifulSoup(response.content, 'html.parser')
        articles = beautiful_soup.find_all('article')
        #print(articles)
        #print(articles[0].prettify())
        for article in articles:
            article_type = article.find("span", class_="c-meta__type").get_text(strip=True)
            if article_type == "News":
                print(article)
                article_url = url + article.find("a")["href"]
                article_response = requests.get(article_url, headers=headers)
                soup = BeautifulSoup(article_response.content, 'html.parser')
                print(article_url)
                print(soup)
                article_title = soup.find("title").get_text(strip=True)
                article_title = article_title.translate(translator)
                article_title = article_title.replace(" ", "_")
                print(article_title)
                article_content = soup.find("p", class_="article__teaser").get_text(strip=True)
                print(article_content)
                file = open(f'{article_title}.txt', 'w', encoding="utf-8")
                file.write(article_content)
        print("Content saved.")
    except Exception as e:
        print("Invalid page!")
else:
    print("The URL returned "+ str(response.status_code) +"!")