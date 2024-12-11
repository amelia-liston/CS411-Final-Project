import pytest
import requests

from meal_max.models.personal_model import PersonalModel


@pytest.fixture
def mock_spotify_api(mocker):
    """Fixture to mock Spotify API calls."""
    mock_response = mocker.Mock()
    mocker.patch("requests.get", return_value=mock_response)
    return mock_response


def test_get_top_items_success(mock_spotify_api):
    """Test successful retrieval of top items."""
    mock_spotify_api.json.return_value = {"items": [{"name": "Artist 1"}, {"name": "Artist 2"}]}
    mock_spotify_api.status_code = 200

    personal_model = PersonalModel("test_token")
    result = personal_model.get_top_items(type="artists", time_range="medium_term", limit=10, offset=0)

    assert result == {"items": [{"name": "Artist 1"}, {"name": "Artist 2"}]}, "Expected top items not returned"
    requests.get.assert_called_once_with(
        f"{personal_model.BASE_URL}/me/top/artists",
        headers={"Authorization": "Bearer test_token"},
        params={"time_range": "medium_term", "limit": 10, "offset": 0},
        timeout=5
    )


def test_get_top_items_invalid_type():
    """Test error when trying to get top items with invalid type."""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid item type: invalid_type"):
        personal_model.get_top_items(type="invalid_type")

def test_get_top_items_invalid_time_range():
    """Test error when trying to get top items with invalid time range"""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid time range: invalid_term"):
        personal_model.get_top_items(type="artists",time_range="invalid_term")

def test_get_top_items_invalid_limit():
    """Test error when trying to get top items with invalid limit"""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid item limit: 51"):
        personal_model.get_top_items(type="artists",limit=51)

def test_get_top_items_invalid_offset():
    """Test error when trying to get top items with invalid offset"""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid offset: -1"):
        personal_model.get_top_items(type="artists",offset=-1)

def test_get_top_items_timeout(mocker):
    """Test timeout error."""
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)

    personal_model = PersonalModel("test_token")

    with pytest.raises(RuntimeError, match="Request to Spotify timed out."):
        personal_model.get_top_items(type="artists")

def test_get_top_items_request_failure(mocker):
    """Test request failure handling."""
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error"))

    personal_model = PersonalModel("test_token")

    with pytest.raises(RuntimeError, match="Request to Spotify failed: Connection error"):
        personal_model.get_top_items(type="artists")

def test_get_followed_artists_invalid_limit():
    """Test error when trying to get top items with invalid limit"""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid item limit: 51"):
        personal_model.get_followed_artists(limit=51)

def test_get_followed_artists_success(mock_spotify_api):
    """Test successful retrieval of followed artists."""
    mock_spotify_api.json.return_value = {"artists": {"items": {"name": "Artist 1"}}}
    mock_spotify_api.status_code = 200

    personal_model = PersonalModel("test_token")
    result = personal_model.get_followed_artists(limit=10, after=None)

    assert result == {"artists": {"items": {"name": "Artist 1"}}}, "Expected followed artists not returned"
    requests.get.assert_called_once_with(
        f"{personal_model.BASE_URL}/me/following",
        headers={"Authorization": "Bearer test_token"},
        params={"type": 'artist', "limit": 10},
    )

def test_get_followed_artists_timeout(mocker):
    """Test timeout handling."""
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)

    personal_model = PersonalModel("test_token")

    with pytest.raises(RuntimeError, match="Request to Spotify timed out."):
        personal_model.get_followed_artists()

def test_get_followed_artists_request_failure(mocker):
    """Test request failure handling."""
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error"))

    personal_model = PersonalModel("test_token")

    with pytest.raises(RuntimeError, match="Request to Spotify failed: Connection error"):
        personal_model.get_followed_artists()

def test_get_saved_albums_invalid_limit():
    """Test error when trying to get saved albums with invalid limit"""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid item limit: 51"):
        personal_model.get_saved_albums(limit=51)

def test_get_saved_albums_invalid_offset():
    """Test error when trying to get saved albums with invalid offset"""
    personal_model = PersonalModel("test_token")

    with pytest.raises(ValueError, match="Invalid offset: -1"):
        personal_model.get_saved_albums(offset=-1)

def test_get_saved_albums_success(mock_spotify_api):
    """Test successful retrieval of saved albums."""
    mock_spotify_api.json.return_value = {"items": [{"album": {"name": "Album 1"}}]}
    mock_spotify_api.status_code = 200

    personal_model = PersonalModel("test_token")
    result = personal_model.get_saved_albums(limit=10, offset=0)

    assert result == {"items": [{"album": {"name": "Album 1"}}]}, "Expected saved albums not returned"
    requests.get.assert_called_once_with(
        f"{personal_model.BASE_URL}/me/albums",
        headers={"Authorization": "Bearer test_token"},
        params={"limit": 10, "offset": 0},
        timeout=5
    )

def test_get_saved_albums_timeout(mocker):
    """Test timeout handling."""
    mocker.patch("requests.get", side_effect=requests.exceptions.Timeout)

    personal_model = PersonalModel("test_token")

    with pytest.raises(RuntimeError, match="Request to Spotify timed out."):
        personal_model.get_saved_albums()

def test_get_saved_albums_request_failure(mocker):
    """Test request failure handling."""
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error"))

    personal_model = PersonalModel("test_token")

    with pytest.raises(RuntimeError, match="Request to Spotify failed: Connection error"):
        personal_model.get_saved_albums()


