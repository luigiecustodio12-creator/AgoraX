import streamlit as st
from utils.db import cursor
import pandas as pd

if st.session_state.get("role") != "SELLER":
    st.error("Access Denied. Sellers Only")
    st.stop()

cursor.execute("SELECT * FROM products WHERE owner=?", (st.session_state.username,))
data = cursor.fetchall()

st.write(pd.DataFrame(data, columns=[
    "ID", "Name", "Category", "Quantity", "Price", "Supplier", "Image", "Owner", "Date"
]))