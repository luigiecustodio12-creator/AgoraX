import streamlit as st
from utils.db import cursor, conn

st.subheader("CHECKOUT")

cursor.execute("""
SELECT product_id, product_name, price, quantity
FROM carts
WHERE buyer=?
""", (st.session_state.username,))

items = cursor.fetchall()

total = 0

for item in items:
    product_id, name, price, qty = item
    total += price * qty

st.write(f"### Total: ₱{total}")

# FORM FIX
with st.form("checkout_form"):
    email = st.text_input("Email Address")
    fullname = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Shipping Address")
    payment = st.selectbox(
        "Payment Method",
        ["Gcash", "Cash on delivery", "Paymaya", "Debit Card"]
    )

    submitted = st.form_submit_button("CONFIRM CHECKOUT")

if submitted:
    if email and fullname and phone and address:
        for item in items:
            product_id, name, price, qty = item
            subtotal = price * qty

            cursor.execute("""
            INSERT INTO orders (buyer, product_id, product_name, quantity, price, total, date)
            VALUES (?, ?, ?, ?, ?, ?, date('now'))
            """, (
                st.session_state.username,
                product_id,
                name,
                qty,
                price,
                subtotal
            ))

        cursor.execute("""
        DELETE FROM carts WHERE buyer=?
        """, (st.session_state.username,))

        conn.commit()

        st.success("Checkout successful!") 
    else:
        st.error("Please fill all fields")