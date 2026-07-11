from datetime import datetime
from collections import defaultdict
from checkin import obtener_checkins
from collections import Counter
def analizar_checkins():
    registros = obtener_checkins()

    categorias = []

    palabras_clave = {
        "programacion": [
            "python",
            "programacion",
            "programé",
            "codigo",
            "codifique",
            "proyecto",
            "software",
            "nova"
        ],

        "ejercicio": [
            "ejercicio",
            "entrene",
            "entrené",
            "gym",
            "gimnasio",
            "corrí",
            "corri",
            "pesas"
        ],

        "lectura": [
            "leí",
            "lei",
            "leer",
            "libro",
            "lectura"
        ],

        "estudio": [
            "estudie",
            "estudié",
            "aprendi",
            "aprendí",
            "curso",
            "clase"
        ]
    }

    for registro in registros:

        texto = registro["mensaje"].lower()

        for categoria, palabras in palabras_clave.items():

            for palabra in palabras:

                if palabra in texto:
                    categorias.append(categoria)
                    break

    return Counter(categorias)
def generar_conclusiones():
    conteo = analizar_checkins()

    if not conteo:
        return "Todavía no tengo suficientes registros para analizar patrones."

    principal = conteo.most_common(1)[0]

    categoria = principal[0]
    cantidad = principal[1]

    return (
        f"Has registrado {cantidad} actividades relacionadas con "
        f"{categoria}. Parece ser una de tus principales áreas de enfoque."
    )
from patterns import generar_conclusiones

print(generar_conclusiones())
def analizar_tendencias():
    registros = obtener_checkins()

    if len(registros) < 3:
        return "Todavía necesito más registros para detectar tendencias."
    actividad_por_dia = defaultdict(int)

    for registro in registros:

        fecha = registro["fecha"]

        texto = registro["mensaje"].lower()

        if (
            "python" in texto
            or "programacion" in texto
            or "proyecto" in texto
            or "nova" in texto
        ):
            actividad_por_dia[fecha] += 1
    valores = list(actividad_por_dia.values())
    if len(valores) < 3:
        return "Aún no hay suficientes datos para analizar tendencias."
    inicio = valores[0]
    final = valores[-1]
    if final > inicio:
        return (
            "Tu actividad relacionada con programación "
            "ha aumentado con el tiempo."
        )
    elif final < inicio:
        return (
            "Tu actividad relacionada con programación "
            "ha disminuido recientemente."
        )
    else:
        return (
            "Tu actividad relacionada con programación "
            "se ha mantenido bastante constante."
        )