import streamlit as st
import time

st.title ("LAÇO DE LOGIN")

usuario1 = "cr7@gmail.com"
senha1 = "123456"

usuario = st.text_input("Digite seu email.")
senha = st.text_input("Digite sua senha: ", type="password")


if st.button("Login"):

    if usuario == usuario1 and senha == senha1:
        st.success ("Bem-Vindo ele, ela, elu ")
    
    else:
        st.error("Não sabe nem seu login burro !")

