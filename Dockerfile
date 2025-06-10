FROM python:3.7-slim

# Avoid interactive prompts during dependencies install
ENV DEBIAN_FRONTEND=noninteractive

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose the port (Heroku uses dynamic $PORT)
EXPOSE 5000

# Run using Gunicorn with dynamic port from Heroku
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:$PORT", "app:app"]
