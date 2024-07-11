# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /code
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install MongoDB
RUN apt-get update && apt-get upgrade -y

# Run entrypoint script but first make it excutable
RUN chmod +x ./entrypoint.sh

# Run entrypoint.sh when the container launches
ENTRYPOINT ["./entrypoint.sh"]
