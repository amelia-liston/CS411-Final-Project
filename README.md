# CS411-Final-Project

## Overview:
### This project makes calls to the Spotify API and manages the personal statistic of users such as their top items, followed artists, and saved albums.

## Routes:

Route: `/login`
- Request Type: POST
- Purpose: Redirects the user to Spotify's authentication page to initiate the OAuth login process.
- Request Body: No request body is required for this endpoint
- Response Format: Redirect to Spotify's authentication page.
  -   Success Response Example:
      - Code: 302
      - Content: Redirects to Spotify's authentication URL.
  -   Example Request: No request body needed.
  -   Example Response: A redirect response pointing to Spotify's authentication page
 
Route: `/callback`
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
 
