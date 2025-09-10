import streamlit as st 



st.title("CalCUladora")

n_1 = st.number_input("Digite o primeiro número: ")
n_2 = st.number_input(" Digite o segundo número: ")


soma = n_1 + n_2 
media= (n_1 + n_2) / 2 
prduto = n_1 * n_2 
menor_valor = min (n_1, n_2)
maior_valor = max (n_1, n_2)

if st.button("Calcular"):
    st.success(" calculos realizados com sucesso ")

st.write (f"O maior valor foi o : {maior_valor} ")
st.write (f"valores da media foi o: {media} ")
st.write (f"valores do produto foi o: {prduto}")
st.write (f"menor valor é o : {menor_valor} ")
st.write (f"maior valor é o : {maior_valor}")
