import requests
from bs4 import BeautifulSoup
url = input("Input the URL: ")
headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'My User Agent 1.0'
}

response = requests.get(url, headers=headers)
#print(response)
if (response.status_code == 200):
    try:
        beautiful_soup = BeautifulSoup(response.content, 'html.parser')
        title = beautiful_soup.title.text
        summary = beautiful_soup.find('meta', attrs= {'name': 'description'}).get('content')
        print(dict(title = title, description = summary))
    except Exception as e:
        print("Invalid page!")
else:
    print("Invalid page!")