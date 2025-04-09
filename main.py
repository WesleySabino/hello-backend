# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Hello Backend", version="0.1.0")

# ----- Data model -----
class Greeting(BaseModel):
    name: str

# ----- Routes -----
@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is alive 🚀"}

@app.post("/greet")
def greet(payload: Greeting):
    return {"greeting": f"Nice to meet you, {payload.name}!"}

@app.get("/hello/{name}")
def hello_anyone(name: str):
    return {"message": f"Hello, {name}"}