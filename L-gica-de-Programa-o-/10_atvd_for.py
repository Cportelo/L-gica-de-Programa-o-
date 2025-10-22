# escrever um algoritimo  que solicite ao usuário um  número e faça contagem
# regressiva a partir do número informando até o número 1, aguardado um  segundo para exebir cada número 

import streamlit as st 
import time 

numero = st.number_input("Digite um Número: ", step=1)
if st.button ("Clique"):

    for i in range(numero,1, -1):
        st.success (i)
        time.sleep(1)