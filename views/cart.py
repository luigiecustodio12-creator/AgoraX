import streamlit as st
from utils.db import cursor, conn

st.subheader("🛒 CART")

cursor.execute("""
SELECT id, product_id, product_name, price, quantity FROM carts WHERE buyer=?
""", (st.session_state.username,))

items = cursor.fetchall()

if len(items) == 0:
    st.info("Cart is empty")
    st.stop()

total = 0

for item in items:

    cart_id, product_id, name, price, qty = item
    subtotal = price * qty
    total += subtotal

    with st.container():
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(name)
        with col2:
            st.write(f"Qty: {qty}")
        with col3:
            st.write(f"Price: ₱{subtotal}")
            st.write(f"### Total: ₱{total}")

            if st.button("Remove Item", key=f"del_{cart_id}"):
                cursor.execute("""
                DELETE FROM carts
                WHERE id=? AND buyer=?
                """, (cart_id, st.session_state.username))
                conn.commit()
                st.rerun()
