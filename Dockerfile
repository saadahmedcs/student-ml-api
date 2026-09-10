# Pinned official lightweight base image
FROM python:3.11-slim

# Establish explicit working directory
WORKDIR /app

# Copy dependency definition first to leverage layer caching
COPY requirements.txt .

# Install dependencies without retaining pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy application assets and tests
COPY . .

# Expose port matching application configuration
EXPOSE 5000

# Start Flask application directly bound to 0.0.0.0:5000
CMD ["python", "app.py"]