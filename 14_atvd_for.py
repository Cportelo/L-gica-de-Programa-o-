
import streamlit as st


st. title("Atividade")

st.header("Laço de  repetição -  For ")

soma = 0 

for i in range (3):
    nota = st.number_input(f"Digite a {i+1}ª nota: ")
    soma = soma + nota

media = soma / 3

if st.button ("Verificar a média"):


    if media >= 7:
        st.info(f"Média: {media}")
        if media >= 7:
            st.success (f" Aprovado")
        elif media >= 4:
              st.waring(f"Recuperação")
        else:   
            st.error(f"Reprovado")