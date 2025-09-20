"""
To run:
1. cd fastapi
2. `fastapi dev main.py`
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}