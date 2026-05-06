import streamlit as st
from utils.register import register_user
from utils.login import login_user

def auth_user():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = "GUESS"
        st.session_state.role = ""

    if not st.session_state.logged_in:
        menu = st.selectbox("MENU", ["LOGIN", "REGISTER"])

        if menu == "LOGIN":
            st.subheader("LOGIN")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                user = login_user(username, password)
                
                if user:    
                    st.session_state.logged_in = True
                    st.session_state.username = user[1]
                    st.session_state.role = user[3]
                    st.rerun()
                else:
                    st.error("INVALID USERNAME OR PASSWORD")

        if menu == "REGISTER":
            st.subheader("REGISTER")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            role = st.selectbox("ROLE", ["BUYER", "SELLER"])

            if st.button("Register"):
                if register_user(username, password, role):
                    st.success("ACCOUNT HAS BEEN CREATED")
                else:
                    st.error("Username already EXISTS")