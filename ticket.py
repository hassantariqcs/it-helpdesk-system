class Ticket:
    def __init__(self, ticket_id, name, issue, priority):
        self.ticket_id = ticket_id
        self.name = name
        self.issue = issue
        self.priority = priority
        self.status = "Open"

    def update_status(self, new_status):
        self.status = new_status

    def display(self):
        print(f"""
Ticket ID: {self.ticket_id}
User: {self.name}
Issue: {self.issue}
Priority: {self.priority}
Status: {self.status}
-------------------------
""")