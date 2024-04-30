## Whole Sale 


## Table of Contents

- [Requirements](#requirements)
- [MongoDB Configuration](#MongoDB-Configuration)
- [Installation](#installation)

## Requirements

List the prerequisites and dependencies required to run the project. Include links or version numbers ([Installation](#installation)).

- Python (3.11.4)
- Django (4.1.13)
- djangorestframework (3.14.0)
- pymongo (3.12.3)


## MongoDB Configuration
This project uses `MongoDB` as its database backend. Ensure that `MongoDB` is installed and running on your system.

### Database and Collections

The project interacts with a MongoDB database named `mydb`:

```bash
# Connect to MongoDB shell
mongo

# Create the mydb database
use mydb

# Create collections (users, organizations, permissions)
db.createCollection("users")
db.createCollection("organizations")
db.createCollection("permissions")
```

which contains the following `collections`:

- `users`: Stores information about users.
- `organizations`: Stores information about organizations. 
- `permissions`: Stores information about permissions.

Ensure that these collections are present in your `MongoDB` database for the project to function correctly.

## Installation

Provide step-by-step instructions to set up the project locally.

1. **Clone the Repository**: Begin by cloning the repository to your local machine:
   ```bash
   git clone https://github.com/Ahmed-Naserelden/Wholesale-Authentication-Api.git
    ```

2. **Navigate to the Project Directory**: Move into the project directory:
    ```bash
    cd Wholesale-Authentication-Api
    ```

3. **Create a Virtual Environment (Optional but Recommended)**: It's good practice to work within a virtual environment to keep your dependencies isolated:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**: Activate the virtual environment to start using it:

    - On Windows:
    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

5. **Install Dependencies**: Use pip to install the project dependencies listed in the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```

    Once installed, configure your Django project's `wholesale/settings.py` file to use MongoDB as the database backend. Here's an example configuration:

    > **Note**: 
    >
    > For local development, the project is configured to connect to a MongoDB database running on localhost. **Don't** edit anything in the database configuration `wholesale/settings.py` if you intend to connect with the local environment. 
    ```python
    # wholesale/settings.py
    
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'mydb',  # Specify the name of your MongoDB database
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'your_cluster_name.mongodb.net',  # MongoDB Cloud host
                'port': 27017,  # MongoDB default port
                'username': 'your_username',  # MongoDB username
                'password': 'your_password',  # MongoDB password
                'authSource': 'admin',  # Authentication database
                'ssl': True,  # Enable SSL encryption
                'retryWrites': True,  # Enable retryable writes
                'retryReads': True,  # Enable retryable reads
            }
        }
    }

    ```

6. **Migrate the Database**: Run database migrations to create necessary tables:
    ```bash
    python manage.py migrate
    ```
7. **Create a Superuser**: You can create a superuser to access the Django admin interface and perform administrative tasks:
    ```bash
    python manage.py createsuperuser
    ```
8. **Run the Development Server**: Start the Django development server to run the project locally:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```


## Run in Postman
Want to quickly test the API endpoints? Click the button below to run the `Postman` collection:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/28281018-23c37ca9-ae19-4816-a122-ac3e6598acdc?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D28281018-23c37ca9-ae19-4816-a122-ac3e6598acdc%26entityType%3Dcollection%26workspaceId%3Daf9e4e52-2ba6-43d0-969c-d07e31f6d518)


## Questions or Feedback?

If you have any questions, feedback, or encounter any issues while setting up the project, feel free to reach out! We're here to help.