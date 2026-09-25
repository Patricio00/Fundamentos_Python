import streamlit as st
import numpy as np

st.title("Python Fundamentals")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Patricio Jarrín")
modulo = st.sidebar.selectbox("Seleccione un módulo",["Listas","Arreglos","Funciones","POO"])
if modulo == "Listas":
  st.write("Te encuentras en el módulo de listas")
  valor_inicial = st.number_input("Ingresa tu valor inicial",min_value = 0,max_value = 100,value = 10)
  valor_final = st.number_input("Ingresa tu valor final",min_value = 0,max_value = 100,value = 20)
  lista = list(range(int(valor_inicial),int(valor_final)))
  st.write(lista)
elif modulo == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")
  valor_inicial_array = st.number_input("Ingresa tu valor inicial del arreglo",min_value = 0,max_value = 100,value = 10)
  valor_final_array = st.number_input("Ingresa tu valor final del arreglo",min_value = 0,max_value = 100,value = 20)
  arreglo = list(range(int(valor_inicial_array),int(valor_final_array)))
  st.write(arreglo)  
elif modulo == "Funciones":
  st.write("Te encuentras en el módulo de funciones")
else:
  st.write("Te encuentras en el módulo de POO")
  
