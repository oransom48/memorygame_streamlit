import streamlit as st

from streamlit_extras.switch_page_button import switch_page 

st.set_page_config(
    "Memorist",
    page_icon= "😎",
)

goback = st.button(":arrow_backward: Go back")
if goback:
    switch_page("main")

# main part start here
st.title("Sign up")

with st.form("signup"):
    username = st.text_input("username", key='username')
    password = st.text_input("password", type='password', key='password')
    confirm_password = st.text_input("confirm password", type='password')
    
    signup_submitted = st.form_submit_button("Register")

    if signup_submitted:

        # 1. check if this user is already exist
        alreadyexist = False
        with open("user.txt", 'r') as file:
            for i in file:
                u, p, a, b = i.strip().split(',')
                if u == username:
                    alreadyexist = True
                    break

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
            with open("user.txt", 'a') as file:
                file.write(f"{st.session_state.username},{st.session_state.password},0,0\n")
                st.success('Register successful')
            switch_page("main")
