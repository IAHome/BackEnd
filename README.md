# Aplicación de Agrupación de Datos

Esta es una aplicación simple desarrollada con Flask que proporciona un servicio de agrupación de datos.

## Requisitos

- Python 3.x
- Flask (puedes instalarlo usando `pip install flask`)

## Configuración

1. Clona este repositorio en tu máquina local:

2. Instala las dependencias:

3. Para correrlo se ejecuta python3 app.py


## Uso

1. Ejecuta la aplicación:

python app.py


La aplicación estará disponible en `http://localhost:5000`.

2. Realiza una solicitud a la API:

- **Endpoint:** `/agrupar`
- **Método:** `POST`
- **Cuerpo de la solicitud:** Envia un JSON con los siguientes parámetros:
  - `Edad`: Edad de la persona (número entero).
  - `Genero`: Género de la persona (cadena de texto).
  - `comuna`: Comuna de residencia (cadena de texto).
  - `TipoVivienda`: Tipo de vivienda (cadena de texto).
  - `TotalpersonasH`: Número total de personas en el hogar (número entero).
  - `SumaIngresosAUX`: Suma de ingresos auxiliares (número entero).
  - `SumaIngresosLAV`: Suma de ingresos laborales (número entero).
  - `SumaIngresosExt`: Suma de ingresos extra (número entero).
  - `SumaGastos`: Suma de gastos (número entero).

Ejemplo de solicitud en cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "Edad": 30,
    "Genero": "Femenino",
    "comuna": "Ejemplo",
    "TipoVivienda": "Casa",
    "TotalpersonasH": 3,
    "SumaIngresosAUX": 50000,
    "SumaIngresosLAV": 70000,
    "SumaIngresosExt": 20000,
    "SumaGastos": 30000
}' http://localhost:5000/agrupar

Deberías recibir una respuesta con el grupo correspondiente.
