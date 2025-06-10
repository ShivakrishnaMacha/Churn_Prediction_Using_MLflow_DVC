FROM python:3.9-slim

# Copy all files to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port (Heroku uses PORT env variable, but Docker build needs a number)
EXPOSE 5000

# Run app using Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
