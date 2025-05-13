from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import product

app = FastAPI()
app.include_router(product.router, prefix='/products', tags=['products'])

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5564"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)