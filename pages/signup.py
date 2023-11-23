import streamlit as st
import sqlite3

from streamlit_extras.switch_page_button import switch_page 

def initial():
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

initial()

# database config
con = sqlite3.connect('userdb.db')
cur = con.cursor()

goback = st.button(":arrow_backward: Go back")
if goback:
    switch_page("main")

with open("static/style_signup.css") as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap">"""
            , unsafe_allow_html=True)

# main part start here
st.title("Sign up")

with st.form("signup"):
    username = st.text_input("username")
    password = st.text_input("password", type='password')
    confirm_password = st.text_input("confirm password", type='password')
    
    signup_submitted = st.form_submit_button("Register")

    if signup_submitted:

        # 1. check if this user is already exist
        alreadyexist = False

        res = cur.execute("SELECT * FROM userdb WHERE username=?", (username,))
        if res.fetchone() is not None:
            alreadyexist = True

        if alreadyexist:
            st.error('This username already exists. Please try again.')

        # 2. check if password and username are different
        elif username == password:
            st.error('Username can\'t be the same as password. Please try again.')

        # 3. check if confirmed password is the same as password
        elif password != confirm_password:
            st.error('Wrong password. Please try again.')

        # if all pass
        else:
            # add user to database
            cur.execute("""
                INSERT INTO userdb VALUES
                    (?,?);
            """, (username,password))

            cur.execute("""
                INSERT INTO score VALUES
                    (?,?,?,?);
            """, (username, 0, 0, 0))

            con.commit()

            st.session_state.username = username
            switch_page("mode")
