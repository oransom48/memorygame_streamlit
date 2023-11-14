import streamlit as st

from streamlit_extras.switch_page_button import switch_page 

# session_state: username
if 'username' not in st.session_state:
    st.session_state.username = "guest"

st.set_page_config(
    "Memorism",
    page_icon= "😎",
    initial_sidebar_state="collapsed",
)

with open("style_main.css") as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap">"""
            , unsafe_allow_html=True)
st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap">"""
            , unsafe_allow_html=True)
# hide sidebar
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

# head
st.write("welcome to")
st.title("Memorism")
st.markdown(
    "How long can you :rainbow[remember]?!"
)

col1, col2 = st.columns(2)

with col1:
    # log in
    login = st.button("Log In", use_container_width = True)
    if login:
        switch_page("login")

with col2:
    # guest
    asguest = st.button("Play as Guest", use_container_width = True)
    if asguest:
        st.session_state.username = "guest"
        switch_page("mode")

st.divider()

st.write("Don't have account?")
# sign up
signup = st.button("Sign Up Here!")
if signup:
    switch_page("signup")
