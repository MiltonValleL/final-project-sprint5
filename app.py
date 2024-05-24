"""Archivo Python para trabajar con Streamlit"""
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('../final-project-sprint5/vehicles_us.csv') # leer los datos

st.header('Proyecto Final del Sprint 5 - Entorno de Desarrollo Individual') # Crear el encabezado

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma por tipo de vehículo')

if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de la columna "type"')

    # crear un histograma
    fig = px.histogram(car_data, x="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para la columna type')

    # se crea el histograma en plotly-express
    fig = px.scatter(car_data, x='type', y='price')

    # mostramos el gráfico interactivo de Plotly-Express
    st.plotly_chart(fig, use_container_width=True)

    st.write("Muchas gracias por revisar la información, que tengas un buen día.")
