from connect import get_connect
from time import sleep
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
for i in find_by_column(title="a"):
    sleep(5)
    print(i)