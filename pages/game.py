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

# question
listnum = ['0','1','2','3','4','5','6','7','8','9']
listchar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

listchoice = []
if st.session_state.mode == 'Character':
    listchoice = listchar
else:
    listchoice = listnum

def checkstate():
    if st.session_state.ans == st.session_state.keylist:
        st.session_state.score += 1
        st.session_state.keylist = ''
        for i in range(st.session_state.score + 1):
            new = random.choice(listchoice)
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
            # st.write(f"digit {i+1}")
            st.header(f"digit {i+1}: :red[{question[i]}]")
            time.sleep(1)
        st.write("Time to answer!")
    
# temp
# st.write(st.session_state)