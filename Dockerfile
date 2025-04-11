FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libreoffice \
    && apt-get clean

# Set working dir
WORKDIR /app

# Copy your code
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start the app
CMD ["streamlit", "run", "main.py"]
