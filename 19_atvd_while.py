import streamlit as st

st.title(" Cálculo da Média do Aluno")

st.write("Digite duas notas entre 0 e 10. Se alguma nota for inválida, corrija para continuar.")


nota1 = st.number_input("Digite a 1ª nota:", min_value=0.0, max_value=10.0, step=0.1, format="%.2f")
nota2 = st.number_input("Digite a 2ª nota:", min_value=0.0, max_value=10.0, step=0.1, format="%.2f")


if st.button("Calcular Média"):
    media = (nota1 + nota2) / 2
    st.success(f" A média do aluno é: **{media:.2f}**")
