import streamlit as st
from utils.auth import auth_user

auth_user()
    
if st.session_state.logged_in:
    col1, col2, col3 = st.columns(3, gap="medium", vertical_alignment="center")
    with col1:
        st.image("assets/User_prof1.png")
    with col2:
        st.metric("Username", st.session_state.username)
    with col3:
        st.metric("Role", st.session_state.role)