import streamlit as st

st.title ("Verificando a idade ")


idade = st.number_input ("digite sua idade: ")

if st.button("verificar"):
    if idade < 18:
        st.write ("Menor de idade ")
    else:
        st.write ("Maior de idade. ")

else:
    st.warning("por favor, digite sua idade. ")