from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

# user imports
from api import users, courses, sections

app = FastAPI(
    title="Fast Api for lms",
    description="LMS Api for managing students and course",
    version="0.0.1",
    contact={
        "name": "Uneku",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


# entry point
@app.get("/")
async def root():
    return {"message": "welcome to the backend"}
