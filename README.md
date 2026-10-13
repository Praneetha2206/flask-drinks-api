# Flask Drinks REST API

A REST API built with Flask and SQLAlchemy to manage drink records. This project demonstrates backend development, API validation, automated testing, Docker containerization, CI/CD, and cloud deployment.

**Live API:** https://flask-drinks-api.onrender.com  
**GitHub Repository:** https://github.com/Praneetha2206/flask-drinks-api

## Features

- RESTful endpoints for retrieving, creating, and deleting drink records
- Input validation and appropriate HTTP error responses
- SQLAlchemy database integration with SQLite
- Automated API tests using pytest
- Code quality checks using Ruff
- Docker containerization
- Gunicorn as the WSGI server
- GitHub Actions for continuous integration
- Automated Docker image publishing to GitHub Container Registry (GHCR)
- Deployment on Render

## Tech Stack

- **Language:** Python
- **Backend:** Flask, Flask-SQLAlchemy, SQLAlchemy
- **Database:** SQLite
- **Testing:** pytest
- **Linting:** Ruff
- **Containerization:** Docker
- **Application Server:** Gunicorn
- **CI/CD:** GitHub Actions
- **Container Registry:** GitHub Container Registry (GHCR)
- **Deployment:** Render

## API Endpoints

Base URL: `https://flask-drinks-api.onrender.com`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check the API home endpoint |
| GET | `/drinks` | Retrieve drink records |
| GET | `/drinks/<id>` | Retrieve a drink by ID |
| POST | `/drinks` | Create a drink |
| DELETE | `/drinks/<id>` | Delete a drink |

### Example: Create a drink

Send a `POST` request to `/drinks` with a JSON body:

```json
{
  "name": "Iced Coffee",
  "description": "Cold coffee with milk"
}
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Praneetha2206/flask-drinks-api.git
cd flask-drinks-api
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the API

```bash
python application.py
```

The API will be available at `http://localhost:5000`.

## Docker

Build the Docker image:

```bash
docker build -t flask-drinks-api:local .
```

Run the container:

```bash
docker run -d --name drinks-api -p 5000:5000 flask-drinks-api:local
```

Open `http://localhost:5000` to access the API.

## Testing and Code Quality

Run the automated tests:

```bash
python -m pytest
```

Run Ruff checks:

```bash
python -m ruff check application.py tests/
```

These checks are also included in the GitHub Actions CI workflow.

## CI/CD Workflow

The project uses GitHub Actions to automate quality checks and container publishing.

1. Code is pushed to the `main` branch.
2. The CI workflow runs the pytest suite and Ruff checks.
3. After successful CI, the Docker publishing workflow builds and publishes the image to GHCR.
4. The published image can be deployed to Render.

## Deployment

The API is deployed on Render using Gunicorn.

**Live URL:** https://flask-drinks-api.onrender.com

The service uses Render's free instance, which may spin down after inactivity. Its local filesystem is ephemeral, so SQLite data should not be considered durable across restarts or redeployments.

## What I Learned

- Designing and implementing REST API endpoints
- Validating requests and handling API errors
- Working with SQLAlchemy and SQLite
- Writing and running automated tests
- Maintaining code quality with linting
- Building and running Docker containers
- Automating CI/CD workflows with GitHub Actions
- Publishing container images to GHCR
- Deploying a Python API with Gunicorn on Render

## Future Improvements

- Add authentication and authorization
- Improve database persistence and migrations
- Add API documentation and further integration tests
- Expand monitoring and deployment automation
