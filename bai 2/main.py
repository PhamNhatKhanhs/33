from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class OperationInput(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server"}

@app.post("/add")
def add(input: OperationInput):
    return {"result": input.a + input.b}

@app.post("/subtract")
def subtract(input: OperationInput):
    return {"result": input.a - input.b}

@app.post("/multiply")
def multiply(input: OperationInput):
    return {"result": input.a * input.b}

@app.post("/divide")
def divide(input: OperationInput):
    if input.b == 0:
        return {"error": "Không thể chia cho 0"}
    return {"result": input.a / input.b}



