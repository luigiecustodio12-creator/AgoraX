import streamlit as st
import sqlite3
import pandas as pd
import datetime as datetime

conn = sqlite3.connect("data_base.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    supplier TEXT,
    image TEXT,
    owner TEXT,
    date_added TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer TEXT,
    product_id INTEGER,
    quantity INTEGER,
    product_name TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer TEXT,
    product_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    price REAL,
    total REAL,
    date TEXT
)
""")

conn.commit()