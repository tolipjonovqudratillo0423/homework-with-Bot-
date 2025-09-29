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
        title varchar(100) not null unique,
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
