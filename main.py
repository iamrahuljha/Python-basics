from fastapi import FastAPI
import os
app = FastAPI()
 
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
