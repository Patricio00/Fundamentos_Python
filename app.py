import streamlit as st
import numpy as np
import libreria_funciones as lf

st.sidebar.image ("Python.png",width=100)

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
  arreglo = np.arange(int(valor_inicial_array),int(valor_final_array))
  st.write(arreglo)  
elif modulo == "Funciones":
  st.write("Te encuentras en el módulo de funciones")
  principal = st.number_input("Monto del Préstamo", value=1000)
  tasa = st.numberinput("Tasa anual en decimal", value=0.15)
  anios = st.numberinput("Número de años del préstamo", value=1)
  pagos_por_anio = st.numberinput("Cantidad de Pagos por Año", value=12)
  cuota = lf.cuota_prestamo(principal,tasa,anios,pagos_por_anio)
  st.write (cuota)
else:
  st.write("Te encuentras en el módulo de POO")
  
