import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

query = input("What type of news are you interested in today: ")
api = os.getenv("NEWS_API_KEY")

if not api:
    print("Error: API key not found. Please set NEWS_API_KEY in your .env file.")
    exit(1)

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"

r = requests.get(url)
data = r.json()

articles = data["articles"]

print(f"\nTop news for '{query}':\n")

for index, article in enumerate(articles[:5]):   
    print(f"{index + 1}. {article['title']}")
    print(f"Description: {article['description']}")
    print(f"Read more: {article['url']}")
    print("\n" + "-"*60 + "\n")