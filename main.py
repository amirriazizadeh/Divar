# main.py
import pickle
import os
from core import Auth  

DATA_FILE = "data.pkl"


def save_data(auth_obj):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(auth_obj, f)


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            auth = pickle.load(f)
            Auth._instance = auth  
            return auth
    else:
        return Auth()

# print(load_data().get_all_tickets())

def print_menu():
    print("\n--- Event & Ticket Management ---")
    print("1. Login as Admin")
    print("2. Register User")
    print("3. Add Event")
    print("4. Issue Ticket")
    print("5. Cancel Ticket")
    print("6. List Events")
    print("7. List Tickets for User")
    print("8. List All Tickets")
    print("9. Logout Admin")
    print("0. Exit")


def main():
    auth = load_data()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            u = input("Admin username: ")
            p = input("Admin password: ")
            auth.login_admin(u, p)

        elif choice == "2":
            u = input("New username: ")
            p = input("Password: ")
            n = input("National ID: ")
            auth.register(u, p, n)
            save_data(auth)

        elif choice == "3":
            name = input("Event name: ")
            date = input("Date (YYYY-MM-DD): ")
            capacity = int(input("Capacity: "))
            desc = input("Description (optional): ")
            auth.add_event(name, date, capacity, desc)
            save_data(auth)

        elif choice == "4":
            u = input("Username: ")
            e = input("Event name: ")
            auth.issue_ticket(u, e)
            save_data(auth)

        elif choice == "5":
            u = input("Username: ")
            e = input("Event name: ")
            auth.cancel_ticket(u, e)
            save_data(auth)

        elif choice == "6":
            for ev in auth.get_all_events():
                print(ev)

        elif choice == "7":
            u = input("Username: ")
            tickets = auth.get_tickets_for_user(u)
            for t in tickets:
                print(t)

        elif choice == "8":
            for t in auth.get_all_tickets():
                print(t)

        elif choice == "9":
            auth.logout_admin()

        elif choice == "0":
            save_data(auth)
            print("Exiting. Data saved.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


