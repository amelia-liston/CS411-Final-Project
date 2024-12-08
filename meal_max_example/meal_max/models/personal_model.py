import logging
import os
import time
from typing import Any, List
import requests


logger = logging.getLogger(__name__)
configure_logger(logger)


TTL = os.getenv("TTL", 60)  # Default TTL is 60 seconds


class PersonalModel:
    """
    A class to manage personal statistics of a user.

    Attributes:
        access_token (str): The OAuth token for Spotify API.
    """
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self, access_token: str):
        """Initialize the SpotifyModel with an access token"""
        self.access_token = access_token

    def get_headers(self):
        """
        Returns headers with authorization token for Spotify API requests.
        """
        return {"Authorization": f"Bearer {self.access_token}"}
        
    
    def get_top_items(self, type: str, time_range: str = "medium_term", limit: int = 20, offset: int = 0) -> dict:
        """
        Fetches the user's top items (either artists or tracks) from Spotify.

        Args:
            type (str): 'artists' or 'tracks' to specify which type of items to fetch.
            time_range (str): The time period to check (default 'medium_term').
            limit (int): Number of items to return (default 20, min 1, max 50).
            offset (int): The index of the first item to return (default 0). Can use with limit for pages of items.
        
        Returns:
            dict: JSON response containing the top items (artists or tracks).

        Raises:
            ValueError: if the type entered is not valid, if the time range is invalid, if the limit is invalid, or if the offset is invalid.
            RuntimeError: If the request to the Spotify API fails or returns an invalid response.
        """
        # Validate the inputs
        if type not in ["artists", "tracks"]:
            raise ValueError("Invalid item type: %s", type)
        if time_range not in ["long_term", "medium_term", "short_term"]:
            raise ValueError("Invalid time range: %s", time_range)
        if limit <1 or limit >50:
            raise ValueError("Invalid item limit: %s", limit)
        if offset <0:
            raise ValueError("Invalid offset: %s", offset)
        
        # Construct URL
        url = f"{self.BASE_URL}/me/top/{type}"
        
        # Define query parameters
        params = {
            "time_range": time_range,
            "limit": limit,
            "offset": offset
        }
        
        try:
            # Log the request to spotify
            logger.info("Fetching top items from %s", url)

            # Send request to Spotify API
            response = requests.get(url, headers=self.get_headers(), params=params, timeout=5)
            response.raise_for_status()  # Raise an error if the request failed

            # Return response JSON
            return response.json()

        except requests.exceptions.Timeout:
            logger.error("Request to Spotify timed out.")
            raise RuntimeError("Request to Spotify timed out.")
    
        except requests.exceptions.RequestException as e:
            logger.error("Request to Spotify failed: %s", e)
            raise RuntimeError("Request to Spotify failed: %s" % e)
        
    def get_followed_artists(self, limit: int = 20, after: str = None) -> dict:
        """
        Fetch the user's followed artists from Spotify.

        Args:
            limit (int): The number of artists to return (default is 20, min is 1, max is 50).
            after (str): The cursor for the next page of results.

        Returns:
            dict: The response from the Spotify API containing followed artists data.

        Raises:
            ValueError: If input parameters are invalid.
            RequestException: If the Spotify API request fails.
        """
        # Validate inputs
        if not (1 <= limit <= 50):
            raise ValueError("Limit must be between 1 and 50.")

        # Prepare API request
        headers = self.get_headers()
        params = {
            'type': 'artist',
            'limit': limit
        }
        if after:
            params['after'] = after

        url = f"{self.BASE_URL}/me/following"

        # Make the request to Spotify API
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json().get('artists', {})
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to fetch followed artists: {str(e)}")
        
    def get_saved_albums(self, limit: int = 20, offset: int = 0, market: str = None) -> dict:
        """
        Fetches the user's saved albums from Spotify.

        Args:
            limit (int): Number of items to return (default 20, min 1, max 50).
            offset (int): The index of the first item to return (default 0).
            market (str, optional): Country code to filter content by market.

        Returns:
            dict: The response from the Spotify API containing the saved albums.

        Raises:
            ValueError: If the limit or offset values are invalid.
            RuntimeError: If the request to the Spotify API fails or returns an invalid response.
        """
        # Validate the inputs
        if limit <1 or limit >50:
            raise ValueError("Invalid item limit: %s", limit)
        if offset < 0:
            raise ValueError("Invalid offset: %s", offset)

        # Construct URL
        url = f"{self.BASE_URL}/me/albums"

        # Define query parameters
        params = {
            "limit": limit,
            "offset": offset,
        }
        if market:
            params["market"] = market

        try:
            # Log the request to Spotify
            logger.info("Fetching saved albums from %s", url)

            # Send request to Spotify API
            response = requests.get(url, headers=self.get_headers(), params=params, timeout=5)
            response.raise_for_status()  # Raise an error if the request failed

            # Return response JSON
            return response.json()

        except requests.exceptions.Timeout:
            logger.error("Request to Spotify timed out.")
            raise RuntimeError("Request to Spotify timed out.")

        except requests.exceptions.RequestException as e:
            logger.error("Request to Spotify failed: %s", e)
            raise RuntimeError("Request to Spotify failed: %s" % e)


