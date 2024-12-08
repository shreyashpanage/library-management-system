import sqlite3

class Book:
    def __init__(self, id, title, author, publication_year):
        self.id = id
        self.title = title
        self.author = author
        self.publication_year = publication_year

    @classmethod
    def get_all(cls, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        return [cls(*row) for row in rows]

    def save(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
                    (self.title, self.author, self.publication_year))
        self.id = cur.lastrowid
        conn.commit()

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'publication_year': self.publication_year}

# Similar implementation for Member class
