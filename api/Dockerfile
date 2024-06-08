# Use the official Python image.
FROM python:3.10-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--workers", "3", "api.wsgi:application", "--bind", "0.0.0.0:8000"]
