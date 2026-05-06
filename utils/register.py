import streamlit as st
from utils.db import cursor, conn

def register_user(username, password, role):
    try:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        return True
    except:
        return False