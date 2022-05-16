import mysql.connector

def conectar():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        db='master_python',
        port=3306
        )
    cursor = db.cursor(buffered=True)

    return [db, cursor]