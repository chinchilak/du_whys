# Django Dynamic Model API

This is a Django project that provides endpoints for importing and querying dynamic model data from JSON source using the Django REST Framework.

## Prerequisites

see requirements.txt

## Getting Started

1. Clone this repository to your local machine:

    git clone https://github.com/your-username/django-dynamic-model-api.git

2. Navigate to the project directory:

    cd django-dynamic-model-api

3. Install the project dependencies:

    pip install -r requirements.txt

4. Apply database migrations:

    python manage.py migrate

5. (Optional) Populate the database with initial data:

    [text](post_request.sh)

6. Start the development server:

    python manage.py runserver

7. Access the API endpoints in your browser or using a tool like cURL or Postman.

## Endpoints

- `POST /import`: Imports data from a JSON file to the database.
- `GET /detail/<model_name>/`: Retrieves all data for a specific model.
- `GET /detail/<model_name>/<id>/`: Retrieves data for a specific model with a given ID.

## Running Tests

To run the project's tests, execute the following command:

python manage.py test
