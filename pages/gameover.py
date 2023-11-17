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

with open("static/style_gameover.css") as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap">"""
            , unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap">"""
            , unsafe_allow_html=True)

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
    restart = st.button("Restart", use_container_width = True)
    if restart:
        del st.session_state.ans
        del st.session_state.keylist
        del st.session_state.score
        switch_page("mode")

# st.session_state
