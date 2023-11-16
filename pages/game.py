import random
import time

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

# session_state: score, keylist, ans
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'keylist' not in st.session_state:
    st.session_state.keylist = '0'
if 'ans' not in st.session_state:
    st.session_state.ans = ''

class sequence:
    def __init__(self):
        # question
        self.listnum = ['0','1','2','3','4','5','6','7','8','9']
        self.listchar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
        self.listmix = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

    def choice(self):
        if st.session_state.mode == 'Character':
            return self.listchar
        elif st.session_state.mode == 'Mix it all':
            return self.listmix
        else:
            return self.listnum

    def check(self):
        if st.session_state.ans == st.session_state.keylist:
            st.session_state.score += 1
            st.session_state.keylist = ''
            for i in range(st.session_state.score + 1):
                new = random.choice(self.choice())
                st.session_state.keylist += new
        else:
            switch_page("gameover")

# go to main page
restart = st.button(":repeat: Restart")
if restart:
    del st.session_state.ans
    del st.session_state.keylist
    del st.session_state.score
    switch_page("mode")

st.title('Game start!')
st.write("enter '0' to start game (and get 1 point for :rainbow[free] :smile:)")

question = sequence()

col1, col2 = st.columns(2)

with col2: 
    answer = st.text_input("answer")
    st.session_state.ans = answer
    submit = st.button("Submit")
    if submit:
        del answer
        question.check()
    st.write(f"Your score: { st.session_state.score }")

with col1:
    question = st.session_state.keylist    
    with st.empty():
        for i in range(len(question)):
            st.subheader(f"digit {i+1}: :red[{question[i]}]")
            time.sleep(1)
        st.write("Time to answer!")
    
# temp
# st.write(st.session_state)
