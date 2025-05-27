from fastapi import FastAPI

app = FastAPI()

fake_db = []

@app.post("/leads/")
def create_lead(name: str, email: str):
    lead = {"name": name, "email": email}
    fake_db.append(lead)
    return {"message": "Lead created", "lead": lead}

@app.get("/leads/")
def get_leads():
    return {"leads": fake_db}
