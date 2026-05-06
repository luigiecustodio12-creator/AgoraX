import streamlit as st
from utils.db import cursor, conn
import pandas as pd

st.subheader("PRODUCTS")

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

columns = ["ID", "Name", "Category", "Quantity", "Price", "Supplier", "Image", "Date"]

for row in rows:
    with st.container():

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(row[6], width=150)

        with col2:
            st.subheader(row[1])
            st.write(f"Category: {row[2]}")

        with col3:
            st.write(f"Price: ₱{row[4]}")
            st.write(f"Stock: {row[3]}")

            qty = st.number_input(
                "Quantity",
                min_value=1,
                max_value=row[3],
                value=1,
                key=f"qty_{row[0]}"
            )

            if st.button("ADD TO CART", key=f"cart_{row[0]}"):
                
                if not st.session_state.get("logged_in"):
                    st.error("Please log in first")
                else:
                    cursor.execute("""
                    INSERT INTO carts (buyer, product_id, product_name, price, quantity)
                    VALUES (?, ?, ?, ?, ?)
                    """, (
                        st.session_state.username,
                        row[0],
                        row[1],
                        row[4],
                        qty
                    ))
                    conn.commit()
                st.success("Added to cart")
