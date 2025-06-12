from fastapi import FastAPI 
import os
from dotenv import load_dotenv

load_dotenv()
app= FastAPI()

app_name=os.getenv("APP_NAME")
@app.get("/api/")
def index():
    return {"message": f"This response is being served by: {app_name} behind Nginx load balancer"}


