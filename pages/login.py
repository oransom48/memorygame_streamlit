import streamlit as st

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    "Memorist",
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

        # open user.txt file to check whether this username is valid and paaword is correct
        with open("user.txt", 'r') as file:
            for i in file:
                u, p, a, b = i.strip().split(',')

                if u == username and p != password:
                    st.error("Incorrect password. Please try again.")
                elif u == username and p == password:
                    st.session_state.username = u
                    switch_page("mode")

            st.error("Invalid user. Please try again.")
                