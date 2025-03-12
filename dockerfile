# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model (if not already trained)
RUN python main.py --train

# Expose API port
EXPOSE 8000

# Run the FastAPI server
CMD ["python", "main.py", "--api"]
