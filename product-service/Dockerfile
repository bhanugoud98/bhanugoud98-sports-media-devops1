# product-service/Dockerfile
FROM python:3.11-slim

# set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
