<!-- @format -->

# LMS API Project with FastAPI

## Overview

This project is aimed at developing a robust API for a Learning Management System (LMS) using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.10+ based on standard Python type hints.

## Features

- **User Management**: CRUD operations for managing users (students, instructors, administrators).
- **Course Management**: CRUD operations for managing courses.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **SQLAlchemy**: ORM (Object Relational Mapper) for database interactions.
- **PostgreSQL**: Database options for storing application data.
- **Alembic**: Lightweight database migration tool for usage with SQLAlchemy, allowing for easy schema versioning.

## API Endpoints

### User Management

- **`POST /users/`**: Create a new user.
- **`GET /users/{user_id}/`**: Retrieve user details.
- **`PUT /users/{user_id}/`**: Update user details.
- **`DELETE /users/{user_id}/`**: Delete a user.

### Course Management

- **`POST /courses/`**: Create a new course.
- **`GET /courses/{course_id}/`**: Retrieve course details.
- **`PUT /courses/{course_id}/`**: Update course details.
- **`DELETE /courses/{course_id}/`**: Delete a course.

## Database Schema

### Users

- **id**: Integer (Primary Key)
- **username**: String
- **email**: String
- **role**: String (Enum: "student", "teacher")

### Courses

- **id**: Integer (Primary Key)
- **title**: String
- **description**: String

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/lms-api.git
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Set up the database:

   ```bash
   alembic upgrade head
   ```

4. Run the development server:

   ```bash
   uvicorn main:app --reload
   ```

## Conclusion

This API project provides a scalable and efficient solution for managing a Learning Management System. With FastAPI's speed and flexibility, it ensures high performance and ease of development for building robust APIss.
