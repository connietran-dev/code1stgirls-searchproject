import requests
from pprint import pprint


def search_anime_by_genre(genre):
    base_url = "https://api.jikan.moe/v4/anime"

    # Parameters for the API request
    params = {
        'genres': genre,
        'sort': 'desc',  # 'desc' for descending order, 'asc' for ascending
        'limit': 10  # Number of results to fetch
    }

    try:
        # Making the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for any request errors

        # Parse the JSON response
        data = response.json()

        pprint(data)

        # Display the results
        for anime in data['data']:
            # print(anime['popularity'])
            print(f"Title: {anime['title']}")
            print(f"Popularity: {anime['popularity']}")
            # print(f"Rating: {anime['attributes']['averageRating']}")
            # print("===")


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

#attributes look at alt


# use this to search anime type to return number.
def get_genre_id_by_name(genre_name):
    url = "https://api.jikan.moe/v4/genres/anime"
    response = requests.get(url)
    genres = response.json()

    for genre in genres['data']:
        if genre['name'].lower() == genre_name.lower():
            return genre['mal_id']
    return None


# Example usage
genre_name = input('What anime them would you like to search?: ')
genre_id = get_genre_id_by_name(genre_name)
print(genre_id)

search_anime_by_genre(genre=genre_id)