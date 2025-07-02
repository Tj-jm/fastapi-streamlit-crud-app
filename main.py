from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models, schemas, crud
from database import engine,SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Task App',
    description='A tutorial',
    verion="1.0.0"
)

#corrs middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

#Dependency to get DB sesssion


def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()    


@app.get("/tasks/",response_model=list[schemas.Task])
def read_tasks(skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    return crud.get_tasks (db,skip=skip,limit=limit)


@app.post("/tasks/",response_model=schemas.Task,status_code=201)
def create_task(task:schemas.TaskCreate,db:Session=Depends(get_db)):
    return crud.create_task(db,task)

@app.get("/tasks/{task_id}",response_model=schemas.Task)
def read_task(task_id:int,db:Session=Depends(get_db)):
    task =crud.get_task(db,task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task Not Found")
    return task

@app.put("/tasks/{task_id}",response_model=schemas.Task)
def update_task(task_id:int,task_update:schemas.TaskUpdate,db:Session=Depends(get_db)):
    task = crud.update_task(db,task_id,task_update)
    if task is None:
        raise HTTPException(status_code=404, detail='Task Not Found')
    
    return task

@app.delete("/tasks/{task_id}",response_model=schemas.Task)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    task = crud.delete_task(db,task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task