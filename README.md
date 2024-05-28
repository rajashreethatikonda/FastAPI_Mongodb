# FastAPI User Management API

This is a simple FastAPI application for managing user data using MongoDB as the database backend.

## Features

- Create, read, update, and delete (CRUD) operations for user data.
- RESTful API endpoints for user management.
- Pydantic models for data validation.
- MongoDB as the database backend.
- Error handling for better user experience.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic
- pymongo

## Installation

1. Clone this repository:

2. Install the required Python packages:

3. Start your MongoDB server and ensure it's running locally.

4. Update the MongoDB connection details in `db.py` if necessary.

## Usage

1. Start the FastAPI application:

2. Access the API documentation at `http://127.0.0.1:8000/docs` to view and test the available endpoints using Swagger UI.

3. Use the provided API endpoints to perform CRUD operations on user data.

## API Endpoints

- **GET /users/**: Retrieve all users.
- **GET /users/{user_id}**: Retrieve a specific user by ID.
- **POST /users/**: Create a new user.
- **PUT /users/{user_id}**: Update an existing user.
- **DELETE /users/{user_id}**: Delete a user by ID.

## Data Model

The user data model consists of the following fields:

- **name**: Name of the user.
- **email**: Email address of the user.
- **password**: Password of the user.

## Error Handling

- The API endpoints handle various error scenarios and provide appropriate HTTP responses.
- Error details are returned in JSON format for easy debugging and handling.



