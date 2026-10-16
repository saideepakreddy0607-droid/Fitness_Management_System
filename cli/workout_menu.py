from Modals.workout import Workout
from Modals.trainer import Trainer
from databases.workout_repository import WorkoutRepository
from databases.trainer_repository import TrainerRepository
from cli.utils import read_int, read_positive_number, run_db_action


def _load_workout(repo, workout_id):
    rows = repo.get_workout(workout_id)
    if not rows:
        return None, None
    first = rows[0]
    exercises = [row[5] for row in rows if row[5] is not None]
    durations = [int(row[6]) for row in rows if row[5] is not None]
    workout = Workout(first[2], first[1], exercises, first[3], durations)
    return workout, rows


def workout_menu():
    repo = WorkoutRepository()
    trainer_repo = TrainerRepository()

    while True:
        print("\n===== WORKOUT MANAGEMENT =====")
        print("1. Add Workout")
        print("2. View Workout")
        print("3. Add Exercise to Workout")
        print("4. Update Exercise Duration")
        print("5. Delete Exercise from Workout")
        print("6. Calculate Total Workout Duration")
        print("7. Delete Workout")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            workout_id = read_int("Workout ID: ")
            member_id = read_int("Member ID: ")
            trainer_id = read_int("Trainer ID: ")
            trainer_row = trainer_repo.get_trainer(trainer_id)
            if trainer_row is None:
                print("Trainer not found. Add the trainer first.")
                continue
            purpose = input("Workout purpose: ").strip()
            workout = Workout(trainer_id, member_id, [], purpose, [])
            trainer = Trainer(*trainer_row)

            while True:
                exercise = input("Exercise name (leave blank to finish): ").strip()
                if not exercise:
                    break
                duration = read_positive_number("Duration in minutes: ")
                trainer.add_exercise(workout, exercise, int(duration))

            if not workout.exercise:
                print("A workout must contain at least one exercise.")
                continue
            run_db_action(lambda: repo.add_workout(workout_id, workout), "Workout added successfully.")

        elif choice in ("2", "6"):
            workout_id = read_int("Workout ID: ")
            workout, rows = _load_workout(repo, workout_id)
            if workout is None:
                print("Workout not found.")
                continue
            print("Workout ID:", rows[0][0])
            print("Member ID:", workout.member_id)
            print("Trainer ID:", workout.trainer_id)
            print("Purpose:", workout.purpose)
            print("Exercises:")
            if workout.exercise:
                for exercise, duration in zip(workout.exercise, workout.duration):
                    print(f"- {exercise}: {duration} minutes")
            else:
                print("No exercises recorded.")
            if choice == "6":
                print("Total duration:", workout.calculate_duration(), "minutes")

        elif choice in ("3", "4", "5"):
            workout_id = read_int("Workout ID: ")
            workout, rows = _load_workout(repo, workout_id)
            if workout is None:
                print("Workout not found.")
                continue
            trainer_row = trainer_repo.get_trainer(workout.trainer_id)
            if trainer_row is None:
                print("Trainer for this workout was not found.")
                continue
            trainer = Trainer(*trainer_row)

            if choice == "3":
                exercise = input("New exercise name: ").strip()
                duration = int(read_positive_number("Duration in minutes: "))
                trainer.add_exercise(workout, exercise, duration)
                run_db_action(
                    lambda: repo.add_exercise(workout_id, exercise, duration),
                    "Exercise added successfully."
                )

            elif choice == "4":
                exercise = input("Exercise name to update: ").strip()
                duration = int(read_positive_number("New duration in minutes: "))
                if exercise not in workout.exercise:
                    print("Exercise not found in this workout.")
                    continue
                trainer.update_exercise(workout, exercise, duration)
                if repo.update_exercise(workout_id, exercise, duration):
                    print("Exercise duration updated successfully.")
                else:
                    print("Exercise not found in the database.")

            else:
                exercise = input("Exercise name to delete: ").strip()
                if exercise not in workout.exercise:
                    print("Exercise not found in this workout.")
                    continue
                trainer.delete_exercise(workout, exercise)
                if repo.delete_exercise(workout_id, exercise):
                    print("Exercise deleted successfully.")
                else:
                    print("Exercise not found in the database.")

        elif choice == "7":
            workout_id = read_int("Workout ID to delete: ")
            if not repo.get_workout(workout_id):
                print("Workout not found.")
            else:
                confirm = input("Delete this workout and its exercises? (y/n): ").strip().lower()
                if confirm == "y":
                    run_db_action(lambda: repo.delete_workout(workout_id), "Workout deleted successfully.")
                else:
                    print("Delete cancelled.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
