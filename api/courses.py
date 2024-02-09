import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic_shemas.course import Course, CourseCreate
from db.db_setup import get_db
from api.utils.courses import get_course, get_courses, create_course


router = fastapi.APIRouter()


# get all courses
@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


#  creare  anew course
@router.post("/courses", response_model=Course)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


# get course by id
@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_courses = get_course(db=db, course_id=course_id)
    if db_courses is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_courses


@router.patch("/courses/{course_id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{course_id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{course_id}/sections")
async def read_course_sections():
    return {"courses": []}
