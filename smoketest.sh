#!/bin/bash

# Define the base URL for the Flask API
BASE_URL="http://localhost:5001/api"

# Flag to control whether to echo JSON output
ECHO_JSON=false

# Parse command-line arguments
while [ "$#" -gt 0 ]; do
  case $1 in
    --echo-json) ECHO_JSON=true ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

###############################################
#
# Health checks
#
###############################################

# Function to check the health of the service
check_health() {
  echo "Checking health status..."
  curl -s -X GET "$BASE_URL/health" | grep -q '"status": "healthy"'
  if [ $? -eq 0 ]; then
    echo "Service is healthy."
  else
    echo "Health check failed."
    exit 1
  fi
}

##############################################
#
# User management
#
##############################################

# Function to create a user
create_user() {
  echo "Creating a new user..."
  curl -s -X POST "$BASE_URL/create-user" -H "Content-Type: application/json" \
    -d '{"username":"testuser", "password":"password123"}' | grep -q '"status": "user added"'
  if [ $? -eq 0 ]; then
    echo "User created successfully."
  else
    echo "Failed to create user."
    exit 1
  fi
}

# Function to log in a user
login_user() {
  echo "Logging in user..."
  response=$(curl -s -X POST "$BASE_URL/login" -H "Content-Type: application/json" \
    -d '{"username":"testuser", "password":"password123"}')
  if echo "$response" | grep -q '"message": "User testuser logged in successfully."'; then
    echo "User logged in successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Login Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to log in user."
    if [ "$ECHO_JSON" = true ]; then
      echo "Error Response JSON:"
      echo "$response" | jq .
    fi
    exit 1
  fi
}

# Function to log out a user
logout_user() {
  echo "Logging out user..."
  response=$(curl -s -X POST "$BASE_URL/logout" -H "Content-Type: application/json" \
    -d '{"username":"testuser"}')
  if echo "$response" | grep -q '"message": "User testuser logged out successfully."'; then
    echo "User logged out successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Logout Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to log out user."
    if [ "$ECHO_JSON" = true ]; then
      echo "Error Response JSON:"
      echo "$response" | jq .
    fi
    exit 1
  fi
}

# Function to check password
check_password_test() {
  echo "Testing check_password..."
  response=$(curl -s -X POST "$BASE_URL/check-password" -H "Content-Type: application/json" \
    -d '{"username":"testuser", "password":"password123"}')
  if echo "$response" | grep -q '"password_match": true'; then
    echo "Password check passed successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Check Password Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed password check."
    exit 1
  fi
}


# Function to test retrieving a user ID by username
get_id_by_username_test() {
  echo "Testing get_id_by_username..."
  response=$(curl -s -X GET "$BASE_URL/get-id-by-username?username=testuser")
  if echo "$response" | grep -q '"user_id"'; then
    echo "User ID retrieved successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Get ID by Username Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to retrieve user ID."
    exit 1
  fi
}

# Function to test updating a password
update_password_test() {
  echo "Testing update_password..."
  response=$(curl -s -X PUT "$BASE_URL/update-password" -H "Content-Type: application/json" \
    -d '{"username":"testuser", "new_password":"newpassword123"}')
  if echo "$response" | grep -q '"status": "password updated"'; then
    echo "Password updated successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Update Password Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to update password."
    exit 1
  fi
}

# Function to update user profile
update_user_profile() {
  echo "Updating user profile..."
  response=$(curl -s -X PUT "$BASE_URL/update-profile" -H "Content-Type: application/json" \
    -d '{"username":"testuser", "new_email":"testuser@example.com"}')
  if echo "$response" | grep -q '"status": "profile updated"'; then
    echo "User profile updated successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Update Profile Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to update user profile."
    exit 1
  fi
}

# Function to test deleting a user
delete_user_test() {
  echo "Testing delete_user..."
  response=$(curl -s -X DELETE "$BASE_URL/delete-user" -H "Content-Type: application/json" \
    -d '{"username":"testuser"}')
  if echo "$response" | grep -q '"status": "user deleted"'; then
    echo "User deleted successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Delete User Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to delete user."
    exit 1
  fi
}
##############################################
#
# Spotify Functions
#
##############################################

# Function to test fetching playlists
get_playlists_test() {
  echo "Testing playlists..."
  response=$(curl -s -X GET "$BASE_URL/spotify/playlists")
  if echo "$response" | grep -q '"items"'; then
    echo "Playlists fetched successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Playlists Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to fetch playlists."
    exit 1
  fi
}

# Function to test fetching top items
get_top_items_test() {
  echo "Testing get_top_items..."
  response=$(curl -s -X GET "$BASE_URL/spotify/top-items?type=artists&time_range=medium_term&limit=10&offset=0")
  if echo "$response" | grep -q '"items"'; then
    echo "Top items fetched successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Top Items Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to fetch top items."
    exit 1
  fi
}

# Function to test fetching followed artists
get_followed_artists_test() {
  echo "Testing get_followed_artists..."
  response=$(curl -s -X GET "$BASE_URL/spotify/followed-artists?limit=10")
  if echo "$response" | grep -q '"artists"'; then
    echo "Followed artists fetched successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Followed Artists Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to fetch followed artists."
    exit 1
  fi
}

# Function to test fetching saved albums
get_saved_albums_test() {
  echo "Testing get_saved_albums..."
  response=$(curl -s -X GET "$BASE_URL/spotify/saved-albums?limit=10&offset=0")
  if echo "$response" | grep -q '"albums"'; then
    echo "Saved albums fetched successfully."
    if [ "$ECHO_JSON" = true ]; then
      echo "Saved Albums Response JSON:"
      echo "$response" | jq .
    fi
  else
    echo "Failed to fetch saved albums."
    exit 1
  fi
}

# Run all the steps in order

check_health
create_user
login_user
update_user_profile
check_password_test
update_password_test
get_id_by_username_test
get_playlists_test
get_top_items_test
get_followed_artists_test
get_saved_albums_test
delete_user_test
logout_user

echo "All tests completed successfully!"
