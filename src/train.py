import pandas as pd
from model import TrainTicketRecommender

# Load data
file_path = "../data/booking_history.csv"
df = pd.read_csv(file_path)

# Preprocess data (ensure combined_features column exists)
df.fillna("Unknown", inplace=True)
df["combined_features"] = df.astype(str).agg(" ".join, axis=1)

# Initialize and train model
recommender = TrainTicketRecommender()
recommender.train_model(df)

# Save trained model
recommender.save_model()
print("✅ Model training complete and saved.")
