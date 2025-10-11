import sqlite3
from .connect import get_connect


def create_important_table():
    users_table = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL UNIQUE,
        name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL UNIQUE,
        location TEXT NOT NULL,
        is_admin INTEGER DEFAULT 0
    );
    """

    books_table = """
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        author TEXT NOT NULL,
        description TEXT,
        quantity INTEGER DEFAULT 1,
        price INTEGER NOT NULL
    );
    """

    orders_table = """
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(id),
        book_id INTEGER REFERENCES books(id),
        status TEXT DEFAULT 'new',
        quantity INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """

    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(users_table)
    cursor.execute(books_table)
    cursor.execute(orders_table)
    connect.commit()
    connect.close()


def insert_query(chat_id, name, phone, username, location):
    insert_sql = """
    INSERT INTO users(chat_id, name, phone, username, location)
    VALUES (?, ?, ?, ?, ?);
    """
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(insert_sql, (chat_id, name, phone, username, location))
    user_id = cursor.lastrowid
    connect.commit()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    connect.close()
    return user


def check_user(chat_id):
    check_sql = "SELECT * FROM users WHERE chat_id = ?;"
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(check_sql, (chat_id,))
    user = cursor.fetchone()
    connect.close()
    return bool(user)


def get_user_data(chat_id):
    check_sql = "SELECT name, phone, username, location FROM users WHERE chat_id = ?;"
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(check_sql, (chat_id,))
    user = cursor.fetchall()
    connect.close()
    return user


def find_by_column(title=None, genre=None, author=None):
    title_sql = "SELECT * FROM books WHERE LOWER(title) LIKE LOWER(?);"
    author_sql = "SELECT * FROM books WHERE LOWER(author) LIKE LOWER(?);"
    genre_sql = "SELECT * FROM books WHERE LOWER(genre) LIKE LOWER(?);"

    connect = get_connect()
    cursor = connect.cursor()

    try:
        if title:
            cursor.execute(title_sql, (f"%{title}%",))
            return cursor.fetchall()
        elif author:
            cursor.execute(author_sql, (f"%{author}%",))
            return cursor.fetchall()
        elif genre:
            cursor.execute(genre_sql, (f"%{genre}%",))
            return cursor.fetchall()
        else:
            return "Hech Qanday kitoblar TOPILMADI"
    except Exception:
        return None
    finally:
        connect.close()
        
