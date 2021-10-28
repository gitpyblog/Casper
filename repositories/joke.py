import sqlite3
from datetime import datetime


class JokeRepository:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def execute(self, query, data):
        self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor

    def execute_no_data(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def save(self, joke, author, created_at=datetime.now()):
        return self.execute(
            'INSERT INTO jokes (joke, author, record_data) VALUES (?, ?, ?)',
            (joke, author, created_at)
        ).fetchone()

    def get_by_name(self, joke_id):
        return self.execute('SELECT joke, author, record_data FROM jokes WHERE joke=?', (joke_id,)).fetchone()

    def get_random(self):
        return self.execute_no_data('SELECT joke, author, record_data FROM jokes ORDER BY random() LIMIT 1').fetchone()

    def __del__(self):
        self.connection.close()
