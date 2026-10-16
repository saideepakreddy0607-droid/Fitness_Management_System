from Modals.trainer import Trainer
from databases.trainer_repository import TrainerRepository
from cli.utils import read_int, run_db_action


def trainer_menu():
    repo = TrainerRepository()

    while True:
        print("\n===== TRAINER MANAGEMENT =====")
        print("1. Add Trainer")
        print("2. View Trainer")
        print("3. Update Trainer")
        print("4. Delete Trainer")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            trainer_id = read_int("Trainer ID: ")
            name = input("Trainer Name: ").strip()
            phone = input("Trainer Phone Number: ").strip()
            trainer = Trainer(trainer_id, name, phone)
            run_db_action(lambda: repo.add_trainer(trainer), "Trainer added successfully.")

        elif choice == "2":
            trainer_id = read_int("Trainer ID: ")
            row = repo.get_trainer(trainer_id)
            if row is None:
                print("Trainer not found.")
            else:
                print("Trainer ID:", row[0])
                print("Trainer Name:", row[1])
                print("Trainer Phone:", row[2])

        elif choice == "3":
            trainer_id = read_int("Trainer ID: ")
            if repo.get_trainer(trainer_id) is None:
                print("Trainer not found.")
                continue
            name = input("New Trainer Name: ").strip()
            phone = input("New Trainer Phone Number: ").strip()
            run_db_action(lambda: repo.update_trainer(trainer_id, name, phone), "Trainer updated successfully.")

        elif choice == "4":
            trainer_id = read_int("Trainer ID to delete: ")
            if repo.get_trainer(trainer_id) is None:
                print("Trainer not found.")
            else:
                confirm = input("Delete this trainer? (y/n): ").strip().lower()
                if confirm == "y":
                    run_db_action(lambda: repo.delete_trainer(trainer_id), "Trainer deleted successfully.")
                else:
                    print("Delete cancelled.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
