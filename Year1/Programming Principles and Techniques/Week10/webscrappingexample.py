from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.bbc.co.uk/news/")
soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("a")


for tag in tags:
    print(tag)
