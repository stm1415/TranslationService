from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
import schemas

import crud
import models
from database import get_db, engine

 # from schemas import TranslationRequest --> in order for this to work, we need the __init__.py file

app = FastAPI() # creates an instance of the FastAPI class, which is the central object of your FastAPI application. This instance is used to define routes, middleware, and configuration settings.

# setup for Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get('/index', response_class = HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


# enable cors:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allows all origins
    allow_credentials=True, # Allow cookies or authentication headers
    allow_methods=["*"], # allowed all HTTP methods(GET, POST, etc.)
    allow_headers=["*"]              # HTTP headers allowed in requests

)

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):
    # pseudo code
    """
    task = CRUD.create_translation_task(x,y,o)

    Background tasks:
    background_tasks.add_task(perform_translation, task_id, request.text ,request.languages, db)
    
    return {"task_id":{task_id}}
    
    """
    task = crud.create_translation_task(get_db.db, request.text, request.languages)

    #background.tasks.add_task(perform_translation, task.id, request.text, request.languages, get_db.db)






