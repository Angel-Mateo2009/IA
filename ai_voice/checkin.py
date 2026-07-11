import json
from datetime import datetime

ARCHIVO = "checkins.json"
def guardar_checkin(texto):

    try:
        with open(
            ARCHIVO,
            "r",
            encoding="utf-8"
        ) as f:

            datos = json.load(f)

    except:

        datos = []

    datos.append({
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "mensaje": texto
    })

    with open(
        ARCHIVO,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            datos,
            f,
            indent=4,
            ensure_ascii=False
        )
def es_checkin(texto):

    texto = texto.lower()

    claves = [
        "mi día",
        "hoy",
        "estudié",
        "entrené",
        "trabajé",
        "hice"
    ]

    return any(
        palabra in texto
        for palabra in claves
    )
def obtener_checkins():

    try:

        with open(
            ARCHIVO,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except:

        return []
def resumen_checkins():

    checkins = obtener_checkins()

    if not checkins:
        return "Todavía no tengo registros diarios."

    ultimos = checkins[-5:]

    textos = []

    for item in ultimos:
        textos.append(item["mensaje"])

    return " ".join(textos)