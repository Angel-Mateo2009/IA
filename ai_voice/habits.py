import json
import os

ARCHIVO = "habitos.json"

def guardar_habito(habito):
    if not os.path.exists(ARCHIVO):
        datos = []
    else:
        with open(ARCHIVO, "r") as f:
            datos = json.load(f)

    if habito not in datos:
        datos.append(habito)

    with open(ARCHIVO, "w") as f:
        json.dump(datos, f)

def obtener_habitos():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as f:
        return json.load(f)

def detectar_habito(texto):
    texto = texto.lower()

    palabras = ["estudiar", "gym", "ejercicio", "leer", "programar"]

    for p in palabras:
        if p in texto:
            return p

    return None