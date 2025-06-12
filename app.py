from fastapi import FastAPI 
import os
from dotenv import load_dotenv

load_dotenv()
app= FastAPI()

app_name=os.getenv("APP_NAME")
@app.get("/")
def index():
    return{"message":f"welcome to my world of Devops from {app_name}"}

