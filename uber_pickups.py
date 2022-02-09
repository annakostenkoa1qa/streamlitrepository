import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.write(df)

import streamlit as st
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))