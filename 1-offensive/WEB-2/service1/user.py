from psycopg import DatabaseError
from base64 import b64encode, b64decode
from db import get_connection
from flask_login import UserMixin
import hashlib

def hash(s: str):
    return hashlib.sha256(s.encode()).hexdigest()


class User(UserMixin):
    id: int
    username: str
    password: str

    def __init__(self, id, username, password):
        self.id = id
        self.username = username 
        self.password = password
    
    @staticmethod
    def get_by_id(id: int):
        conn = get_connection()
        if not conn:
            print("DB ERROR")
            return

        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM users WHERE id=%s;", (id,))
                res = cur.fetchone()
                if not res:
                    return
                return User(*res)
            except:
                return

    @staticmethod
    def get_by_username(username: str):
        conn = get_connection()
        if not conn:
            print("DB ERROR")
            return

        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM users WHERE username=%s;", (username,))
                res = cur.fetchone()
                if not res:
                    return
                return User(*res)
            except:
                return


    @staticmethod
    def auth(username: str, password: str):
        conn = get_connection()
        if not conn:
            print("DB ERROR")
            return


        with conn.cursor() as cur:
            try:
                hashed_password = hash(password)
                cur.execute("SELECT * FROM users WHERE username=%s AND password=%s;", (username, hashed_password,))
                res = cur.fetchone()
                if not res:
                    return
                return User(*res)
            except:
                return

    @staticmethod
    def register(username: str, password: str):

        user = User.get_by_username(username)
        if user:
            return 

        conn = get_connection()
        if not conn:
            print("DB ERROR")
            return
        with conn.cursor() as cur:
            try:
                hashed_password = hash(password)
                cur.execute("INSERT INTO users VALUES (DEFAULT, %s, %s) RETURNING id, username, password;", (username, hashed_password))
                conn.commit()
                res = cur.fetchone()
                if not res:
                    return
                return User(*res)
            except:
                return
