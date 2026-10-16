from datetime import datetime

from Modals.member import Member
from Modals.member_ship import Member_ship
from Modals.payment import Payment
from Modals.trainer import Trainer
from Modals.workout import Workout

from databases.member_repository import MemberRepository
from databases.membership_repository import MembershipRepository
from databases.payment_repository import PaymentRepository
from databases.trainer_repository import TrainerRepository
from databases.workout_repository import WorkoutRepository

# ================= MEMBER MANAGEMENT =================

def member_menu():
    repo = MemberRepository()

    while True:
        print("\n===== MEMBER MANAGEMENT =====")
        print("1. Add Member")
        print("2. View Member")
        print("3. Update Member")
        print("4. Delete Member")
        print("0. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            member = Member(
                int(input("Member ID: ")),
                input("Name: "),
                input("DOB (YYYY-MM-DD): "),
                input("Email: "),
                input("Phone Number: "),
                input("Address: "),
                input("Join Date (YYYY-MM-DD): ")
            )

            repo.add_member(member)
            print("Member added successfully.")

        elif choice == "2":
            member_id = int(input("Member ID: "))
            result = repo.get_member(member_id)

            if result:
                print("\n===== MEMBER DETAILS =====")
                print("Member ID:", result[0])
                print("Name:", result[1])
                print("DOB:", result[2])
                print("Email:", result[3])
                print("Phone:", result[4])
                print("Address:", result[5])
                print("Join Date:", result[6])
            else:
                print("Member not found.")

        elif choice == "3":
            member_id = int(input("Member ID: "))

            print("\n===== UPDATE MEMBER =====")
            print("1. Update Name")
            print("2. Update DOB")
            print("3. Update Email")
            print("4. Update Phone Number")
            print("5. Update Address")
            print("0. Cancel")

            field = input("Choose what to update: ").strip()

            if field == "1":
                repo.update_name(
                    input("New name: "), member_id
                )
            elif field == "2":
                repo.update_dob(
                    input("New DOB (YYYY-MM-DD): "), member_id
                )
            elif field == "3":
                repo.update_email(
                    input("New email: "), member_id
                )
            elif field == "4":
                repo.update_phone_no(
                    input("New phone number: "), member_id
                )
            elif field == "5":
                repo.update_address(
                    input("New address: "), member_id
                )
            elif field == "0":
                continue
            else:
                print("Invalid choice.")
                continue

            print("Member update operation completed.")

        elif choice == "4":
            member_id = int(input("Member ID to delete: "))
            repo.delete_member(member_id)
            print("Delete operation completed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ================= MEMBERSHIP MANAGEMENT =================

def membership_menu():
    repo = MembershipRepository()

    while True:
        print("\n===== MEMBERSHIP MANAGEMENT =====")
        print("1. Add Membership")
        print("2. View Membership")
        print("3. Update Membership")
        print("4. Renew Membership")
        print("5. Check Membership Status")
        print("6. Delete Membership")
        print("0. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            membership = Member_ship(
                int(input("Membership ID: ")),
                int(input("Member ID: ")),
                input("Plan (silver/gold/daimond): ").lower(),
                input("Start Date (YYYY-MM-DD): "),
                input("End Date (YYYY-MM-DD): ")
            )

            repo.add_membership(membership)
            print("Membership added successfully.")

        elif choice == "2":
            membership_id = int(input("Membership ID: "))
            result = repo.get_membership(membership_id)

            if result:
                print("\n===== MEMBERSHIP DETAILS =====")
                print("Membership ID:", result[0])
                print("Member ID:", result[1])
                print("Plan:", result[2])
                print("Start Date:", result[3])
                print("End Date:", result[4])
            else:
                print("Membership not found.")

        elif choice == "3":
            membership_id = int(input("Membership ID: "))
            plan = input("New plan (silver/gold/daimond): ").lower()
            start_date = input("New start date (YYYY-MM-DD): ")
            end_date = input("New end date (YYYY-MM-DD): ")

            repo.update_membership(
                membership_id, plan, start_date, end_date
            )
            print("Membership update operation completed.")

        elif choice == "4":
            membership_id = int(input("Membership ID to renew: "))
            result = repo.get_membership(membership_id)

            if result:
                membership = Member_ship(
                    result[0], result[1], result[2],
                    result[3], result[4]
                )

                membership.renew_member_ship()

                repo.update_membership(
                    membership.member_ship_id,
                    membership.member_ship_plan,
                    membership.start_date,
                    membership.end_date
                )

                print("Membership renewed.")
                print("New end date:", membership.end_date)
            else:
                print("Membership not found.")

        elif choice == "5":
            membership_id = int(input("Membership ID: "))
            result = repo.get_membership(membership_id)

            if result:
                membership = Member_ship(
                    result[0], result[1], result[2],
                    result[3], result[4]
                )

                print("Membership status:", membership.check_status())
            else:
                print("Membership not found.")

        elif choice == "6":
            membership_id = int(input("Membership ID to delete: "))
            repo.delete_membership(membership_id)
            print("Delete operation completed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ================= PAYMENT MANAGEMENT =================

def payment_menu():
    repo = PaymentRepository()

    while True:
        print("\n===== PAYMENT MANAGEMENT =====")
        print("1. Add Payment")
        print("2. View Payment")
        print("3. Update Payment")
        print("4. Delete Payment")
        print("0. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            payment = Payment(
                int(input("Payment ID: ")),
                int(input("Member ID: ")),
                float(input("Amount: ")),
                input("Payment Date (YYYY-MM-DD): ")
            )

            repo.add_payment(payment)
            print("Payment added successfully.")

        elif choice == "2":
            payment_id = int(input("Payment ID: "))
            result = repo.get_payment(payment_id)

            if result:
                print("\n===== PAYMENT DETAILS =====")
                print("Payment ID:", result[0])
                print("Member ID:", result[1])
                print("Amount:", result[2])
                print("Payment Date:", result[3])
            else:
                print("Payment not found.")

        elif choice == "3":
            payment_id = int(input("Payment ID: "))
            result = repo.get_payment(payment_id)

            if result:
                amount = float(input("New amount: "))
                payment_date = input("New payment date (YYYY-MM-DD): ")

                payment = Payment(
                    result[0], result[1], result[2], result[3]
                )
                payment.update_payment(amount, payment_date)

                repo.update_payment(
                    payment_id,
                    payment.amount,
                    payment.payment_date
                )

                print("Payment update operation completed.")
            else:
                print("Payment not found.")

        elif choice == "4":
            payment_id = int(input("Payment ID to delete: "))
            repo.delete_payment(payment_id)
            print("Delete operation completed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ================= TRAINER MANAGEMENT =================

def trainer_menu():
    repo = TrainerRepository()

    while True:
        print("\n===== TRAINER MANAGEMENT =====")
        print("1. Add Trainer")
        print("2. View Trainer")
        print("3. Update Trainer")
        print("4. Delete Trainer")
        print("0. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            trainer = Trainer(
                int(input("Trainer ID: ")),
                input("Trainer Name: "),
                input("Trainer Phone Number: ")
            )

            repo.add_trainer(trainer)
            print("Trainer added successfully.")

        elif choice == "2":
            trainer_id = int(input("Trainer ID: "))
            result = repo.get_trainer(trainer_id)

            if result:
                print("\n===== TRAINER DETAILS =====")
                print("Trainer ID:", result[0])
                print("Trainer Name:", result[1])
                print("Phone Number:", result[2])
            else:
                print("Trainer not found.")

        elif choice == "3":
            trainer_id = int(input("Trainer ID: "))
            result = repo.get_trainer(trainer_id)

            if result:
                trainer = Trainer(
                    result[0], result[1], result[2]
                )

                trainer.trainer_name = input("New trainer name: ")
                trainer.trainer_phno = input("New phone number: ")

                repo.update_trainer(
                    trainer.trainer_id,
                    trainer.trainer_name,
                    trainer.trainer_phno
                )

                print("Trainer update operation completed.")
            else:
                print("Trainer not found.")

        elif choice == "4":
            trainer_id = int(input("Trainer ID to delete: "))
            repo.delete_trainer(trainer_id)
            print("Delete operation completed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ================= WORKOUT MANAGEMENT =================

def workout_menu():
    repo = WorkoutRepository()

    while True:
        print("\n===== WORKOUT MANAGEMENT =====")
        print("1. Create Workout")
        print("2. View Workout")
        print("3. Delete Workout")
        print("0. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            workout_id = int(input("Workout ID: "))
            member_id = int(input("Member ID: "))
            trainer_id = int(input("Trainer ID: "))
            purpose = input("Workout purpose: ")

            workout = Workout(
                trainer_id, member_id, [], purpose, []
            )

            trainer = Trainer(trainer_id, "", "")

            while True:
                exercise = input(
                    "Exercise name (or type 'done' to finish): "
                ).strip()

                if exercise.lower() == "done":
                    break

                try:
                    duration = int(input("Duration in minutes: "))

                    if duration <= 0:
                        print("Duration must be greater than zero.")
                        continue

                    trainer.add_exercise(
                        workout, exercise, duration
                    )

                except ValueError:
                    print("Enter a valid duration.")

            repo.add_workout(workout_id, workout)

            print("Workout added successfully.")
            print(
                "Total workout duration:",
                workout.calculate_duration(),
                "minutes"
            )

        elif choice == "2":
            workout_id = int(input("Workout ID: "))
            result = repo.get_workout(workout_id)

            if result:
                print("\n===== WORKOUT DETAILS =====")

                first = result[0]
                print("Workout ID:", first[0])
                print("Member ID:", first[1])
                print("Trainer ID:", first[2])
                print("Purpose:", first[3])

                total_duration = 0

                for row in result:
                    if row[5] is not None:
                        print(
                            "Exercise:", row[5],
                            "| Duration:", row[6], "minutes"
                        )
                        total_duration += row[6]

                print("Total Duration:", total_duration, "minutes")
            else:
                print("Workout not found.")

        elif choice == "3":
            workout_id = int(input("Workout ID to delete: "))
            repo.delete_workout(workout_id)
            print("Delete operation completed.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ================= MAIN MENU =================

def main():
    while True:
        print("\n===== FITNESS MANAGEMENT SYSTEM =====")
        print("1. Member Management")
        print("2. Membership Management")
        print("3. Payment Management")
        print("4. Trainer Management")
        print("5. Workout Management")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            member_menu()
        elif choice == "2":
            membership_menu()
        elif choice == "3":
            payment_menu()
        elif choice == "4":
            trainer_menu()
        elif choice == "5":
            workout_menu()
        elif choice == "0":
            print("Exiting Fitness Management System.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
