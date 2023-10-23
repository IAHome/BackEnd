# -*- coding: utf-8 -*-
import pickle
import openai
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

openai.api_key = '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'

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

def obtener_consejo_financiero(cluster):
    # Define los clústeres y los consejos asociados a cada uno
    consejos_por_cluster = {
        0: "Consejo para el clúster 0.",
        1: "Consejo para el clúster 1.",
        2: "Consejo para el clúster 2.",
        3: "Consejo para el clúster 3."
        # Puedes agregar más clústeres y consejos según sea necesario
    }

    # Obtén el consejo asociado al clúster
    consejo = consejos_por_cluster.get(cluster, "Consejo genérico si el clúster no se encuentra en la lista.")

    # Usa GPT-3.5 para generar un consejo más detallado basado en el clúster
    if cluster in consejos_por_cluster:
        prompt = f"Tengo 4 cluster de personas con datos economicos, dame consejos para el cluster número: Cluster {cluster}: {consejo}"
        respuesta_gpt = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150  # Ajusta el número de tokens según sea necesario
        )
        consejo_detallado = respuesta_gpt.choices[0].text.strip()
        return consejo_detallado

    return consejo
