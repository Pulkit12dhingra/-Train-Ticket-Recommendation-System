import os
import argparse
from train import TrainTicketRecommender
import uvicorn
from api import app

# Define paths
MODEL_PATH = "../deployment/faiss_index"

def train_model():
    """
    Train the recommendation model and save it.
    """
    import pandas as pd
    file_path = "../data/generated/booking_history.csv"

    # Load and preprocess data
    df = pd.read_csv(file_path)
    df.fillna("Unknown", inplace=True)
    df["combined_features"] = df.astype(str).agg(" ".join, axis=1)

    # Train and save model
    recommender = TrainTicketRecommender()
    recommender.train_model(df)
    recommender.save_model()

def recommend_interactively():
    """
    Provide an interactive CLI for recommendations.
    """
    recommender = TrainTicketRecommender()

    # Ensure model is trained
    if not os.path.exists(MODEL_PATH):
        print(" Model not found! Training now...")
        train_model()

    # Load model
    recommender.load_model()

    while True:
        user_input = input("\n🔍 Enter your travel preference (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print(" Exiting recommendation system.")
            break
        
        recommendations = recommender.recommend_tickets(user_input, top_k=5)
        
        if recommendations:
            print("\ Recommended Tickets:")
            for idx, rec in enumerate(recommendations, 1):
                print(f"{idx}. {rec}")
        else:
            print(" No suitable recommendations found!")

def start_api():
    """
    Start the FastAPI server.
    """
    print("🚀 Starting FastAPI server at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Ticket Recommendation System")
    parser.add_argument("--train", action="store_true", help="Train and save the model")
    parser.add_argument("--recommend", action="store_true", help="Run interactive recommendations")
    parser.add_argument("--api", action="store_true", help="Start FastAPI server")

    args = parser.parse_args()

    if args.train:
        print(" Training the model...")
        train_model()
        print(" Model training complete.")
    elif args.recommend:
        recommend_interactively()
    elif args.api:
        start_api()
    else:
        print(" No valid option provided. Use --help for usage details.")
