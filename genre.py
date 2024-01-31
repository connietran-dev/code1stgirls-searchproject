import requests

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

        # Display the results
        for anime in data['data']:
            print(f"Title: {anime['attributes']['titles']['en']}")
            print(f"Rating: {anime['attributes']['averageRating']}")
            print("===")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Usage example
search_anime_by_genre(genre='Drama')
