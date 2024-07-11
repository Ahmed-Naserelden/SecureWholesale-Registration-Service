#!/bin/sh

# Apply database migrations
echo "Changing DataBase settings ..."
SETTINGS_FILE="wholesale/settings.py"
VARIABLE_NAME="DATABASE_HOST"
NEW_VALUE="db"

sed -i "s/\($VARIABLE_NAME *= *\).*/\1\"$NEW_VALUE\"/" $SETTINGS_FILE
echo "$VARIABLE_NAME updated to $NEW_VALUE in $SETTINGS_FILE"

echo "Applying database migrations..."
python manage.py migrate

# Start server
echo "Starting server..."
exec "$@"