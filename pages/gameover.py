import streamlit as st
import sqlite3

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

# database config
con = sqlite3.connect('userdb.db')
cur = con.cursor()

# body
st.title("Game over :(")

st.write(f"score: {st.session_state.score}")

# score
if st.session_state.username != 'guest':
    res = cur.execute("SELECT * FROM score WHERE username = ?", (st.session_state.username,))
    temp = res.fetchone()
    username, intmode, charmode, mixmode = temp

    if st.session_state.mode == 'Number' and intmode < st.session_state.score:
        cur.execute("""
            UPDATE score
            SET int = ?
            WHERE username = ?;
        """, (st.session_state.score, st.session_state.username,))
        st.write(f"{st.session_state.username} got new high score!")
    elif st.session_state.mode == 'Character' and charmode < st.session_state.score:
        cur.execute("""
            UPDATE score
            SET char = ?
            WHERE username = ?;
        """, (st.session_state.score, st.session_state.username,))
        st.write(f"{st.session_state.username} got new high score!")
    elif st.session_state.mode == 'Mix it all' and mixmode < st.session_state.score:
        cur.execute("""
            UPDATE score
            SET mix = ?
            WHERE username = ?;
        """, (st.session_state.score, st.session_state.username,))
        st.write(f"{st.session_state.username} got new high score!")

con.commit()

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
