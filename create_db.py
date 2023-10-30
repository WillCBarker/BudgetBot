import sqlite3

class DatabaseManager:
    def __init__(self, db_name='financials.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Create Budget table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                allocated_amount REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expense (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT NOT NULL,
                frequency TEXT NOT NULL,
                budget_id INTEGER,
                FOREIGN KEY (budget_id) REFERENCES budget(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                source TEXT NOT NULL,
                amount REAL NOT NULL,
                frequency TEXT NOT NULL,
                date TEXT NOT NULL,
                budget_id INTEGER,
                FOREIGN KEY (budget_id) REFERENCES budget(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS investment (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                amount REAL NOT NULL,
                roi REAL NOT NULL,
                roi_frequency TEXT NOT NULL,
                description TEXT NOT NULL,
                maturity_date TEXT,
                budget_id INTEGER,
                FOREIGN KEY (budget_id) REFERENCES budget(id)
            )
        ''')

        self.conn.commit()
    # Other methods for interacting with the database...

# Usage
if __name__ == '__main__':
    # Creating an instance of the DatabaseManager
    db_manager = DatabaseManager()