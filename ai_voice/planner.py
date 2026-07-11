def detectar_tareas(texto):
    palabras_clave = [
        "tarea", "tareas", "estudiar", "estudio",
        "gym", "ejercicio", "entrenar",
        "trabajo", "proyecto", "deberes"
    ]

    texto = texto.lower()
    tareas = []

    for palabra in palabras_clave:
        if palabra in texto:
            tareas.append(palabra)

    return list(set(tareas))


def crear_plan(tareas):
    if not tareas:
        return None

    plan = "Enfócate en esto hoy:\n"

    for i, t in enumerate(tareas[:3], 1):
        plan += f"{i}. {t}\n"

    plan += "Empieza por la primera ahora."

    return plan