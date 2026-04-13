from fastapi import FastAPI
from pydantic import BaseModel
from agents import cr_agent
from fastapi.middleware.cors import CORSMiddleware
 
# ✅ FIRST create app
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello World"}
 
# ✅ THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Input schema
class InputData(BaseModel):
    sow: str
    meeting: str
 
# Home route
@app.get("/")
def home():
    return {"message": "PMO Copilot Running"}
 
# Main API
@app.post("/analyze")
def analyze(data: InputData):
    result = cr_agent(data.sow, data.meeting)
    return {"change_requests": result}