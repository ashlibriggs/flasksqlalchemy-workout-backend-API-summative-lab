from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date


with app.app_context():
    print("Deleting existing data...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Creating exercises...")

    push_up = Exercise(name="Push Up", category="Strength", equipment_needed=False)
    squat = Exercise(name="Squat", category="Strength", equipment_needed=False)
    running = Exercise(name="Running", category="Cardio", equipment_needed=False)

    print("Creating workouts...")

    workout_1 = Workout(
        date=date(2026, 6, 20),
        duration_minutes=45,
        notes="Full body workout"
    )

    print("Creating workout exercises...")

    workout_exercise_1 = WorkoutExercise(
        workout=workout_1,
        exercise=push_up,
        reps=15,
        sets=3,
        duration_seconds=0
    )

    workout_exercise_2 = WorkoutExercise(
        workout=workout_1,
        exercise=squat,
        reps=12,
        sets=4,
        duration_seconds=0
    )

    workout_exercise_3 = WorkoutExercise(
        workout=workout_1,
        exercise=running,
        reps=0,
        sets=0,
        duration_seconds=600
    )

    db.session.add_all([
        push_up,
        squat,
        running,
        workout_1,
        workout_exercise_1,
        workout_exercise_2,
        workout_exercise_3
    ])

    db.session.commit()

    print("Database seeded successfully!")