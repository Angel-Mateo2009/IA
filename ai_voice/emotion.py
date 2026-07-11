def detectar_emocion(texto):

    texto = texto.lower()

    emociones = {

        "feliz": [
            "feliz",
            "contento",
            "alegre"
        ],

        "triste": [
            "triste",
            "deprimido",
            "mal"
        ],

        "motivado": [
            "motivado",
            "emocionado",
            "con ganas"
        ],

        "cansado": [
            "cansado",
            "agotado",
            "sin energía"
        ],

        "estresado": [
            "estresado",
            "abrumado",
            "presionado"
        ],

        "frustrado": [
            "frustrado",
            "enojado",
            "molesto"
        ]
    }

    for emocion, palabras in emociones.items():

        for palabra in palabras:

            if palabra in texto:
                return emocion

    return None
def responder_emocion(emocion):

    respuestas = {

        "feliz":
            "Me alegra mucho que te sientas así. ¿Qué hizo que hoy fuera un buen día?",

        "triste":
            "Lamento que te sientas así. Si quieres hablar de ello, aquí estoy para escucharte.",

        "motivado":
            "¡Excelente! Aprovechemos esa motivación. ¿Cuál será tu siguiente paso?",

        "cansado":
            "Parece que hoy has tenido un día pesado. Descansar también es parte del progreso.",

        "estresado":
            "Entiendo. Cuando tenemos muchas cosas encima es fácil sentirse así. ¿Qué es lo que más te preocupa ahora mismo?",

        "frustrado":
            "Es normal sentirse frustrado cuando las cosas no salen como esperamos. Cuéntame qué ocurrió."
    }

    return respuestas.get(emocion)