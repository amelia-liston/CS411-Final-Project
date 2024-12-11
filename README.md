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
- Purpose: Fetches and displays the user's top artists or tracks by making a GET request to Spotify's `/me/top/{type}` endpoint using the stored access token and an input type of item.
- Request Body:
  - No request body is required for this endpoint.
- Response Format: JSON response containing the user's list of items.
  -   Success Response Example:
      - Code: 200
      - Content:
```
{
  "href": "https://api.spotify.com/v1/me/top/artists?limit=1&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "limit": 1,
  "next": "https://api.spotify.com/v1/me/top/artists?offset=1&limit=1&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "offset": 0,
  "previous": null,
  "total": 154,
  "items": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/0e86yPdC41PGRkLp2Q1Bph"
      },
      "followers": {
        "href": null,
        "total": 4253854
      },
      "genres": ["canadian indie rock", "pov: indie", "vancouver indie"],
      "href": "https://api.spotify.com/v1/artists/0e86yPdC41PGRkLp2Q1Bph",
      "id": "0e86yPdC41PGRkLp2Q1Bph",
      "images": [
        {
          "url": "https://i.scdn.co/image/ab6761610000e5eb90f1016268dd7a972d740fd3",
          "height": 640,
          "width": 640
        },
        {
          "url": "https://i.scdn.co/image/ab6761610000517490f1016268dd7a972d740fd3",
          "height": 320,
          "width": 320
        },
        {
          "url": "https://i.scdn.co/image/ab6761610000f17890f1016268dd7a972d740fd3",
          "height": 160,
          "width": 160
        }
      ],
      "name": "Mother Mother",
      "popularity": 73,
      "type": "artist",
      "uri": "spotify:artist:0e86yPdC41PGRkLp2Q1Bph"
    }
  ]
}
```

  -   Error Resonse Example
      -   Code: 401
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Error Resonse Example
      -   Code: 403
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Error Resonse Example
      -   Code: 429
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Example Request: No request body needed. The access token is retrieved from the session.
  -   Example Response:
      -   A successful response with the user's top items:
```
{
  "href": "https://api.spotify.com/v1/me/top/artists?limit=1&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "limit": 1,
  "next": "https://api.spotify.com/v1/me/top/artists?offset=1&limit=1&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "offset": 0,
  "previous": null,
  "total": 154,
  "items": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/0e86yPdC41PGRkLp2Q1Bph"
      },
      "followers": {
        "href": null,
        "total": 4253854
      },
      "genres": ["canadian indie rock", "pov: indie", "vancouver indie"],
      "href": "https://api.spotify.com/v1/artists/0e86yPdC41PGRkLp2Q1Bph",
      "id": "0e86yPdC41PGRkLp2Q1Bph",
      "images": [
        {
          "url": "https://i.scdn.co/image/ab6761610000e5eb90f1016268dd7a972d740fd3",
          "height": 640,
          "width": 640
        },
        {
          "url": "https://i.scdn.co/image/ab6761610000517490f1016268dd7a972d740fd3",
          "height": 320,
          "width": 320
        },
        {
          "url": "https://i.scdn.co/image/ab6761610000f17890f1016268dd7a972d740fd3",
          "height": 160,
          "width": 160
        }
      ],
      "name": "Mother Mother",
      "popularity": 73,
      "type": "artist",
      "uri": "spotify:artist:0e86yPdC41PGRkLp2Q1Bph"
    }
  ]
}
```

### Route: `/following`
- Request Type: POST
- Purpose: Fetches and displays the user's followed artists by making a GET request to Spotify's `/me/following` endpoint using the stored access token.
- Request Body:
  - No request body is required for this endpoint.
- Response Format: JSON response containing the user's followed artists.
  -   Success Response Example:
      - Code: 200
      - Content:
```
{
  "artists": {
    "href": "https://api.spotify.com/v1/me/following?type=artist&limit=1&locale=en-US,en;q%3D0.9,es;q%3D0.8",
    "limit": 1,
    "next": "https://api.spotify.com/v1/me/following?type=artist&limit=1&after=3AFsnAC0H9hes71BeRypbq&locale=en-US,en;q%3D0.9,es;q%3D0.8",
    "cursors": {
      "after": "3AFsnAC0H9hes71BeRypbq"
    },
    "total": 6,
    "items": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/3AFsnAC0H9hes71BeRypbq"
        },
        "followers": {
          "href": null,
          "total": 252056
        },
        "genres": ["pov: indie"],
        "href": "https://api.spotify.com/v1/artists/3AFsnAC0H9hes71BeRypbq",
        "id": "3AFsnAC0H9hes71BeRypbq",
        "images": [
          {
            "url": "https://i.scdn.co/image/ab6761610000e5eb634aa69a50363eadd90d19fb",
            "height": 640,
            "width": 640
          },
          {
            "url": "https://i.scdn.co/image/ab67616100005174634aa69a50363eadd90d19fb",
            "height": 320,
            "width": 320
          },
          {
            "url": "https://i.scdn.co/image/ab6761610000f178634aa69a50363eadd90d19fb",
            "height": 160,
            "width": 160
          }
        ],
        "name": "Fish in a Birdcage",
        "popularity": 62,
        "type": "artist",
        "uri": "spotify:artist:3AFsnAC0H9hes71BeRypbq"
      }
    ]
  }
}
```

  -   Error Resonse Example
      -   Code: 401
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Error Resonse Example
      -   Code: 403
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Error Resonse Example
      -   Code: 429
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Example Request: No request body needed. The access token is retrieved from the session.
  -   Example Response:
      -   A successful response with the user's followed artists:
```
{
  "artists": {
    "href": "https://api.spotify.com/v1/me/following?type=artist&limit=1&locale=en-US,en;q%3D0.9,es;q%3D0.8",
    "limit": 1,
    "next": "https://api.spotify.com/v1/me/following?type=artist&limit=1&after=3AFsnAC0H9hes71BeRypbq&locale=en-US,en;q%3D0.9,es;q%3D0.8",
    "cursors": {
      "after": "3AFsnAC0H9hes71BeRypbq"
    },
    "total": 6,
    "items": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/3AFsnAC0H9hes71BeRypbq"
        },
        "followers": {
          "href": null,
          "total": 252056
        },
        "genres": ["pov: indie"],
        "href": "https://api.spotify.com/v1/artists/3AFsnAC0H9hes71BeRypbq",
        "id": "3AFsnAC0H9hes71BeRypbq",
        "images": [
          {
            "url": "https://i.scdn.co/image/ab6761610000e5eb634aa69a50363eadd90d19fb",
            "height": 640,
            "width": 640
          },
          {
            "url": "https://i.scdn.co/image/ab67616100005174634aa69a50363eadd90d19fb",
            "height": 320,
            "width": 320
          },
          {
            "url": "https://i.scdn.co/image/ab6761610000f178634aa69a50363eadd90d19fb",
            "height": 160,
            "width": 160
          }
        ],
        "name": "Fish in a Birdcage",
        "popularity": 62,
        "type": "artist",
        "uri": "spotify:artist:3AFsnAC0H9hes71BeRypbq"
      }
    ]
  }
}
```

### Route: `/saved-albums`
- Request Type: GET
- Purpose: Fetches the user's saved albums by making a GET request to Spotify's `/me/albums` endpoint using the stored access token.
- Request Body:
  - No request body is required for this endpoint.
- Response Format: JSON response containing the user's followed artists.
  -   Success Response Example:
      - Code: 200
      - Content:
```
{
  "href": "https://api.spotify.com/v1/me/albums?offset=0&limit=1&market=ES&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "items": [
    {
      "added_at": "2024-08-22T04:00:00Z",
      "album": {
        "album_type": "single",
        "total_tracks": 5,
        "is_playable": true,
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7x88WJNlL9qYtxrVzT0ah0"
        },
        "href": "https://api.spotify.com/v1/albums/7x88WJNlL9qYtxrVzT0ah0?market=ES&locale=en-US%2Cen%3Bq%3D0.9%2Ces%3Bq%3D0.8",
        "id": "7x88WJNlL9qYtxrVzT0ah0",
        "images": [
          {
            "url": "https://i.scdn.co/image/ab67616d0000b273361eb9419c0f3f6d09491200",
            "height": 640,
            "width": 640
          },
          {
            "url": "https://i.scdn.co/image/ab67616d00001e02361eb9419c0f3f6d09491200",
            "height": 300,
            "width": 300
          },
          {
            "url": "https://i.scdn.co/image/ab67616d00004851361eb9419c0f3f6d09491200",
            "height": 64,
            "width": 64
          }
        ],
        "name": "Ponyboy 2",
        "release_date": "2024-08-22",
        "release_date_precision": "day",
        "type": "album",
        "uri": "spotify:album:7x88WJNlL9qYtxrVzT0ah0",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
            },
            "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
            "id": "7p24SkpCc94fUK8rPK3JHm",
            "name": "Black Pontiac",
            "type": "artist",
            "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
          }
        ],
        "tracks": {
          "href": "https://api.spotify.com/v1/albums/7x88WJNlL9qYtxrVzT0ah0/tracks?offset=0&limit=50&market=ES&locale=en-US,en;q%3D0.9,es;q%3D0.8",
          "limit": 50,
          "next": null,
          "offset": 0,
          "previous": null,
          "total": 5,
          "items": [
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 218973,
              "explicit": false,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/1rveyk8hejlsYZ4q6Vgkkj"
              },
              "href": "https://api.spotify.com/v1/tracks/1rveyk8hejlsYZ4q6Vgkkj",
              "id": "1rveyk8hejlsYZ4q6Vgkkj",
              "is_playable": true,
              "name": "Blue Blood Baby",
              "preview_url": null,
              "track_number": 1,
              "type": "track",
              "uri": "spotify:track:1rveyk8hejlsYZ4q6Vgkkj",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 198981,
              "explicit": false,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/6NL4r7kh20KcmXsaGlREWU"
              },
              "href": "https://api.spotify.com/v1/tracks/6NL4r7kh20KcmXsaGlREWU",
              "id": "6NL4r7kh20KcmXsaGlREWU",
              "is_playable": true,
              "name": "Call Me Lover",
              "preview_url": null,
              "track_number": 2,
              "type": "track",
              "uri": "spotify:track:6NL4r7kh20KcmXsaGlREWU",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 140505,
              "explicit": true,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/3wiLKALlrb8UEnAK89Yib7"
              },
              "href": "https://api.spotify.com/v1/tracks/3wiLKALlrb8UEnAK89Yib7",
              "id": "3wiLKALlrb8UEnAK89Yib7",
              "is_playable": true,
              "name": "Go Go Hollywood",
              "preview_url": null,
              "track_number": 3,
              "type": "track",
              "uri": "spotify:track:3wiLKALlrb8UEnAK89Yib7",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 203250,
              "explicit": true,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/7JvjAIVPWwbKk75J18Qavz"
              },
              "href": "https://api.spotify.com/v1/tracks/7JvjAIVPWwbKk75J18Qavz",
              "id": "7JvjAIVPWwbKk75J18Qavz",
              "is_playable": true,
              "name": "I NEED PEACE BUT WAR IS FUN",
              "preview_url": null,
              "track_number": 4,
              "type": "track",
              "uri": "spotify:track:7JvjAIVPWwbKk75J18Qavz",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 259000,
              "explicit": true,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/1E9dHFIHeNiiUkGfYKfTiv"
              },
              "href": "https://api.spotify.com/v1/tracks/1E9dHFIHeNiiUkGfYKfTiv",
              "id": "1E9dHFIHeNiiUkGfYKfTiv",
              "is_playable": true,
              "name": "Slow Dance at the Disco - JY Remix",
              "preview_url": null,
              "track_number": 5,
              "type": "track",
              "uri": "spotify:track:1E9dHFIHeNiiUkGfYKfTiv",
              "is_local": false
            }
          ]
        },
        "copyrights": [
          {
            "text": "2024 Black Pontiac",
            "type": "C"
          },
          {
            "text": "2024 Black Pontiac",
            "type": "P"
          }
        ],
        "external_ids": {
          "upc": "198667406751"
        },
        "genres": [],
        "label": "Black Pontiac",
        "popularity": 20
      }
    }
  ],
  "limit": 1,
  "next": "https://api.spotify.com/v1/me/albums?offset=1&limit=1&market=ES&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "offset": 0,
  "previous": null,
  "total": 6
}
```

  -   Error Resonse Example
      -   Code: 401
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Error Resonse Example
      -   Code: 403
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Error Resonse Example
      -   Code: 429
      -   Content:
```
{
  "error": {
    "status": 400,
    "message": "string"
  }
}
```
  -   Example Request: No request body needed. The access token is retrieved from the session.
  -   Example Response:
      -   A successful response with the user's saved albums:
```
{
  "href": "https://api.spotify.com/v1/me/albums?offset=0&limit=1&market=ES&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "items": [
    {
      "added_at": "2024-08-22T04:00:00Z",
      "album": {
        "album_type": "single",
        "total_tracks": 5,
        "is_playable": true,
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7x88WJNlL9qYtxrVzT0ah0"
        },
        "href": "https://api.spotify.com/v1/albums/7x88WJNlL9qYtxrVzT0ah0?market=ES&locale=en-US%2Cen%3Bq%3D0.9%2Ces%3Bq%3D0.8",
        "id": "7x88WJNlL9qYtxrVzT0ah0",
        "images": [
          {
            "url": "https://i.scdn.co/image/ab67616d0000b273361eb9419c0f3f6d09491200",
            "height": 640,
            "width": 640
          },
          {
            "url": "https://i.scdn.co/image/ab67616d00001e02361eb9419c0f3f6d09491200",
            "height": 300,
            "width": 300
          },
          {
            "url": "https://i.scdn.co/image/ab67616d00004851361eb9419c0f3f6d09491200",
            "height": 64,
            "width": 64
          }
        ],
        "name": "Ponyboy 2",
        "release_date": "2024-08-22",
        "release_date_precision": "day",
        "type": "album",
        "uri": "spotify:album:7x88WJNlL9qYtxrVzT0ah0",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
            },
            "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
            "id": "7p24SkpCc94fUK8rPK3JHm",
            "name": "Black Pontiac",
            "type": "artist",
            "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
          }
        ],
        "tracks": {
          "href": "https://api.spotify.com/v1/albums/7x88WJNlL9qYtxrVzT0ah0/tracks?offset=0&limit=50&market=ES&locale=en-US,en;q%3D0.9,es;q%3D0.8",
          "limit": 50,
          "next": null,
          "offset": 0,
          "previous": null,
          "total": 5,
          "items": [
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 218973,
              "explicit": false,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/1rveyk8hejlsYZ4q6Vgkkj"
              },
              "href": "https://api.spotify.com/v1/tracks/1rveyk8hejlsYZ4q6Vgkkj",
              "id": "1rveyk8hejlsYZ4q6Vgkkj",
              "is_playable": true,
              "name": "Blue Blood Baby",
              "preview_url": null,
              "track_number": 1,
              "type": "track",
              "uri": "spotify:track:1rveyk8hejlsYZ4q6Vgkkj",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 198981,
              "explicit": false,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/6NL4r7kh20KcmXsaGlREWU"
              },
              "href": "https://api.spotify.com/v1/tracks/6NL4r7kh20KcmXsaGlREWU",
              "id": "6NL4r7kh20KcmXsaGlREWU",
              "is_playable": true,
              "name": "Call Me Lover",
              "preview_url": null,
              "track_number": 2,
              "type": "track",
              "uri": "spotify:track:6NL4r7kh20KcmXsaGlREWU",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 140505,
              "explicit": true,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/3wiLKALlrb8UEnAK89Yib7"
              },
              "href": "https://api.spotify.com/v1/tracks/3wiLKALlrb8UEnAK89Yib7",
              "id": "3wiLKALlrb8UEnAK89Yib7",
              "is_playable": true,
              "name": "Go Go Hollywood",
              "preview_url": null,
              "track_number": 3,
              "type": "track",
              "uri": "spotify:track:3wiLKALlrb8UEnAK89Yib7",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 203250,
              "explicit": true,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/7JvjAIVPWwbKk75J18Qavz"
              },
              "href": "https://api.spotify.com/v1/tracks/7JvjAIVPWwbKk75J18Qavz",
              "id": "7JvjAIVPWwbKk75J18Qavz",
              "is_playable": true,
              "name": "I NEED PEACE BUT WAR IS FUN",
              "preview_url": null,
              "track_number": 4,
              "type": "track",
              "uri": "spotify:track:7JvjAIVPWwbKk75J18Qavz",
              "is_local": false
            },
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7p24SkpCc94fUK8rPK3JHm"
                  },
                  "href": "https://api.spotify.com/v1/artists/7p24SkpCc94fUK8rPK3JHm",
                  "id": "7p24SkpCc94fUK8rPK3JHm",
                  "name": "Black Pontiac",
                  "type": "artist",
                  "uri": "spotify:artist:7p24SkpCc94fUK8rPK3JHm"
                }
              ],
              "disc_number": 1,
              "duration_ms": 259000,
              "explicit": true,
              "external_urls": {
                "spotify": "https://open.spotify.com/track/1E9dHFIHeNiiUkGfYKfTiv"
              },
              "href": "https://api.spotify.com/v1/tracks/1E9dHFIHeNiiUkGfYKfTiv",
              "id": "1E9dHFIHeNiiUkGfYKfTiv",
              "is_playable": true,
              "name": "Slow Dance at the Disco - JY Remix",
              "preview_url": null,
              "track_number": 5,
              "type": "track",
              "uri": "spotify:track:1E9dHFIHeNiiUkGfYKfTiv",
              "is_local": false
            }
          ]
        },
        "copyrights": [
          {
            "text": "2024 Black Pontiac",
            "type": "C"
          },
          {
            "text": "2024 Black Pontiac",
            "type": "P"
          }
        ],
        "external_ids": {
          "upc": "198667406751"
        },
        "genres": [],
        "label": "Black Pontiac",
        "popularity": 20
      }
    }
  ],
  "limit": 1,
  "next": "https://api.spotify.com/v1/me/albums?offset=1&limit=1&market=ES&locale=en-US,en;q%3D0.9,es;q%3D0.8",
  "offset": 0,
  "previous": null,
  "total": 6
}
```