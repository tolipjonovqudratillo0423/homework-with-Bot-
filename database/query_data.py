from .connect import get_connect

def create_important_table():
    
    users_table = """
    create table if not exists users(
        id bigserial primary key,
        chat_id bigint not null unique,
        name varchar(100) not null,
        username varchar(100) not null unique,
        phone varchar(100) not null unique,
        location varchar(200) not null,
        is_admin boolean default False
    );
    """

    books_table = """
    create table if not exists books(
        id bigserial primary key,
        title varchar(100) not null,
        genre varchar(255) not null ,
        author varchar(100) not null,
        description text,
        quantity integer default 1,
        price integer not null
    );
    """

    orders_table = """
    create table if not exists orders(
        id bigserial primary key,
        user_id bigint references users(id),
        book_id bigint references books(id),
        status varchar(100) default 'new',
        quantity integer default 1,
        created_at timestamp default now(),
        updated_at timestamp default now()
    );
    """

    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(users_table)
            cursor.execute(books_table)
            cursor.execute(orders_table)


def insert_query(chat_id, name, phone, username, location):
    insert_sql = """
    insert into users(chat_id, name, phone, username, location)
    values(%s, %s, %s, %s, %s) returning *;
    """
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(insert_sql, (chat_id, name, phone, username, location))
            user = cursor.fetchone()
            connect.commit()
            return user

def check_user(chat_id):
    check_sql = """
    select * from users where chat_id = %s;
    """
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(check_sql, (chat_id,))
            user = cursor.fetchone()
            connect.commit()

            if user:
                return True
            else:
                return False
def get_user_data(chat_id):
    check_sql = """
    select name , phone , username , location from users where chat_id = %s;
    """
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(check_sql, (chat_id,))
            user = cursor.fetchall()
            connect.commit()
            return user
# def search_by_title(title):
#     search_sql="""
#     select * from books where title ilike '%%s%' """
#     with get_connect() as connect:
#         with connect.cursor() as cursor :
#             cursor.execute(search_sql,(title))
#             books = cursor.fetchall()
#             connect.commit()
#             return books 
# def search_by_genre(genre):
#     search_sql="""
#     select * from books where genre ilike '%%s%'"""
#     with get_connect() as connect:
#         with connect.cursor() as cursor :
#             cursor.execute(search_sql,(genre))
#             books = cursor.fetchall()
#             connect.commit()
#             return books
# def search_by_author(author):
#     search_sql="""
#     select * from books where author ilike '%%s%' """
#     with get_connect() as connect:
#         with connect.cursor() as cursor :
#             cursor.execute(search_sql,(author))
#             books = cursor.fetchall()
#             connect.commit()
#             return books

def find_by_column(title=None,genre=None,author = None):
    title_sql ="""
    select * from books where title ilike '%%s%'"""
    author_sql = """
    select * from books where author ilike '%%s%'"""
    genre_sql = """
    select * from books where genre ilike '%%s%'"""

    if title:
        try:
            with get_connect() as connect:
                with connect.cursor() as cursor :
                    cursor.execute(title_sql,(title))
                    return cursor.fetchall()
                    
        except:            
            return None
    elif author:
        try:
            with get_connect() as connect:
                with connect.cursor() as cursor :
                    cursor.execute(author_sql,(author))
                    return cursor.fetchall()
        except :        
            return None
    elif genre:
        try:
            with get_connect() as connect:
                with connect.cursor() as cursor :
                    cursor.execute(genre_sql,(genre))
                    return cursor.fetchall()
        except:      
            return None
    else:
        return "Hech Qanday kitoblar TOPILMADI"




