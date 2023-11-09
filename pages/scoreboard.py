import streamlit as st
import numpy as np
import pandas as pd

from streamlit_extras.switch_page_button import switch_page

gohome = st.button(":house: Home")
if gohome:
    switch_page("mode")

d = {'username': ['ComPogpog', 'Somsa_zaza', 'Oooom', 'Papapins'], 'highscore':[1,10000000,999,12345]}
scoreboard = pd.DataFrame(data = d)

st.dataframe(scoreboard.sort_values(by=['highscore'], ascending=False))