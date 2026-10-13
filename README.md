# Flask Drinks REST API

A simple REST API built with Python, Flask, Flask-SQLAlchemy, and SQLite. This project demonstrates CRUD operations for managing drinks and uses Docker for containerization.

## Features

- Retrieve all drinks
- Retrieve a drink by ID
- Add a new drink using POST requests
- Delete a drink by ID
- Store drink data in an SQLite database
- Use SQLAlchemy ORM for database operations
- Run the application inside a Docker container

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Docker

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check whether the API is running |
| GET | `/drinks` | Retrieve all drinks |
| GET | `/drinks/<id>` | Retrieve a drink by ID |
| POST | `/drinks` | Add a new drink |
| DELETE | `/drinks/<id>` | Delete a drink by ID |

### Example POST Request

Send a POST request to `/drinks` with a JSON body:

```json
{
  "name": "Coffee",
  "description": "Hot black coffee"
}
```

## Run with Docker

### 1. Build the Docker image

```bash
docker build -t flask-drinks-api .
```

### 2. Run the container

```bash
docker run -d --name drinks-api -p 5000:5000 -v drinks-data:/app/instance flask-drinks-api
```

### 3. Access the API

- Home: http://localhost:5000/
- All drinks: http://localhost:5000/drinks

### 4. View container logs

```bash
docker logs drinks-api
```

### 5. Stop the container

```bash
docker stop drinks-api
```

### 6. Remove the container

```bash
docker rm drinks-api
```

## Run Locally

Create and activate a virtual environment, install dependencies, and start the application.

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
python application.py
```

The API will be available at http://localhost:5000/.

## Future Improvements

- Add automated tests with pytest
- Add input validation and improved error handling
- Set up CI/CD with GitHub Actions
- Deploy the API to a cloud platform

