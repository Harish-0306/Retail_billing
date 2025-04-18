import pymysql

def get_connection():
    return pymysql.connect(
        host="172.31.45.106",  # or host.docker.internal
        user="root",
        password="Muthupattan@1403",
        database="retail_store",
        cursorclass=pymysql.cursors.DictCursor
    )

