from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
import schemas
import crud
import models
from utils import perform_translation
from database import get_db, engine, SessionLocal
from typing import List
import uuid


 # from schemas import TranslationRequest --> in order for this to work, we need the __init__.py file

"""
When this line of code is executed, SQLAlchemy will inspect the metadata and generate the necessary SQL commands to create the tables in the database if they do not already exist. This is a convenient way to ensure that the database schema is in sync with the model definitions in the code.

metadata: an object that holds information about all the database tables and schema defined through the Base class. 
         - it essentially tracks the "blueprints" of your database
create_all(bind=engine):
     - this method generates the actual database tables based on teh models defined in the code
     - bind=engine specifies the databse conection to use (eg. sqlite, postgresql)
"""
models.Base.metadata.create_all(bind=engine)

app = FastAPI() # creates an instance of the FastAPI class, which is the central object of your FastAPI application. This instance is used to define routes, middleware, and configuration settings.

# setup for Jinja2 templates
templates = Jinja2Templates(directory="templates")

# enable cors:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allows all origins
    allow_credentials=True, # Allow cookies or authentication headers
    allow_methods=["*"], # allowed all HTTP methods(GET, POST, etc.)
    allow_headers=["*"]              # HTTP headers allowed in requests

)

@app.get('/index', response_class = HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # pseudo code
    """
    task = CRUD.create_translation_task(x,y,o)

    Background tasks:
    background_tasks.add_task(perform_translation, task_id, request.text ,request.languages, db)
    
    return {"task_id":{task_id}}
    
    """
    task = crud.create_translation_task(db, request.text, request.languages)
    background_tasks.add_task(perform_translation, task.id, request.text, request.languages, db)

    return {"task_id": task.id}


@app.get("/translate/{task_id}", response_model=schemas.TranslationStatus)
def get_translate(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"task_id":task.id, "status":task.status, "translations":task.translations}

@app.get("/translate/content/{task_id}")
def get_translate_content(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task






