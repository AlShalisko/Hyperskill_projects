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
        file = open('source.html', 'wb')
        file.write(response.content)
        print("Content saved.")
    except Exception as e:
        print("Invalid page!")
else:
    print("The URL returned "+ str(response.status_code) +"!")