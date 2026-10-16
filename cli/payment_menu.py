from Modals.payment import Payment
from databases.payment_repository import PaymentRepository
from cli.utils import read_int, read_positive_number, read_date, run_db_action


def payment_menu():
    repo = PaymentRepository()

    while True:
        print("\n===== PAYMENT MANAGEMENT =====")
        print("1. Add Payment")
        print("2. View Payment")
        print("3. Update Payment")
        print("4. Delete Payment")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            payment_id = read_int("Payment ID: ")
            member_id = read_int("Member ID: ")
            amount = read_positive_number("Amount: ")
            payment_date = read_date("Payment Date (YYYY-MM-DD): ")
            payment = Payment(payment_id, member_id, amount, payment_date)
            run_db_action(lambda: repo.add_payment(payment), "Payment recorded successfully.")

        elif choice == "2":
            payment_id = read_int("Payment ID: ")
            row = repo.get_payment(payment_id)
            if row is None:
                print("Payment not found.")
            else:
                print("Payment ID:", row[0])
                print("Member ID:", row[1])
                print("Amount:", row[2])
                print("Payment Date:", row[3])

        elif choice == "3":
            payment_id = read_int("Payment ID: ")
            if repo.get_payment(payment_id) is None:
                print("Payment not found.")
                continue
            amount = read_positive_number("New amount: ")
            payment_date = read_date("New Payment Date (YYYY-MM-DD): ")
            run_db_action(lambda: repo.update_payment(payment_id, amount, payment_date), "Payment updated successfully.")

        elif choice == "4":
            payment_id = read_int("Payment ID to delete: ")
            if repo.get_payment(payment_id) is None:
                print("Payment not found.")
            else:
                confirm = input("Delete this payment? (y/n): ").strip().lower()
                if confirm == "y":
                    run_db_action(lambda: repo.delete_payment(payment_id), "Payment deleted successfully.")
                else:
                    print("Delete cancelled.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
