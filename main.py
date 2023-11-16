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

# head
st.write("welcome to")
st.title("Memorism")
st.markdown("How long can you remember?!")

col1, col2 = st.columns(2)

with col1:
    # log in
    login = st.button("Log in", use_container_width = True)
    if login:
        switch_page("login")

with col2:
    # guest
    asguest = st.button("Play as Guest", use_container_width = True)
    if asguest:
        st.session_state.username = "guest"
        switch_page("mode")



st.write("Don't have account?")
# sign up
signup = st.button("Sign Up Here!")
if signup:
    switch_page("signup")
