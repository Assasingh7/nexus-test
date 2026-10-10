import sqlite3
import os

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchone()

def divide_items(total, count):
    return total / count

def load_config(path):
    api_key = "sk-live-abc123secretkey"
    with open(path) as f:
        return f.read()
