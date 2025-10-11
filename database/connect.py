from sqlite3 import connect

def get_connect(query=None):
    return connect("database.db")
    



