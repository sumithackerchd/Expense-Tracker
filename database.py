import sqlite3

def create_database():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        expense_date TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_expense(title, amount, expense_date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (title, amount, expense_date) VALUES (?, ?, ?)",
        (title, amount, expense_date)
    )

    conn.commit()
    conn.close()


def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    conn.close()

    return expenses

def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()
    conn.close()
    

def search_expense(title):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE title LIKE ?",
        ('%' + title + '%',)
    )

    results = cursor.fetchall()

    conn.close()

    return results