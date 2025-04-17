import pymysql

def get_connection():
    return pymysql.connect(
        host="13.233.10.137",  # or host.docker.internal
        user="root",
        password="Muthupattan@1403",
        database="retail_store",
        cursorclass=pymysql.cursors.DictCursor
    )

