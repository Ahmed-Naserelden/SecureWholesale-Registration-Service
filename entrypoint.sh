#!/bin/bash

# Wait for the database to become available
apt update \ 
    apt upgrade
until curl --silent --fail http://mongo:27017
do
  echo "Waiting for database connection..."
  # Sleep for 5 seconds before retrying
  sleep 5
done

# Apply Django database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
