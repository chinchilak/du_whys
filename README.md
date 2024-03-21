# Django Dynamic Model API

This is a Django project that provides endpoints for importing and querying dynamic model data from JSON source using the Django REST Framework.

## Prerequisites

- Python (tested with 3.11.4)
- see requirements.txt

## Getting Started

1. Clone this repository to your local machine:

    `git clone https://github.com/chinchilak/du_whys.git`

2. Navigate into project folder:

    `cd du_whys`

3. Install the project dependencies:

    `pip install -r requirements.txt`

4. Navigate to the project directory:

    `cd du`

5. Start the development server (default: http://127.0.0.1:8000/):

    `python manage.py runserver`

6. Access the API endpoints in your browser

- `POST /import`: Imports data from a JSON file to the database.
- `GET /detail/<model_name>/`: Retrieves all data for a specific model.
- `GET /detail/<model_name>/<id>/`: Retrieves data for a specific model with a given ID.
