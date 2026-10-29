from fastapi import Depends, FastAPI, HTTPException, status

from app.schemas import UserCreate 

app = FastAPI(title="Example template") #This creates the FastAPI application object. 

users: list[UserCreate] = [] 

@app.get("/health") #This tells FastAPI that the function below it should run when the browser or client sends a GET request to /health.
def health():
    return{"status": "ok"} #This function returns a Python dictionary. FastAPI automatically converts it to JSON.

#Below here code is not given for the exam.


@app.get("/hello") 
def hello(): 
    return {"message": "Hello from FastAPI"} 


@app.post("/api/users", status_code=status.HTTP_201_CREATED) 
def add_user(new_user: UserCreate): 
    for existing_user in users: 
        if existing_user.user_id == new_user.user_id: 
            raise HTTPException( 
                status_code=status.HTTP_409_CONFLICT, 
                detail="A user with this user_id already exists", 
            ) 
 
    users.append(new_user) 
    return new_user 
