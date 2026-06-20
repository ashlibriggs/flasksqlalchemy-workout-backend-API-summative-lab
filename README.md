# Workout Backend API

A Flask + SQLAlchemy API for tracking workouts and exercises.

## Models

### Exercise
- id
- name
- category
- equipment_needed

### Workout
- id
- date
- duration_minutes
- notes

### WorkoutExercise
- id
- workout_id
- exercise_id
- reps
- sets
- duration_seconds

## Relationships

- A Workout has many WorkoutExercises
- An Exercise has many WorkoutExercises
- A Workout has many Exercises through WorkoutExercises
- An Exercise has many Workouts through WorkoutExercises

## Installation

Clone the repository and install dependencies:

```bash
pipenv install
pipenv shell