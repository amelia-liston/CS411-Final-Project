# CS411-Final-Project

## Overview:
### This project makes calls to the Spotify API and manages the personal statistic of users such as their top items, followed artists, and saved albums.

## Routes:

### Route: `/login`
- Request Type: POST
- Purpose: Redirects the user to Spotify's authentication page to initiate the OAuth login process.
- Request Body: No request body is required for this endpoint
- Response Format: Redirect to Spotify's authentication page.
  -   Success Response Example:
      - Code: 302
      - Content: Redirects to Spotify's authentication URL.
  -   Example Request: No request body needed.
  -   Example Response: A redirect response pointing to Spotify's authentication page
 
### Route: `/callback`
- Request Type: POST
- Purpose: Handles the redirect from Spotify after user authentication and exchanges the authorization code for an access token.
- Request Body:
  - Query Parameter:
    - `code` (String): The authorization code returned by Spotify after user authentication.
- Response Format: Redirects to the `/user-profile` route
  -   Success Response Example:
      - Code: 302
      - Content: Redirects to `/user-profile`.
  -   Example Request: This route does not require a direct request body. It relies on a query parameter provided by Spotify during the redirect.
  -   Example Response: A redirect response to `/user-profile`

 ### Route: `/user-profile`
- Request Type: POST
- Purpose: Fetches and displays the authenticated user's Spotify profile by making a GET request to Spotify's `/me` endpoint using the stored access token.
- Request Body:
  - No request body is required for this endpoint.
- Response Format: JSON response containing the user's Spotify profile data.
  -   Success Response Example:
      - Code: 200
      - Content: 
```
{
    "display_name": "John Doe",
    "id": "johndoe123",
    "email": "johndoe@example.com",
    "country": "US",
    "product": "premium"
}
```
  -   Error Response Example:
      -   Code: 401
      -   Content:
```
{
    "error": {
        "status": 401,
        "message": "Invalid access token"
    }
}
```
  -   Example Request: No request body needed. The access token is retrieved from the session.
  -   Example Response:
      -   A successful response with the user's Spotify profile data:

```
{
    "display_name": "Jane Doe",
    "id": "janedoe",
    "email": "janedoe@example.com",
    "country": "US",
    "product": "free"
}
```
  - Or an error response if the access token is missing:
 ```
HTTP/1.1 302 Found
Location: /login
```

### Route: `/playlists`
- Request Type: POST
- Purpose: Fetches and displays the authenticated user's playlists by making a GET request to Spotify's `/me/playlists` endpoint using the stored access token.
- Request Body:
  - No request body is required for this endpoint.
- Response Format: JSON response containing the user's playlist data.
  -   Success Response Example:
      - Code: 200
      - Content: Redirects to `/user-profile`.
```
{
    "items": [
        {
            "id": "37i9dQZF1DXcBWIGoYBM5M",
            "name": "Today's Top Hits",
            "tracks": {
                "total": 50
            }
        },
        {
            "id": "37i9dQZF1DWXJfnUiYjUKT",
            "name": "Rock Classics",
            "tracks": {
                "total": 80
            }
        }
    ],
    "total": 2,
    "limit": 20,
    "offset": 0,
    "href": "https://api.spotify.com/v1/me/playlists"
}
```

  -   Error Resonse Example
      -   Code: 401
      -   Content:
  -   Example Request: No request body needed. The access token is retrieved from the session.
  -   Example Response:
      -   A successful response with the user's playlist data:
```
{
    "items": [
        {
            "id": "4s1v19zF9Z4NpYGEtikN1t",
            "name": "My Favorite Songs",
            "tracks": {
                "total": 24
            }
        }
    ],
    "total": 1,
    "limit": 20,
    "offset": 0,
    "href": "https://api.spotify.com/v1/me/playlists"
}
```
  -   Or an error response if the access token is missing:
```
HTTP/1.1 302 Found
Location: /login
```

### Route: `/top-items`
- Request Type: POST
- Purpose: Fetches the authenticated user's top items (either artists or tracks) from Spotify based on the specified time range, limit, and offset.
- Request Body:
  - Expected JSON Input:
      - 
- Response Format: 
  -   Success Response Example:
      - Code: 
      - Content: 
```
{
    
}
```

  -   Error Resonse Example
      -   Code: 
      -   Content:
  -   Example Request: 
  -   Example Response:
      -   
```
{
    code here
}
```
  -   Or an error response:
```
code ehre
```

