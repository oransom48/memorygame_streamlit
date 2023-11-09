import streamlit as st

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    "Memorist",
    page_icon= "😎",
)

st.title("Game over :(")

st.write(f"score: {st.session_state.score}")

# play again

col1, col2 = st.columns(2)

with col1:
    scoreboard = st.button("Scoreboard", use_container_width = True)
    if scoreboard:
        switch_page("scoreboard")

with col2:
    home = st.button("Home", use_container_width = True)
    if home:
        del st.session_state.ans
        del st.session_state.keylist
        del st.session_state.score
        switch_page("mode")


# st.session_state