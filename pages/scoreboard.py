import streamlit as st
import numpy as np
import pandas as pd
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

gohome = st.button(":house: Home")
if gohome:
    del st.session_state.ans
    del st.session_state.keylist
    del st.session_state.score
    switch_page("mode")

mode = st.selectbox(
    "game mode",
    ('Number', 'Character', 'Mix it all'),
)

with open("style_scoreboard.css") as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap">"""
            , unsafe_allow_html=True)
st.markdown("""<link rel="stylesheet" 
            href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap">"""
            , unsafe_allow_html=True)

# database config
con = sqlite3.connect('userdb.db')
cur = con.cursor()

if mode == 'Number':
    sql_query = pd.read_sql_query("""
        SELECT username, int FROM score
        WHERE NOT int = 0
        ORDER BY int DESC;
    """, con)
    scoreboard = pd.DataFrame(sql_query, columns = ['username', 'int'])
    scoreboard.rename(columns={'int':'highest score'}, inplace = True)
    st.subheader("Number mode")
    st.dataframe(
        scoreboard, 
        hide_index = True, 
        use_container_width = True
    )

elif mode == 'Character':
    sql_query = pd.read_sql_query("""
        SELECT username, char FROM score
        WHERE NOT char = 0
        ORDER BY char DESC;
    """, con)
    scoreboard = pd.DataFrame(sql_query, columns = ['username', 'char'])
    scoreboard.rename(columns={'char':'highest score'}, inplace = True)
    st.subheader("Character mode")
    st.dataframe(
        scoreboard, 
        hide_index = True, 
        use_container_width = True
    )

elif mode == 'Mix it all':
    sql_query = pd.read_sql_query("""
        SELECT username, mix FROM score
        WHERE NOT mix = 0
        ORDER BY mix DESC;
    """, con)
    scoreboard = pd.DataFrame(sql_query, columns = ['username', 'mix'])
    scoreboard.rename(columns={'mix':'highest score'}, inplace = True)
    st.subheader("Mix it all mode")
    st.dataframe(
        scoreboard, 
        hide_index = True, 
        use_container_width = True
    )

con.commit()

# st.session_state
