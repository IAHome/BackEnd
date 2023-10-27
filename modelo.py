# -*- coding: utf-8 -*-
import os
import pickle
import openai
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from dotenv import load_dotenv

load_dotenv()
#openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = "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"

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

def obtener_consejo_financiero(cluster, datos):

    genero = datos["Genero"]
    edad = datos["Edad"]
    comuna = datos["comuna"]
    vivienda = datos["TipoVivienda"]
    personas = datos["TotalpersonasH"]
    ingresos = datos["SumaIngresosLAB"]
    gastos = datos["SumaGastos"]

    tipos_vivienda = {
        1: "Casa",
        2: "Apartamento",
        3: "Cuartos",
        4: "Vivienda Indigente",
        5: "Otro"
    }

    gens = {
        1: "Hombre",
        2: "Mujer"
    }

    gen = gens.get(genero)

    tipo_vivienda = tipos_vivienda.get(vivienda)


    # Define los clústeres y los consejos asociados a cada uno
    consejos_por_cluster = {
        0: "Debería ahorrar y realizar la búsqueda de nuevas oportunidades que le permitan incrementar sus ingresos.",
        1: "Debe buscar nuevas oportunidades de ingreso.",
        2: "Puede invertir, ahorrar y relalizar gastos ociosos.",
        3: "Puede ahorrar y relizar gastos ociosos."
        # Puedes agregar más clústeres y consejos según sea necesario
    }

    clus = consejos_por_cluster.get(cluster)

    base = f"Tengo {edad} años de edad, género {gen}, vivo en la comuna {comuna} de Medellín en una vivienda de tipo {tipo_vivienda}. En mi hogar, hay un total de {personas} personas sin incluirme. Mis ingresos mensuales son de {ingresos} pesos colombianos y los gastos mensuales son de {gastos} pesos colombianos. ¿Puedes darme un consejo financiero realista basado en esta información? Por favor habla de forma profesional y que sea personalizado, menciona los datos necesarios, ten también en cuenta este consejo el cual se definió mediante clustering {cluster}"

    # Obtén el consejo asociado al clúster
    consejo = consejos_por_cluster.get(cluster, "Consejo genérico si el clúster no se encuentra en la lista.")

    # Usa GPT-3.5 para generar un consejo más detallado basado en el clúster
    if cluster in consejos_por_cluster:
        prompt = f"Tengo 4 cluster de personas con datos economicos, dame consejos para el cluster número: Cluster {cluster}: {base}"
        respuesta_gpt = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500  # Ajusta el número de tokens según sea necesario
        )
        consejo_detallado = respuesta_gpt.choices[0].text.strip()
        return consejo_detallado

    return consejo

