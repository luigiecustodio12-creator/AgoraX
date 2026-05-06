import streamlit as st
from utils.products import add_products
import os

if st.session_state.get("role") != "SELLER":
    st.error("Access Denied. Sellers Only")
    st.stop()

st.subheader("ADD NEW PRODUCTS")

image = st.file_uploader("Upload Product Image", type=["png", "jpg", "jpeg"])
name = st.text_input("Product Name")
category = st.text_input("Category")
quantity = st.number_input("Quantity", min_value=1, step=1)
price = st.number_input("Price", min_value=0.00)
supplier = st.text_input("Supplier")

if st.button("Add Products"):
    if name and category and supplier and image:
        
        os.makedirs("assets/products", exist_ok=True)

        image_path = f"assets/products/{image.name}"

        with open(image_path, "wb") as f:
            f.write(image.getbuffer())

        add_products(name, category, quantity, price, supplier, image_path, st.session_state.username)
        st.success("Product Has Been Added Successfully")
    else:
        st.error("Please Fill in all fields")