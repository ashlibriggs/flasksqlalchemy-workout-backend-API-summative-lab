from marshmallow import Schema, fields, validates, ValidationError


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)

    @validates("name")
    def validate_name(self, value):
        if not value or not value.strip():
            raise ValidationError("Name must not be empty.")

    @validates("category")
    def validate_category(self, value):
        if not value or not value.strip():
            raise ValidationError("Category must not be empty.")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str(allow_none=True)

    @validates("duration_minutes")
    def validate_duration_minutes(self, value):
        if value <= 0:
            raise ValidationError("Duration must be greater than 0.")


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(load_default=0)
    sets = fields.Int(load_default=0)
    duration_seconds = fields.Int(load_default=0)

    @validates("reps")
    def validate_reps(self, value):
        if value < 0:
            raise ValidationError("Reps must be 0 or greater.")

    @validates("sets")
    def validate_sets(self, value):
        if value < 0:
            raise ValidationError("Sets must be 0 or greater.")

    @validates("duration_seconds")
    def validate_duration_seconds(self, value):
        if value < 0:
            raise ValidationError("Duration seconds must be 0 or greater.")