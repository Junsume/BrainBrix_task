# Use a lightweight Python image
FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Default command (can be overridden in docker-compose.yml)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]