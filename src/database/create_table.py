from create_database import connect
import psycopg2
from psycopg2 import extensions

conn = connect()
autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
conn.set_isolation_level(autocommit)
cursor = conn.cursor()

try:
    cursor.execute("""CREATE TABLE rsf_data (
        capacity int,
        time time without time zone,
        date date
        )""")
except:
    print("ERROR: table failed to create")

cursor.close()
conn.close()