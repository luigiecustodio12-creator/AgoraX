import streamlit as st
from utils.db import cursor

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = "Guest"

if "role" not in st.session_state:
    st.session_state.role = ""

st.title("🛒 Welcome to AgoraX")
st.write(f"Logged in as: **{st.session_state.username}**")
st.write(f"Role: **{st.session_state.role}**")

search = st.text_input("Search products")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🛍 Products", "Browse")

with col2:
    st.metric("🛒 Cart", "View Items")

with col3:
    st.metric("💳 Orders", "Checkout History")

cursor.execute("SELECT * FROM products LIMIT 5")
products = cursor.fetchall()

st.subheader("🔥 Featured Products")

for p in products:
    st.image(p[6], width=120)
    st.write(p[1])
    st.write(f"₱{p[4]}")
    st.divider()

if st.session_state.role == "SELLER":
    st.success("Seller Dashboard")
    st.write("Manage your products and inventory")
else:
    st.success("Buyer Dashboard")
    st.write("Browse and shop products")

if st.button("Go to Products"):
    st.switch_page("views/product.py")

if st.button("Go to Cart"):
    st.switch_page("views/cart.py")

st.metric("Total Products", len(products))