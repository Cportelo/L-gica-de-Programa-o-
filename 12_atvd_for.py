import streamlit as st
import time



st.title("Contador de Números Pares e Ímpares")

numeros = []
for i in range(5):
    numero = st.number_input(f"Digite o {i+1}º número inteiro:", step=1, format="%d", key=i)
    numeros.append(numero)

if st.button("Contar Pares e Ímpares"):
    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = 5 - pares

    st.write(f" Quantidade de números pares: **{pares}**")
    st.write(f" Quantidade de números ímpares: **{impares}**")
