# Get Python base image
FROM python:3.10.16-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY requirements.txt .
COPY main.py .
COPY model_2.keras .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port the API runs on
EXPOSE 8000

# Run the application
CMD ["python3", "main.py"]
