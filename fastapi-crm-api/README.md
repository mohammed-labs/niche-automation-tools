# FastAPI CRM API

Basic CRM-style lead API with FastAPI.

## Run
```bash
uvicorn main:app --reload
```

## Endpoints
- POST `/leads/` with name and email
- GET `/leads/` to fetch all leads
