import streamlit as st

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    "Memorist",
    page_icon= "😎",
)

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
    ('Number', 'Character'),
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