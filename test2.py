import requests
from pprint import pprint

anime_id = input('What anime are you searching for today?: ')

url = f'https://api.jikan.moe/v4/anime?q={anime_id}&sfw'

response = requests.get(url)
print(response)

anime_response = response.json()
pprint(anime_response)

# Save the JSON response to a text file
file_name = f'anime_response_{anime_id}.txt'
with open(file_name, 'w') as file:
    pprint(anime_response, stream=file)

print(f"The JSON response has been saved to {file_name}")
