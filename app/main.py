from fastapi import Depends, FastAPI

app = FastAPI(title="Example template") #This creates the FastAPI application object. 

@app.get("/health") #This tells FastAPI that the function below it should run when the browser or client sends a GET request to /health.
def health():
    return{"status": "ok"} #This function returns a Python dictionary. FastAPI automatically converts it to JSON.

#Below here code is not given for the exam.

@app.get("/hello") 
def hello(): 
    return {"message": "Hello from FastAPI"} 
