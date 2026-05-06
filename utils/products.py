import streamlit as st
from utils.db import conn, cursor
from datetime import datetime
import pandas as pd
import os

def add_products(product_name, category, quantity, price, supplier, image_path, owner):
    cursor.execute("""
    INSERT INTO products (product_name, category, quantity, price, supplier, image, owner, date_added) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
    (product_name, category, quantity, price, supplier, image_path, owner, datetime.now().strftime("%Y-%m-%d"))
    )
    conn.commit()

def get_products():
    return pd.read_sql_query("SELECT * FROM products", conn)

def delete_product(product_id, owner):
    cursor.execute("DELETE FROM products WHERE id=? AND owner=?", (product_id, owner))
    result = cursor.fetchone()

    if result and result[0]:
        if os.path.exists(result[0]):
            os.remove(result[0])
            
    cursor.execute("DELETE FROM products WHERE id=? AND owner=?", (product_id, owner))
    conn.commit()