import streamlit as st
import sqlite3

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    "Memorism",
    page_icon= "😎",
    initial_sidebar_state="collapsed",
)

# hide sidebar
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

#link style
with open("stylized.css") as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)
# database config
con = sqlite3.connect('userdb.db')
cur = con.cursor()

goback = st.button(":arrow_backward: Go back")
if goback:
    switch_page("main")

# main program
st.title("Log in")

with st.form("login"):

    username = st.text_input(
        "username", 
    )
    password = st.text_input(
        "password", 
        type='password', 
    )
    login_submitted = st.form_submit_button("Log In")

    if login_submitted:

        res = cur.execute("SELECT * FROM userdb WHERE username=?", (username,))
        temp = res.fetchone()
        if temp is None:
            st.error("Invalid user. Please try again.")
        else:
            u, p = temp
            if u == username and p != password:
                st.error("Incorrect password. Please try again.")
            elif u == username and p == password:
                st.session_state.username = username
                switch_page("mode")
                