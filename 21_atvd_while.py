import streamlit as st


st.title("Laço de repitição: While")

login_salvo = "marta"
senha_salva = "123"


st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)


login = st.text_input("Digite seu login: " , disabled=st.session_state.desabilitar)
senha = st.text_input("Digite sua senha: " , type= "password", disabled=st.session_state.desabilitar )


if st.button("Verificar"):
    if login == login_salvo and senha == senha_salva:
        st.success ("Bem vindo!")
    else:
        st.session_state.tentativas +=1
        if st.session_state.tentativas <=3:
            st.warning(f"Login ou senha inválidos, tentativas: {st.session_state.tentativas}")

        else:
            st.session_state.desabilitar = True
            st.error ("Número de tentativas inválidas")
            