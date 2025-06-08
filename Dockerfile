FROM python:3.7

# Copy all files to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port (Heroku uses PORT env variable, but Docker build needs a number)
EXPOSE 5000

# Run  app using Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
