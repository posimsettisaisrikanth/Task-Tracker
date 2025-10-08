# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose Streamlit UI port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.enableCORS", "false", "--server.port", "8501", "--server.address", "0.0.0.0"]
