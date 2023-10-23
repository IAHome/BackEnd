# -*- coding: utf-8 -*-
import pickle
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Cargar el modelo KMeans previamente entrenado
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Cargar el escalador previamente entrenado
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Función para predecir el clúster para un nuevo registro
def predecir_cluster(nuevo_registro):
    # Crear un DataFrame con el nuevo registro
    nuevo_registro_df = pd.DataFrame([nuevo_registro])
    
    # Escalar las características del nuevo registro
    nuevo_registro_df_scaled = scaler.transform(nuevo_registro_df[['Genero', 'Edad', 'comuna', 'TipoVivienda', 'TotalpersonasH', 'SumaIngresosAUX', 'SumaIngresosLAB', 'SumaIngresosExt', 'SumaGastos']])
    
    # Predecir el clúster usando el modelo KMeans
    cluster_predicho = kmeans_model.predict(nuevo_registro_df_scaled)
    resultado_serializable = int(cluster_predicho[0])
    
    # Devolver la predicción del clúster
    return resultado_serializable
