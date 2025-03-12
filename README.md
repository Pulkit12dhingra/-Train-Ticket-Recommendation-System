# 🚆 Train Ticket Recommendation System
A **machine learning-based recommendation system** that suggests train tickets based on **user preferences, booking history, and real-time pricing trends**.

✅ Uses **LangChain embeddings & FAISS** for efficient recommendations.  
✅ Provides a **FastAPI server** for real-time ticket suggestions.  
✅ Includes an **interactive CLI** for manual recommendations.  
✅ Fully tested with **`pytest`** to ensure reliability.  

---

## 📂 Project Structure

✅ Uses LangChain embeddings & FAISS for efficient recommendations.
✅ Provides a FastAPI server for real-time ticket suggestions.
✅ Includes an interactive CLI for manual recommendations.
✅ Fully tested with pytest to ensure reliability.

📂 Project Structure

📦 train-ticket-recommendation
│
├── data/  
│   ├── generate_data.py            # Script to generate synthetic data  
│
├── notebooks/  
│   ├── 1_data_exploration.ipynb    # EDA & visualization  
│   ├── 2_model_training.ipynb      # Training & evaluation  
│
├── src/  
│   ├── model.py                    # Machine Learning model (FAISS + LangChain)  
│   ├── train.py                    # Script to train & save the model  
│   ├── inference.py                 # Script to load model & make predictions  
│   ├── api.py                      # FastAPI server for recommendations  
│
├── tests/  
│   ├── test_model.py                # Unit tests for the recommendation model  
│   ├── test_api.py                   # API tests using pytest & FastAPI  
│
├── requirements.txt              # Dependencies  
│
├── main.py                          # Entry point (Train, CLI Recommend, Start API)  
├── README.md                         # Project documentation  
└── .gitignore                        # Ignore unnecessary files  

## 🚀 Getting Started
1️⃣ Install Dependencies
Make sure you have Python 3.8+ installed. Then, install the required packages:

`pip install -r requirements.txt`

2️⃣ Generate Data

Run this script to create synthetic datasets:

`python data/generate_data.py`

💾 This generates CSV files in the data/generated/ directory.

3️⃣ Train the Recommendation Model
Train the model and save it as a FAISS index:
`python main.py --train`

✅ The trained model will be saved in deployment/faiss_index/.

4️⃣ Get Recommendations
📌 Interactive CLI Mode
Run the system in interactive mode and enter your travel preferences:
`python main.py --recommend`

💡 Example:

🔍 Enter your travel preference: Business class ticket from CityA to CityB with a window seat
🎟️ Recommended Tickets:
1. {Train Name: "Express", Class: "Business", Departure: "CityA", Arrival: "CityB", Price: 50}
2. {Train Name: "Superfast", Class: "Business", Departure: "CityA", Arrival: "CityB", Price: 55}
🔹 Type exit to close the CLI.

5️⃣ Start the API
Run the FastAPI server:
`python main.py --api`

🚀 The API will be available at http://127.0.0.1:8000

6️⃣ Make API Requests
📌 Get API Status
`curl -X 'GET' 'http://127.0.0.1:8000/'`
Response:
{"message": "🚀 Train Ticket Recommendation API is running!"}
📌 Get Ticket Recommendations
`curl -X 'POST' 'http://127.0.0.1:8000/recommend' \
     -H 'Content-Type: application/json' \
     -d '{"user_input": "Business class from CityA to CityB", "top_k": 5}'`

Response:

json
`{
  "status": "success",
  "recommendations": [
    {"Train Name": "Express", "Class": "Business", "Departure": "CityA", "Arrival": "CityB", "Price": 50},
    {"Train Name": "Superfast", "Class": "Business", "Departure": "CityA", "Arrival": "CityB", "Price": 55}
  ]
}`

🛠 Running Tests
Run all tests using:
pytest tests/
🧪 Test Model
`pytest tests/test_model.py`
🧪 Test API
`pytest tests/test_api.py`
✅ Ensures model works correctly
✅ Ensures API handles requests properly


📜 How the System Works
1️⃣ Prepares Data → Cleans, preprocesses, and extracts features from CSV files.
2️⃣ Embeds Features → Uses LangChain embeddings for numerical representation.
3️⃣ Stores in FAISS → Uses FAISS for fast similarity search.
4️⃣ Retrieves Recommendations → Finds nearest top-k matches for user input.
5️⃣ Provides API & CLI → Users can get recommendations via API or interactive CLI.

📌 Technologies Used
✅ Python → Core programming language
✅ LangChain → Text embedding model for recommendations
✅ FAISS → Vector database for fast retrieval
✅ FastAPI → REST API for ticket recommendations
✅ pytest → Unit testing framework

🚀 Happy Coding! 🎉