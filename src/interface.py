from model import TrainTicketRecommender

# Load trained model
recommender = TrainTicketRecommender()
recommender.load_model()

# Get user input and generate recommendations
user_query = "Business class ticket from CityA to CityB with a window seat"
recommendations = recommender.recommend_tickets(user_query, top_k=5)

# Display recommendations
print("\n Recommended Tickets:")
for idx, rec in enumerate(recommendations, 1):
    print(f"{idx}. {rec}")
