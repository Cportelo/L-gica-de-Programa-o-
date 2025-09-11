# escrever um algoritimo que moestre números  ímpares entre 1 e 20

import streamlit as st 
import time

st.title ("Atividade: 2 ")

st.header ("Laço de repitição")

if st.button ("Iniciar"):
    for i in range (1,21, 2):
        st.info(i)
        time.sleep(1)
    st.header("FIM")    