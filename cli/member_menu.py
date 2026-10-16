from Modals.member import Member
from databases.member_repository import MemberRepository
from cli.utils import read_int, read_date, run_db_action


def member_menu():
    repo = MemberRepository()

    while True:
        print("\n===== MEMBER MANAGEMENT =====")
        print("1. Add Member")
        print("2. View Member")
        print("3. Update Member")
        print("4. Delete Member")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            member_id = read_int("Member ID: ")
            name = input("Name: ").strip()
            dob = read_date("Date of Birth (YYYY-MM-DD): ")
            email = input("Email: ").strip()
            phone = input("Phone Number: ").strip()
            address = input("Address: ").strip()
            join_date = read_date("Join Date (YYYY-MM-DD): ")
            member = Member(member_id, name, dob, email, phone, address, join_date)
            run_db_action(lambda: repo.add_member(member), "Member added successfully.")

        elif choice == "2":
            member_id = read_int("Enter Member ID: ")
            result = repo.get_member(member_id)
            if result is None:
                print("Member not found.")
            else:
                member = Member(*result)
                member.displayMember()

        elif choice == "3":
            member_id = read_int("Enter Member ID: ")
            if repo.get_member(member_id) is None:
                print("Member not found.")
                continue
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Date of Birth")
            print("3. Email")
            print("4. Phone Number")
            print("5. Address")
            field = input("Choose an attribute: ").strip()
            if field == "1":
                value = input("Enter new name: ").strip()
                action = lambda: repo.update_name(value, member_id)
            elif field == "2":
                value = read_date("Enter new Date of Birth (YYYY-MM-DD): ")
                action = lambda: repo.update_dob(value, member_id)
            elif field == "3":
                value = input("Enter new email: ").strip()
                action = lambda: repo.update_email(value, member_id)
            elif field == "4":
                value = input("Enter new phone number: ").strip()
                action = lambda: repo.update_phone_no(value, member_id)
            elif field == "5":
                value = input("Enter new address: ").strip()
                action = lambda: repo.update_address(value, member_id)
            else:
                print("Invalid attribute choice.")
                continue
            run_db_action(action, "Member details updated successfully.")

        elif choice == "4":
            member_id = read_int("Enter Member ID to delete: ")
            if repo.get_member(member_id) is None:
                print("Member not found.")
            else:
                confirm = input("Delete this member? (y/n): ").strip().lower()
                if confirm == "y":
                    run_db_action(lambda: repo.delete_member(member_id), "Member deleted successfully.")
                else:
                    print("Delete cancelled.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
