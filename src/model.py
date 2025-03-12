import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os

class TrainTicketRecommender:
    def __init__(self, model_path="../deployment/faiss_index"):
        self.model_path = model_path
        self.embedding_model = OpenAIEmbeddings()
        self.vector_store = None

    def train_model(self, data):
        """
        Train the FAISS recommendation model using LangChain embeddings.
        """
        train_data = data["combined_features"].tolist()
        embeddings = self.embedding_model.embed_documents(train_data)
        self.vector_store = FAISS.from_embeddings(embeddings)

    def save_model(self):
        """
        Save the FAISS index to disk.
        """
        if self.vector_store:
            self.vector_store.save_local(self.model_path)
            print(f"✅ Model saved at {self.model_path}")
        else:
            print("⚠️ No model found. Train the model first.")

    def load_model(self):
        """
        Load the FAISS model from disk.
        """
        if os.path.exists(self.model_path):
            self.vector_store = FAISS.load_local(self.model_path)
            print("✅ Model loaded successfully.")
        else:
            raise FileNotFoundError("❌ Model file not found! Train the model first.")

    def recommend_tickets(self, user_input, top_k=5):
        """
        Recommend top-k train tickets based on user input query.
        """
        if not self.vector_store:
            raise ValueError("❌ Model is not loaded! Call `load_model()` first.")
        
        input_embedding = self.embedding_model.embed_query(user_input)
        similar_docs = self.vector_store.similarity_search_by_vector(input_embedding, k=top_k)

        recommendations = [doc.metadata for doc in similar_docs]
        return recommendations
