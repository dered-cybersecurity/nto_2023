import psycopg
import os
import time

def force_connect():
    global conn, cur

    is_connected = False
    while not is_connected:
        try:
            print("[+] Trying to connecting to db")
            is_connected = True
            conn = psycopg.connect(f"postgresql://{PG_LOGIN}:{PG_PASSWORD}@{PG_HOST}:5432/{PG_DB}")
        except:
            is_connected = False
        time.sleep(1)
    cur = conn.cursor()

    print("[+] Connected!")

PG_HOST = os.environ.get("PG_HOST", "127.0.0.1")
PG_LOGIN = os.environ.get("PG_LOGIN", "postgres")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "postgres")
PG_DB = os.environ.get("PG_DB", "ctf")


def get_connection():
    global PG_HOST, PG_LOGIN, PG_PASSWORD, PG_DB
    try:
        a = psycopg.connect(f"postgresql://{PG_LOGIN}:{PG_PASSWORD}@{PG_HOST}:5432/{PG_DB}")
        return a
    except:
        return



force_connect()


cur.execute("CREATE TABLE IF NOT EXISTS users ( id SERIAL PRIMARY KEY, username VARCHAR(64), password VARCHAR(64));")
conn.commit()
