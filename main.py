from fastapi import FastAPI
import os
os.system("pip install fastapi")
os.system("pip install uvicorn")
app = FastAPI()
 
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
