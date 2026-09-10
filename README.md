# Student ML Prediction API

![CI Workflow](https://github.com/saadahmedcs/student-ml-api/actions/workflows/ci.yml/badge.svg)
![Release Workflow](https://github.com/saadahmedcs/student-ml-api/actions/workflows/release.yml/badge.svg)

Containerized Flask machine learning prediction service featuring automated CI validation, multi-tag packaging to GitHub Container Registry (GHCR), and SemVer release management.

---

## Features
- **Health Endpoint (`GET /health`)**: Service status and application version reporting.
- **Inference Endpoint (`POST /predict`)**: Real-time feature processing returning predicted outputs.
- **Continuous Integration**: Automated linting, testing (`pytest`), and container validation on pull requests.
- **Automated Delivery**: Tag-driven releases (`v*.*.*`) building and publishing images tagged with semantic version, git commit SHA, and `latest`.

---

## Quickstart (Local Development)

### 1. Prerequisites
- Python 3.11+
- Virtual environment (`venv`)

### 2. Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run Tests
```bash
pytest
```

4. Run Application
```bash
python app.py
```

## Docker Deployment (from GHCR)
The production image is published to GitHub Container Registry and can be pulled publicly:

```bash
\# Pull image
docker pull ghcr.io/saadahmedcs/student-ml-api:1.0.0

\# Run container
docker run -d --name student-ml-api -p 5000:5000 ghcr.io/saadahmedcs/student-ml-api:1.0.0

\# Verify health
curl -i http://localhost:5000/health

\# Run inference
curl -i -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"value": 10.5}'
```

## API Documentation
### GET /health

- Response (200 OK):

```JSON
{
  "application": "student-ml-api",
  "status": "healthy",
  "version": "1.0.0"
}
```

### POST /predict

- Payload:

```JSON
{
  "value": 10.5
}
```
- Response (200 OK):

```JSON
{
  "input": 10.5,
  "prediction": 21.0
}
```
- Error (400 Bad Request):

```JSON
{
  "error": "Missing 'value' in request body"
}
```