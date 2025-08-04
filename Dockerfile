# Use a stable base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

# Copy project files
COPY . /app/

# Run the bot
CMD ["python", "main.py"]
