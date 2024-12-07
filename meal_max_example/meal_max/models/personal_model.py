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
        TBD
    """

    def __init__(self):
        """Not entirely sure what to initialize yet"""

    def get_headers(self):
        """
        Returns headers with authorization token for Spotify API requests. //We will need to figure out what to put in here.
        """
        
    
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
        # Check type
        if type not in ["artists", "tracks"]:
            raise ValueError("Invalid item type: %s", type)
        
        # Check time_range
        if time_range not in ["long_term", "medium_term", "short_term"]:
            raise ValueError("Invalid time range: %s", time_range)
        
        # Check limit
        if limit <1 or limit >50:
            raise ValueError("Invalid item limit: %s", limit)
        
        # Check offset
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
