from databases.connection import get_connection

class WorkoutRepository:

    def add_workout(self, workout_id, workout):
        connection = get_connection()
        cursor = connection.cursor()

        # Insert the workout details
        query = """
            INSERT INTO Workout
            (Workout_Id, Member_Id, Trainer_Id, Purpose)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            workout_id,
            workout.member_id,
            workout.trainer_id,
            workout.purpose
        )

        cursor.execute(query, values)

        # Insert each exercise belonging to this workout
        query = """
            INSERT INTO WorkoutExercise
            (Workout_Exercise_Id, Workout_Id, Exercise, Duration)
            VALUES (%s, %s, %s, %s)
        """

        for i in range(len(workout.exercise)):
            exercise_id = workout_id * 100 + i + 1

            values = (
                exercise_id,
                workout_id,
                workout.exercise[i],
                workout.duration[i]
            )

            cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

    def get_workout(self, workout_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                w.Workout_Id,
                w.Member_Id,
                w.Trainer_Id,
                w.Purpose,
                we.Workout_Exercise_Id,
                we.Exercise,
                we.Duration
            FROM Workout w
            LEFT JOIN WorkoutExercise we
                ON w.Workout_Id = we.Workout_Id
            WHERE w.Workout_Id = %s
        """

        cursor.execute(query, (workout_id,))
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result

    def delete_workout(self, workout_id):
        connection = get_connection()
        cursor = connection.cursor()

        # Delete exercises first because they reference Workout
        query = """
            DELETE FROM WorkoutExercise
            WHERE Workout_Id = %s
        """
        cursor.execute(query, (workout_id,))

        # Then delete the workout
        query = """
            DELETE FROM Workout
            WHERE Workout_Id = %s
        """
        cursor.execute(query, (workout_id,))

        connection.commit()
        cursor.close()
        connection.close()


    def add_exercise(self, workout_id, exercise, duration):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COALESCE(MAX(Workout_Exercise_Id), %s) + 1 FROM WorkoutExercise WHERE Workout_Id = %s",
            (workout_id * 100, workout_id)
        )
        exercise_id = cursor.fetchone()[0]

        cursor.execute(
            "INSERT INTO WorkoutExercise (Workout_Exercise_Id, Workout_Id, Exercise, Duration) VALUES (%s, %s, %s, %s)",
            (exercise_id, workout_id, exercise, duration)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return True

    def update_exercise(self, workout_id, exercise, duration):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT Workout_Exercise_Id FROM WorkoutExercise WHERE Workout_Id = %s AND Exercise = %s LIMIT 1",
            (workout_id, exercise)
        )
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            connection.close()
            return False

        cursor.execute(
            "UPDATE WorkoutExercise SET Duration = %s WHERE Workout_Exercise_Id = %s",
            (duration, row[0])
        )
        connection.commit()
        cursor.close()
        connection.close()
        return True

    def delete_exercise(self, workout_id, exercise):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT Workout_Exercise_Id FROM WorkoutExercise WHERE Workout_Id = %s AND Exercise = %s LIMIT 1",
            (workout_id, exercise)
        )
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            connection.close()
            return False

        cursor.execute(
            "DELETE FROM WorkoutExercise WHERE Workout_Exercise_Id = %s",
            (row[0],)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return True
