import streamlit as st

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

with open("style_mode.css") as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap">"""
            , unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap">"""
            , unsafe_allow_html=True)

# go to main page
if st.session_state.username == 'guest':
    login = st.button(":information_desk_person: Log in")
    if login:
        switch_page("main")
else:
    logout = st.button(":information_desk_person: Log out")
    if logout:
        del st.session_state.username
        switch_page("main")



# main program
st.write(f"Welcome {st.session_state.username} to Memorism!")
st.title("Game Mode")

# select game mode
mode = st.selectbox(
    "Please choose :rainbow[game mode]",
    ('Number', 'Character', 'Mix it all'),
    index=None,
    placeholder="Game mode",
)

start = st.button("Start")

# session_state: mode
if 'mode' not in st.session_state:
    st.session_state.mode = mode

# go to game page
if start:
    st.session_state.mode = mode
    switch_page("game")

# st.session_state
