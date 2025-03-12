import pytest
from model import TrainTicketRecommender

# Initialize recommender system
recommender = TrainTicketRecommender()

def test_model_loading():
    """
    Test if the model loads correctly.
    """
    try:
        recommender.load_model()
        assert recommender.vector_store is not None, " Model failed to load!"
    except Exception as e:
        pytest.fail(f" Model loading failed with error: {e}")

def test_recommendation_output():
    """
    Test if the model returns valid recommendations.
    """
    recommender.load_model()
    user_query = "Business class ticket from CityA to CityB with a window seat"
    recommendations = recommender.recommend_tickets(user_query, top_k=3)
    
    assert isinstance(recommendations, list), " Output is not a list!"
    assert len(recommendations) > 0, " No recommendations returned!"
    assert isinstance(recommendations[0], dict), " Recommendation format is incorrect!"

def test_empty_input():
    """
    Test model behavior for an empty input query.
    """
    recommender.load_model()
    recommendations = recommender.recommend_tickets("", top_k=3)

    assert isinstance(recommendations, list), " Empty input should return a list!"
    assert len(recommendations) == 0, " Empty input should return no recommendations!"

def test_invalid_top_k():
    """
    Test if the model handles invalid top_k values gracefully.
    """
    recommender.load_model()
    user_query = "Sleeper class from CityE to CityF"
    
    with pytest.raises(ValueError):
        recommender.recommend_tickets(user_query, top_k=-1)

# Run tests if executed directly
if __name__ == "__main__":
    pytest.main()
