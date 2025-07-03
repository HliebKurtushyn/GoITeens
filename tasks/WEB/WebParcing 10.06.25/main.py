import requests
from bs4 import BeautifulSoup


# URL сторінки музичних чартів
url = "https://api.jikan.moe/v4/anime?genres=10"

result = requests.get(url=url)

d = result.json()["data"]

dictionary = {}

for i in d:
    if i["mal_id"] == 10:
        print(f"{i["title"]}: {i["mal_id"]}\n")
    else:
        dictionary.update({i["title"]: i["mal_id"]})


print(f"Not fantasy films:\n{dictionary}")
        