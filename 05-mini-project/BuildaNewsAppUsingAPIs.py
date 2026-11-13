import requests

query = input("What type of news are you interested in today? ")

API = "940312a9b1254b28a7c72736841aff37"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-10-13&sortBy=publishedAt&apiKey={API}"

print(url)

r = requests.get(url)

data = r.json()

articles = data["articles"]

