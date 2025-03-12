import pandas as pd

# Load the CSV file
file_path = "feedback_data.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
df.head()

import random

# Sample feedback relevant to train ride experiences
train_feedback_samples = [
    "The train was on time and the journey was smooth.",
    "Seats were comfortable, but the cleanliness could be improved.",
    "The staff was helpful, but the train was delayed.",
    "Great experience! The train was clean and punctual.",
    "The ride was bumpy, and the restroom was not well-maintained.",
    "Had trouble finding my seat, but the ride itself was pleasant.",
    "The food service was excellent, and the seats were spacious.",
    "Too noisy, especially near the engine section.",
    "Loved the scenic views along the route.",
    "The Wi-Fi was slow, but otherwise, a comfortable ride.",
    "Air conditioning was too cold, but the train was well-maintained.",
    "Easy booking process and smooth journey.",
    "Had difficulty understanding the announcements.",
    "The train was late, but the staff was courteous.",
    "Luggage storage was limited and inconvenient.",
    "Great legroom, but the train was crowded.",
    "Seats were hard and uncomfortable for a long journey.",
    "Announcements were clear, and the ride was peaceful.",
    "The train was packed, making it hard to move around.",
    "Enjoyed the journey, but the food options were limited."
]

# Update the 'Feedback' column with randomly selected relevant feedback
df["Feedback"] = [random.choice(train_feedback_samples) for _ in range(len(df))]

df.to_csv("feedback_data.csv", index=False)

# Display the updated DataFrame
df.head()