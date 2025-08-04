# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies for building audio tools
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Optional: Expose a port (not necessary for a worker bot, but useful for testing)
EXPOSE 8080

# Start the bot
CMD ["python3", "main.py"]
