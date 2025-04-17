import pymysql

def get_connection():
    return pymysql.connect(
        host=" 172.17.0.1 ",   # <--- FIXED THIS
        user="root",
        password="Muthupattan@1403",
        database="retail_store",
        cursorclass=pymysql.cursors.DictCursor
    )
