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
    """Test timeout handling."""
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
