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

# database config
con = sqlite3.connect('userdb.db')
cur = con.cursor()

goback = st.button(":arrow_backward: Go back")
if goback:
    switch_page("main")

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
