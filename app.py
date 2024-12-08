from flask import Flask, request, jsonify
import sqlite3
from models import Book, Member

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

# Book Endpoints
@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        book = Book(title=data['title'], author=data['author'], publication_year=data['publication_year'])
        book.save(conn)
        conn.commit()
        return jsonify({'message': 'Book added successfully'}), 201

    books = Book.get_all(conn)
    conn.close()
    return jsonify([book.to_dict() for book in books])

# ... similar routes for other book operations ...

# Member Endpoints
@app.route('/members', methods=['GET', 'POST'])
def members():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        member = Member(name=data['name'], email=data['email'])
        member.save(conn)
        conn.commit()
        return jsonify({'message': 'Member added successfully'}), 201

    members = Member.get_all(conn)
    conn.close()
    return jsonify([member.to_dict() for member in members])

# ... similar routes for other member operations ...

if __name__ == '__main__':
    app.run(debug=True)
