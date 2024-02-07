import requests
from pprint import pprint

def get_genre_id_by_name(genre_name):
    url = "https://api.jikan.moe/v4/genres/anime"
    response = requests.get(url)
    genres = response.json()

    for genre in genres['data']:
        if genre['name'].lower() == genre_name.lower():
            return genre['mal_id']
    return None

def search_anime_by_genre(genre_name):
    genre_id = get_genre_id_by_name(genre_name)

    if genre_id is not None:
        base_url = "https://api.jikan.moe/v4/anime"
        params = {
            'genres': genre_id,
            'order_by': 'popularity',
            'sort': 'asc',
            'limit': 10
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            print(f"{genre_name.capitalize()} data:")
            pprint(data)

            save_to_txt(data, genre_name)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    else:
        print(f"No genre found for: {genre_name}")

def save_to_txt(data, genre_name):
    with open('anime_genre_recommendations.txt', 'w+') as text_file:
        text_file.write(f"{genre_name.capitalize()} recommendations:\n\n")
        sorted_anime = sorted(data['data'], key=lambda x: x['popularity'])

        for anime in sorted_anime:
            text_file.write(f"Title: {anime['title']}\n")
            text_file.write(f"Rating: {anime['rating']}\n")
            text_file.write(f"Score: {anime['score']}\n")
            text_file.write(f"Popularity: {anime['popularity']}\n")
            text_file.write("===\n")

genre_name = input('What anime theme would you like to search?: ')
search_anime_by_genre(genre_name)

