import functions
from fastapi import FastAPI, APIRouter, Depends, Request, Response

app = FastAPI()

@app.get('/')
def index():
    return "Hello World"


@app.get('/login')
def login():
    return functions.generate_token()


@app.get('/protected-route')
def index(current_user = Depends(functions.is_logged_in)):
    print(current_user)
    return "Hello World"
