# Use an official Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set environment variables (optional, modify as needed)
ENV PYTHONUNBUFFERED=1
ENV API_BASE_URL="https://dummyjson.com"

# Run Pytest when the container starts
CMD ["pytest", "--tb=short", "--disable-warnings", "--junitxml=report.xml"]
