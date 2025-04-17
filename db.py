import pymysql

def get_connection():
    return pymysql.connect(
        host="host.docker.internal",  # Docker → Host connection
        user="root",
        password="Muthupattan@1403",
        database="retail_store",
        cursorclass=pymysql.cursors.DictCursor
    )
