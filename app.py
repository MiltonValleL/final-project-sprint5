"""Archivo Python para trabajar con Streamlit"""
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('../vehicles_us.csv') # leer los datos

st.header('Proyecto Final del Sprint 5 - Entorno de Desarrollo Individual') # Crear el encabezado

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # se crea el histograma en plotly-express
    fig = px.histogram(car_data, x='type')

    # mostramos el gráfico interactivo de Plotly-Express
    st.plotly_chart(fig, use_container_width=True)
