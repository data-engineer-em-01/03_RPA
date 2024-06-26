from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as r

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

app.include_router(r.router)

@app.get("/")
def read_root():
 
    return {"API": "API Invoices"}