from Modals.member_ship import Member_ship
from databases.membership_repository import MembershipRepository
from cli.utils import read_int, read_date, run_db_action


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
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            membership_id = read_int("Membership ID: ")
            member_id = read_int("Member ID: ")
            plan = input("Plan (silver/gold/daimond): ").strip().lower()
            if plan not in ("silver", "gold", "daimond"):
                print("Invalid plan. Use silver, gold, or daimond (as defined in your model).")
                continue
            start_date = read_date("Start Date (YYYY-MM-DD): ")
            end_date = read_date("End Date (YYYY-MM-DD): ")
            membership = Member_ship(membership_id, member_id, plan, start_date, end_date)
            run_db_action(lambda: repo.add_membership(membership), "Membership added successfully.")

        elif choice == "2":
            membership_id = read_int("Membership ID: ")
            row = repo.get_membership(membership_id)
            if row is None:
                print("Membership not found.")
            else:
                print("Membership ID:", row[0])
                print("Member ID:", row[1])
                print("Plan:", row[2])
                print("Start Date:", row[3])
                print("End Date:", row[4])

        elif choice == "3":
            membership_id = read_int("Membership ID: ")
            row = repo.get_membership(membership_id)
            if row is None:
                print("Membership not found.")
                continue
            plan = input("New plan (silver/gold/daimond): ").strip().lower()
            if plan not in ("silver", "gold", "daimond"):
                print("Invalid plan.")
                continue
            start_date = read_date("New Start Date (YYYY-MM-DD): ")
            end_date = read_date("New End Date (YYYY-MM-DD): ")
            run_db_action(lambda: repo.update_membership(membership_id, plan, start_date, end_date), "Membership updated successfully.")

        elif choice == "4":
            membership_id = read_int("Membership ID to renew: ")
            row = repo.get_membership(membership_id)
            if row is None:
                print("Membership not found.")
                continue
            membership = Member_ship(*row)
            membership.renew_member_ship()
            run_db_action(
                lambda: repo.update_membership(membership.member_ship_id, membership.member_ship_plan, membership.start_date, membership.end_date),
                f"Membership renewed. New end date: {membership.end_date}"
            )

        elif choice == "5":
            membership_id = read_int("Membership ID: ")
            row = repo.get_membership(membership_id)
            if row is None:
                print("Membership not found.")
            else:
                membership = Member_ship(*row)
                print("Membership status:", membership.check_status())

        elif choice == "6":
            membership_id = read_int("Membership ID to delete: ")
            if repo.get_membership(membership_id) is None:
                print("Membership not found.")
            else:
                confirm = input("Delete this membership? (y/n): ").strip().lower()
                if confirm == "y":
                    run_db_action(lambda: repo.delete_membership(membership_id), "Membership deleted successfully.")
                else:
                    print("Delete cancelled.")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
