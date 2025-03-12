import pytest
from fastapi.testclient import TestClient
from api import app

# Initialize test client
client = TestClient(app)

def test_api_root():
    """
    Test if API root endpoint is accessible.
    """
    response = client.get("/")
    assert response.status_code == 200, " API root is not accessible!"
    assert response.json()["message"] == " Train Ticket Recommendation API is running!"

def test_valid_recommendation():
    """
    Test if the recommendation endpoint returns valid recommendations.
    """
    response = client.post("/recommend", json={"user_input": "Business class from CityA to CityB", "top_k": 3})
    assert response.status_code == 200, " Failed to get recommendations!"
    assert response.json()["status"] == "success", " API did not return success!"
    assert isinstance(response.json()["recommendations"], list), " Recommendations format is incorrect!"

def test_empty_recommendation():
    """
    Test API behavior for an empty query.
    """
    response = client.post("/recommend", json={"user_input": "", "top_k": 3})
    assert response.status_code == 200, " API should handle empty queries!"
    assert isinstance(response.json()["recommendations"], list), " API should return an empty list for empty queries!"
    assert len(response.json()["recommendations"]) == 0, " Empty query should return no recommendations!"

def test_invalid_top_k():
    """
    Test API behavior for an invalid `top_k` parameter.
    """
    response = client.post("/recommend", json={"user_input": "Sleeper class ticket", "top_k": -5})
    assert response.status_code == 200, " API should not break for invalid top_k!"
    assert response.json()["status"] == "error", " API should return an error for invalid top_k!"

# Run tests if executed directly
if __name__ == "__main__":
    pytest.main()
