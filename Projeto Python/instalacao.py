#Pegar o codigo da página já pronto da biblioteca(HTML)
import streamlit as st

st.title("Cadastro para adoção de animais")

nome = st.text_input("Qual o seu nome?")
idade = st.number_input("Qual a sua idade")