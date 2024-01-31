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

#to save to file
with open('anime_genre.txt', 'w+') as text_file:
    text_file.write(str(anime_response))

#error handling
    if response.status_code == 200:
        anime_data = response.json()
        return anime_data
    elif response.status_code == 404:
        print(f"No data found for the provided genre ID: {genre_id}")
        return None
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

#1 tidy code and get into order
#2 add function to save as txt
#3 rank by popularity
#4 error handling
