# Workout Backend API

A Flask + SQLAlchemy REST API for tracking workouts and exercises. This API allows users to create workouts, create exercises, and associate exercises with workouts while tracking details such as reps, sets, duration, and notes.

---

## Project Overview

The Workout Backend API allows users to manage workouts and exercises through a relational database structure. This project demonstrates backend development concepts including RESTful routing, SQLAlchemy models, database relationships, serialization, validation, and API endpoint design using Flask.

---

## Features

* View all workouts
* View a single workout with associated exercises
* Create new workouts
* Delete workouts
* View all exercises
* View a single exercise with associated workouts
* Create new exercises
* Delete exercises
* Associate exercises with workouts
* Track reps, sets, and duration for each exercise within a workout
* Use many-to-many relationships through an association table

---

## Technologies Used

* Python
* Flask
* SQLAlchemy
* Flask-Migrate
* Marshmallow
* SQLite
* REST APIs
* Pipenv
* Git & GitHub

---

## Models

### Exercise

* `id`
* `name`
* `category`
* `equipment_needed`

### Workout

* `id`
* `date`
* `duration_minutes`
* `notes`

### WorkoutExercise

* `id`
* `workout_id`
* `exercise_id`
* `reps`
* `sets`
* `duration_seconds`

---

## Relationships

* A Workout has many WorkoutExercises.
* An Exercise has many WorkoutExercises.
* A Workout has many Exercises through WorkoutExercises.
* An Exercise has many Workouts through WorkoutExercises.

---

## Database Schema

```text
Workout
---------
id
date
duration_minutes
notes

Exercise
---------
id
name
category
equipment_needed

WorkoutExercise
----------------
id
workout_id
exercise_id
reps
sets
duration_seconds
```

---

## API Endpoints

### Workouts

| Method | Endpoint         | Description                    |
| ------ | ---------------- | ------------------------------ |
| GET    | `/workouts`      | Returns all workouts           |
| GET    | `/workouts/<id>` | Returns a single workout by ID |
| POST   | `/workouts`      | Creates a new workout          |
| DELETE | `/workouts/<id>` | Deletes a workout              |

### Exercises

| Method | Endpoint          | Description                     |
| ------ | ----------------- | ------------------------------- |
| GET    | `/exercises`      | Returns all exercises           |
| GET    | `/exercises/<id>` | Returns a single exercise by ID |
| POST   | `/exercises`      | Creates a new exercise          |
| DELETE | `/exercises/<id>` | Deletes an exercise             |

### Workout Exercises

| Method | Endpoint                                                           | Description                           |
| ------ | ------------------------------------------------------------------ | ------------------------------------- |
| POST   | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Associates an exercise with a workout |

---

## Example Requests

### Create a Workout

**POST** `/workouts`

Request Body:

```json
{
  "date": "2026-06-23",
  "duration_minutes": 45,
  "notes": "Lower body strength workout"
}
```

Example Response:

```json
{
  "id": 1,
  "date": "2026-06-23",
  "duration_minutes": 45,
  "notes": "Lower body strength workout"
}
```

### Create an Exercise

**POST** `/exercises`

Request Body:

```json
{
  "name": "Squat",
  "category": "Strength",
  "equipment_needed": "Barbell"
}
```

Example Response:

```json
{
  "id": 1,
  "name": "Squat",
  "category": "Strength",
  "equipment_needed": "Barbell"
}
```

### Associate an Exercise with a Workout

**POST** `/workouts/1/exercises/1/workout_exercises`

Request Body:

```json
{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 0
}
```

Example Response:

```json
{
  "id": 1,
  "workout_id": 1,
  "exercise_id": 1,
  "reps": 10,
  "sets": 3,
  "duration_seconds": 0
}
```

---

## Validation Rules

* Exercise names are required.
* Workout dates are required.
* Duration values must be valid numbers.
* WorkoutExercise records must reference an existing Workout and Exercise.
* Invalid requests return descriptive error messages.

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Install dependencies:

```bash
pipenv install
pipenv shell
```

---

## Database Setup

Run migrations and seed the database:

```bash
flask db upgrade
python seed.py
```

---

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The API will run locally at:

```text
http://localhost:5555
```

---

## Future Improvements

* Add update (`PATCH`/`PUT`) routes
* Add user authentication and authorization
* Add automated testing
* Add filtering and search functionality
* Deploy the API to a cloud platform
* Build a frontend interface

---

## Author

Created by **Ashli Briggs** as part of the SMU Software Engineering Bootcamp.
