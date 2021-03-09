import sqlite3

class Database():
    """sqlite3 database class that holds testers jobs"""
    DB = "listings.db"

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(Database.DB)
        self.cur = self.connection.cursor()

    def close(self):

        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def executemany(self, many_new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.executemany('REPLACE INTO hosts VALUES(?, ?, ?, ?)', many_new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS hosts(title text, \
                                                            job_id integer PRIMARY KEY, 
                                                            company text,
                                                            age integer)''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()