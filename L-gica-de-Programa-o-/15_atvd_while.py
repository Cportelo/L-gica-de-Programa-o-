import streamlit as st

st.title("Lógica de Programação")

st.header("Laço de repetição")

while True:
    numero = st.number_input ("Digite um número:", step=1 )
    if numero == 2:
        break
st.header("FIM") 
   
