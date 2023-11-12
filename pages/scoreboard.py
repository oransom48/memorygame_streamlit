import streamlit as st
import numpy as np
import pandas as pd
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

gohome = st.button(":house: Home")
if gohome:
    del st.session_state.ans
    del st.session_state.keylist
    del st.session_state.score
    switch_page("mode")

mode = st.selectbox(
    "Please choose :rainbow[game mode]",
    ('Number', 'Character', 'Mix it all'),
)

# database config
con = sqlite3.connect('userdb.db')
cur = con.cursor()

if mode == 'Number':
    sql_query = pd.read_sql_query("""
        SELECT username, int FROM score
        WHERE NOT int = 0
        ORDER BY int, username;
    """, con)
    scoreboard = pd.DataFrame(sql_query, columns = ['username', 'int'])
    st.subheader("Number mode")
    st.dataframe(scoreboard)

elif mode == 'Character':
    sql_query = pd.read_sql_query("""
        SELECT username, char FROM score
        WHERE NOT char = 0
        ORDER BY char, username;
    """, con)
    scoreboard = pd.DataFrame(sql_query, columns = ['username', 'char'])
    st.subheader("Character mode")
    st.dataframe(scoreboard)

elif mode == 'Mix it all':
    sql_query = pd.read_sql_query("""
        SELECT username, mix FROM score
        WHERE NOT mix = 0
        ORDER BY mix, username;
    """, con)
    scoreboard = pd.DataFrame(sql_query, columns = ['username', 'mix'])
    st.subheader("Mix it all mode")
    st.dataframe(scoreboard)

    con.commit()

# st.session_state
