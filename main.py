from ticket import Ticket
import database

tickets = []


def create_ticket():
    print("\n--- Create Ticket ---")

    name = input("Enter your name: ")
    issue = input("Describe the issue: ")

    while True:
        priority = input("Priority (Low/Medium/High): ").capitalize()

        if priority in ["Low", "Medium", "High"]:
            break

        print("Invalid priority. Please choose Low, Medium or High.")

    database.add_ticket(name, issue, priority)

    print("\nTicket created successfully!")


def view_tickets():
    print("\n--- All Tickets ---")

    tickets = database.get_tickets()

    if not tickets:
        print("There are currently no tickets.")
        return

    for ticket in tickets:
        print(f"""
Ticket ID: {ticket[0]}
User: {ticket[1]}
Issue: {ticket[2]}
Priority: {ticket[3]}
Status: {ticket[4]}
-------------------------
""")


def search_tickets():
    print("\n--- Search Tickets ---")

    search = input("Enter a name or issue to search for: ")

    tickets = database.search_tickets(search)

    if not tickets:
        print("No matching tickets found.")
        return

    for ticket in tickets:
        print(f"""
Ticket ID: {ticket[0]}
User: {ticket[1]}
Issue: {ticket[2]}
Priority: {ticket[3]}
Status: {ticket[4]}
-------------------------
""")


def update_ticket():
    print("\n--- Update Ticket ---")

    try:
        ticket_id = int(input("Enter ticket ID: "))
    except ValueError:
        print("Please enter a valid ticket ID.")
        return

    valid_statuses = ["Open", "In Progress", "Closed"]

    new_status = input(
        "Enter new status (Open/In Progress/Closed): "
    )

    if new_status not in valid_statuses:
        print("Invalid status.")
        return

    rows_updated = database.update_ticket_status(
        ticket_id,
        new_status
    )

    if rows_updated == 0:
        print("Ticket not found.")
    else:
        print("Ticket updated successfully!")

def delete_ticket():
    print("\n--- Delete Ticket ---")

    try:
        ticket_id = int(input("Enter ticket ID to delete: "))
    except ValueError:
        print("Please enter a valid ticket ID.")
        return

    rows_deleted = database.delete_ticket(ticket_id)

    if rows_deleted == 0:
        print("Ticket not found.")
    else:
        print("Ticket deleted successfully!")

def main():

    database.create_table()

    while True:

        print("""
================================
       IT HELP DESK SYSTEM
================================

1. Create Ticket
2. View Tickets
3. Search Tickets
4. Update Ticket
5. Delete Ticket
6. Exit
""")

        choice = input("Select an option: ")

        if choice == "1":
            create_ticket()

        elif choice == "2":
            view_tickets()

        elif choice == "3":
            search_tickets()

        elif choice == "4":
            update_ticket()

        elif choice == "5":
            delete_ticket()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()  