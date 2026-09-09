from ticket import Ticket

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

    ticket_id = len(tickets) + 1

    ticket = Ticket(ticket_id, name, issue, priority)

    tickets.append(ticket)

    print(f"\nTicket #{ticket_id} created successfully!")


def view_tickets():
    print("\n--- All Tickets ---")

    if not tickets:
        print("There are currently no tickets.")
        return

    for ticket in tickets:
        ticket.display()


def search_tickets():
    print("\n--- Search Tickets ---")

    search = input("Enter a name or issue to search for: ").lower()

    found = False

    for ticket in tickets:
        if (
            search in ticket.name.lower()
            or search in ticket.issue.lower()
        ):
            ticket.display()
            found = True

    if not found:
        print("No matching tickets found.")


def update_ticket():
    print("\n--- Update Ticket ---")

    try:
        ticket_id = int(input("Enter ticket ID: "))
    except ValueError:
        print("Please enter a valid ticket ID.")
        return

    for ticket in tickets:

        if ticket.ticket_id == ticket_id:

            print(f"Current status: {ticket.status}")

            new_status = input(
                "Enter new status (Open/In Progress/Closed): "
            )

            valid_statuses = ["Open", "In Progress", "Closed"]

            if new_status not in valid_statuses:
                print("Invalid status.")
                return

            ticket.update_status(new_status)

            print("Ticket updated successfully!")
            return

    print("Ticket not found.")


def main():

    while True:

        print("""
================================
       IT HELP DESK SYSTEM
================================

1. Create Ticket
2. View Tickets
3. Search Tickets
4. Update Ticket
5. Exit
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
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()  