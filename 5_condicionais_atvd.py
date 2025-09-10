import streamlit as st

st.title("Verificando média")

media = st.number_input("Digite a média: ")

if st.button("verificar"):
    if media >= 7:
        st.write("Aprovado")
    else:
        st.write("reprovado ")

else:
    st.write(" informe a média ") 