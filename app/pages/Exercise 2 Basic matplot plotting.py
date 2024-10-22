
import streamlit as st

st.title('Exercise 2: Basic matplot plotting')

st.code("git clone https://github.com/rug-oop-2024/tutorial_3")

st.markdown("""
Tasks:
- Use glob to get all csv files in the directory
- Use selectbox to select a dataset
- Import the library and based on the number of columns selected, plot the data accordinly from the plotter.
""")

option = st.selectbox(glob("**/*.csv", recursive=True))
if option is None:
  st.write('Please selectsomething')
else:
  df = pd.read_csv(option)
  st.write(df.head())

options = st.multiselect(df.columns)

