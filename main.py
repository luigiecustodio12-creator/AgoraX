import streamlit as st
from utils.auth import auth_user

st.set_page_config(layout="wide")
st.logo("assets/logo.png", size="large")

if "cart" not in st.session_state:
    st.session_state.cart = []

Home_page = st.Page(
    page= "views/home.py",
    title= "Home",
    icon= ":material/home:"
)

User_page = st.Page(
    page= "views/user.py",
    title= "User",
    icon= ":material/account_circle:"
)

Product_page = st.Page(
    page= "views/product.py",
    title= "Product",
    icon= ":material/shopping_bag:"
)

Cart_page = st.Page(
    page= "views/cart.py",
    title= "Add To Cart",
    icon= ":material/shopping_cart:"
)

Checkout_page = st.Page(
    page= "views/checkout.py",
    title= "Check Out",
    icon= ":material/bucket_check:"
)

Inventory_page = st.Page(
    page= "views/inventory.py",
    title= "Invetory",
    icon= ":material/inventory:"
)

Product_add_page = st.Page(
    page= "views/add.py",
    title= "Add Product",
    icon= ":material/add:"
)

Product_del_page = st.Page(
    page= "views/delete.py",
    title= "Delete Products",
    icon= ":material/delete:"
)

pages = {
    "Info": [Home_page, User_page],
    "Dashboard": [Product_page, Cart_page, Checkout_page],
}

if "logged_in" in st.session_state and st.session_state.get("role") == "SELLER":
    pages["Seller Dashboard"] = [Inventory_page, Product_add_page, Product_del_page]

pg = st.navigation(pages)
pg.run()

if "logged_in" in st.session_state:
    st.sidebar.success(f"Logged in as {st.session_state.username}")

if st.sidebar.button("LOGOUT"):
    if "logged_in" in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = "GUESS"
        st.session_state.role = ""
        st.rerun()

st.sidebar.text("MADE BY GROUP 8 💖")
st.sidebar.text("FINAL EXAMMINATION PROJECT")