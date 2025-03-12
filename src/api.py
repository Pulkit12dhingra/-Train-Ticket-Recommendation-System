from fastapi import FastAPI
from pydantic import BaseModel
from model import TrainTicketRecommender

# Initialize API & model
app = FastAPI(title="Train Ticket Recommendation API")
recommender = TrainTicketRecommender()
recommender.load_model()

class QueryRequest(BaseModel):
    user_input: str
    top_k: int = 5

@app.post("/recommend")
def get_recommendations(request: QueryRequest):
    """
    Recommend train tickets based on user query.
    """
    try:
        recommendations = recommender.recommend_tickets(request.user_input, request.top_k)
        return {"status": "success", "recommendations": recommendations}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def root():
    return {"message": " Train Ticket Recommendation API is running!"}
