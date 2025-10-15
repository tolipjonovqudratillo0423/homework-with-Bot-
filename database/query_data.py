import sqlite3
from .connect import get_connect

#bu database.db ga kerakli table yasab beradi 
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


#bu query insert query bulib u userni database.db saqlaydi
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

#bu query user registratsiya qilganmi tekshiradi agar malumot kelsa keyingi kod uni qilgan deydi agar none kelsa yoq
def check_user(chat_id):
    check_sql = "SELECT * FROM users WHERE chat_id = ?;"
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(check_sql, (chat_id,))
    user = cursor.fetchone()
    connect.close()
    return bool(user)

#bu query bizga userni malumotini olib beradi (name phone username lovation ) profil uchun ishlamoqda 
def get_user_data(chat_id):
    check_sql = "SELECT name, phone, username, location FROM users WHERE chat_id = ?;"
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(check_sql, (chat_id,))
    user = cursor.fetchall()
    connect.close()
    return user

#bu query title genre author buyicha malumot qidiradi uni BIZGA LIST QILIB ICHIDA KITOB NOMLARI BULIB KELADI 
def find_by_column(title=None, genre=None, author=None):
    title_sql = "SELECT * FROM books WHERE LOWER(title) LIKE LOWER(?);"
    author_sql = "SELECT * FROM books WHERE LOWER(author) LIKE LOWER(?);"
    genre_sql = "SELECT * FROM books WHERE LOWER(genre) LIKE LOWER(?);"

    connect = get_connect()
    cursor = connect.cursor()

    try:
        if title:
            cursor.execute(title_sql, (f"%{title}%",))
            
            result = cursor.fetchall()

        elif author:
            cursor.execute(author_sql, (f"%{author}%",))
            result = cursor.fetchall()
        elif genre:
            cursor.execute(genre_sql, (f"%{genre}%",))
            result = cursor.fetchall()
        else:
            result = "Hech Qanday kitoblar TOPILMADI"
        
        end_result = []
        for book in result:
            end_result.append(book[1])
        return end_result
    
    except Exception:
        return None
    finally:
        connect.close()


#BU QUERY ORDERS TABLE GA DATA QUSHADI 
def add_data_to_orders(book_id:int,user_id:int,quantity:int):
    with get_connect() as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO orders (book_id,user_id,quantity) values (?,?,?)",(book_id,user_id,quantity))
    db.commit()
    return None
create_important_table()
