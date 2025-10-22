# escreva um algorimo que solicite  do usuário um número e mostre a tabuada  de mutplicação  do número informado
import streamlit as st 


st.title (" Tabuada")

numero = st.number_input ("Digite um número: ")

if st.button ("Calculadora"):
    for i in range(1,11, 1):
        st.success (f"{numero} x {i} =  {numero  * 1 }")
