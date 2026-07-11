import json
import os

ARCHIVO = "seguimiento.json"

def guardar_estado(habito, estado):
    if not os.path.exists(ARCHIVO):
        datos = {}
    else:
        with open(ARCHIVO, "r") as f:
            datos = json.load(f)

    datos[habito] = estado

    with open(ARCHIVO, "w") as f:
        json.dump(datos, f)

def obtener_estados():
    if not os.path.exists(ARCHIVO):
        return {}

    with open(ARCHIVO, "r") as f:
        return json.load(f)

def detectar_estado(texto):
    texto = texto.lower().split()

    positivos = ["sí", "si", "ya", "hecho", "cumplí"]
    negativos = ["no"]

    for p in positivos:
        if p in texto:
            return "si"

    for n in negativos:
        if n in texto:
            return "no"

    return None
ARCHIVO_ACTUAL = "estado_actual.json"

def guardar_habito_actual(habito):
    with open(ARCHIVO_ACTUAL, "w") as f:
        json.dump({"habito": habito}, f)

def obtener_habito_actual():
    if not os.path.exists(ARCHIVO_ACTUAL):
        return None

    with open(ARCHIVO_ACTUAL, "r") as f:
        datos = json.load(f)

    return datos.get("habito")