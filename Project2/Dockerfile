# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app and data
COPY app.py /app/app.py
COPY seed.json /app/seed.json
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
