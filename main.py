import requests
from pprint import pprint

anime_id = input('What anime are you searching for today?: ')

url = f'https://api.jikan.moe/v4/anime?q={anime_id}&sfw'

response = requests.get(url)
print(response)

anime_response = response.json()
pprint(anime_response)

with open('anime.txt', 'w+') as text_file:
    text_file.write(str(anime_response))
