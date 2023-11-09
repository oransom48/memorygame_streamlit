import random
import time

import streamlit as st

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    "Memorist",
    page_icon= "😎",
)

# session_state: score, keylist, ans
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'keylist' not in st.session_state:
    st.session_state.keylist = '0'
if 'ans' not in st.session_state:
    st.session_state.ans = ''

def checkstate():
    if st.session_state.ans == st.session_state.keylist:
        st.session_state.score += 1

        new = random.randrange(0, 10)
        new = str(new)
        st.session_state.keylist += new
    else:
        switch_page("gameover")

# go to main page
gohome = st.button(":house: Home")
if gohome:
    switch_page("main")

st.title('Game start!')
st.write("enter '0' to start game (and get 1 point for :rainbow[free] :smile:)")

col1, col2 = st.columns(2)

with col1:
    answer = st.text_input("answer")
    st.session_state.ans = answer
    submit = st.button("Submit")
    if submit:
        del answer
        checkstate()
        st.write(f"Your score: { st.session_state.score }")

with col2:
    question = st.session_state.keylist    
    with st.empty():
        for i in range(len(question)):
            st.write(f"degit {i+1}")
            st.header(f"{question[i]}")
            time.sleep(1)
        st.write("Time to answer!")
    
# temp
st.write(st.session_state)
