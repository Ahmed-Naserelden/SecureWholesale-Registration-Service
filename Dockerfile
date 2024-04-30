# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /code
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install MongoDB
RUN apt-get update && && apt-get upgrade -y && apt-get install -y mongodb

RUN python manage.py migrate

# Expose the port your Django app runs on
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
