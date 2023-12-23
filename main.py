import streamlit as st
from IR_models.Retrieval import query_builder_andRetrieve
from pathlib import Path

st.title('Search platform')
st.text("By Shirin Dehghani")


query = st.text_input('Write your word or phrase Here')
api_key=st.text_input("please enter your openai api_key")
uploaded_file = st.file_uploader("Upload your PDF file Here", type="pdf")
if uploaded_file:
    save_path=Path("./temp", "The-Mom-Test-en.pdf")
    with open(save_path, mode='wb') as w:
            w.write(uploaded_file.getvalue())

if uploaded_file:
    response = query_builder_andRetrieve(query, api_key)
    st.write(response)