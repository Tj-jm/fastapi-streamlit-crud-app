from sqlalchemy.orm import Session
import models,schemas

def get_task(db:Session,task_id:int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db:Session,skip:int=0,limit:int=10):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db:Session,task:schemas.TaskCreate):
    db_task=models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db:Session,task_id:int,task_update:schemas.TaskUpdate):
    task = get_task(db,task_id)

    if task:
        for field,value in task_update.model_dump(exclude_unset=True).items():
            setattr(task,field,value)
        db.commit()
        db.refresh(task)

    return task


def delete_task(db:Session,task_id:int):
    task = get_task(db,task_id)
    if task:
        db.delete(task)
        db.commit()
    return task