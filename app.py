from fastapi import FastAPI 


app= FastAPI()

@app.get("/message")
def index():
    return{"message":"welcome to my world of Devops"}

