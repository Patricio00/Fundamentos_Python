import streamlit as st

st.title("Python Fundamentals")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Patricio Jarrín")
modulo = st.sidebar.selectbox("Seleccione un módulo",["Listas","Arreglos","Funciones","POO"])
if modulo == "Listas":
  st.write("Te encuentras en el módulo de listas")
elif modulo == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")
elif modulo == "Funciones":
  st.write("Te encuentras en el módulo de funciones")
else:
  st.write("Te encuentras en el módulo de POO")
  
