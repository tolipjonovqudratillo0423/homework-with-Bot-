from sqlite3 import connect
# bu bizi database.db ga ulash uchun
def get_connect(query=None):
    return connect("database.db")
    



