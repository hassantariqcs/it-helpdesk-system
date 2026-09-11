import sqlite3


DATABASE_NAME = "helpdesk.db"


def connect():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            issue TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_ticket(name, issue, priority):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tickets (name, issue, priority, status)
        VALUES (?, ?, ?, ?)
    """, (name, issue, priority, "Open"))

    connection.commit()
    connection.close()


def get_tickets():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def search_tickets(search):
    connection = connect()
    cursor = connection.cursor()

    search = f"%{search}%"

    cursor.execute("""
        SELECT * FROM tickets
        WHERE name LIKE ?
        OR issue LIKE ?
    """, (search, search))

    tickets = cursor.fetchall()

    connection.close()

    return tickets


def update_ticket_status(ticket_id, new_status):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    """, (new_status, ticket_id))

    connection.commit()

    rows_updated = cursor.rowcount

    connection.close()

    return rows_updated

def delete_ticket(ticket_id):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tickets
        WHERE id = ?
    """, (ticket_id,))

    connection.commit()

    rows_deleted = cursor.rowcount

    connection.close()

    return rows_deleted