import requests
url = input("Input the URL: ")
headers = {
    "Accept": "application/json"
}
response = requests.get(url, headers=headers)
data = response.json()

if (response.status_code == 200 and data.get("joke")):
    print(data['joke'])
else:
    print("Invalid resource!")