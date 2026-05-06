import streamlit as st
from utils.db import cursor
from utils.products import delete_product


if st.session_state.get("role") != "SELLER":
    st.error("Access Denied. Sellers Only")
    st.stop()

st.subheader("DELETE PRODUCT")

cursor.execute("SELECT id, product_name FROM products WHERE owner=?", (st.session_state.username,))
products = cursor.fetchall()

for row in products:
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(f"{row[1]}")
    with col2: 
        if st.button("DELETE", key=row[0]):
            delete_product(row[0], st.session_state.username)
            st.success(f"{row[1]} deleted")
            st.rerun()