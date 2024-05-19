from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Giả lập cơ sở dữ liệu
fake_db = {
    "students": [
        {"id": 1, "name": "Nguyễn Văn A", "age": 20, "address": "Hà Nội", "phone": "0123456789", "email": "email@example.com", "class": "10A1"},
        {"id": 2, "name": "Trần Thị B", "age": 21, "address": "TP HCM", "phone": "0123456790", "email": "email2@example.com", "class": "10A2"},
        {"id": 3, "name": "Lê Thị C", "age": 22, "address": "Đà Nẵng", "phone": "0123456791", "email": "email3@example.com", "class": "11A1"},
        {"id": 4, "name": "Phạm Văn D", "age": 23, "address": "Nha Trang", "phone": "0123456792", "email": "email4@example.com", "class": "11A2"},
        {"id": 5, "name": "Hoàng Thị E", "age": 24, "address": "Cần Thơ", "phone": "0123456793", "email": "email5@example.com", "class": "12A1"},
        {"id": 6, "name": "Trần Văn F", "age": 25, "address": "Hải Phòng", "phone": "0123456794", "email": "email6@example.com", "class": "12A2"},
        {"id": 7, "name": "Nguyễn Thị G", "age": 26, "address": "Huế", "phone": "0123456795", "email": "email7@example.com", "class": "12B1"},
        {"id": 8, "name": "Lê Văn H", "age": 27, "address": "Bình Dương", "phone": "0123456796", "email": "email8@example.com", "class": "12B2"}
    ],
    "users": {"admin": "admin"}
}

class Login(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(login: Login):
    user_password = fake_db["users"].get(login.username)
    if user_password and user_password == login.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/students", response_model=List[dict])
def get_students():
    return fake_db["students"]

# Thêm endpoint cho đường dẫn gốc
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",  # Thêm nguồn gốc của bạn ở đây
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run(app, host="127.0.0.1", port=8000)