import json
import os

ARCHIVO = "memoria.json"

def guardar(tipo, mensaje):

    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            json.dump([], f)

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        datos = json.load(f)

    datos.append({
        "tipo": tipo,
        "mensaje": mensaje
    })

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as f:
        return json.load(f)
def obtener_recientes(limite=5):

    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        datos = json.load(f)

    recientes = datos[-limite:]

    conversaciones = []

    for item in recientes:

        tipo = item["tipo"]
        mensaje = item["mensaje"]

        conversaciones.append(f"{tipo}: {mensaje}")

    return conversaciones   

IMPORTANT_FILE = "important_memory.json"
def guardar_importante(mensaje):

    importantes = []

    try:
        with open(IMPORTANT_FILE, "r", encoding="utf-8") as f:
            importantes = json.load(f)

    except:
        importantes = []

    importantes.append(mensaje)

    with open(IMPORTANT_FILE, "w", encoding="utf-8") as f:
        json.dump(importantes, f, indent=4, ensure_ascii=False)
def es_importante(texto):

    claves = [
        "quiero",
        "mi meta",
        "mi objetivo",
        "me gusta",
        "estoy aprendiendo",
        "voy a",
        "planeo",
        "sueño",
        "quiero mejorar"
    ]

    texto = texto.lower()

    for clave in claves:
        if clave in texto:
            return True

    return False
def obtener_importantes():

    try:
        with open(IMPORTANT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return []    
PERFIL_FILE = "perfil_usuario.json"
def obtener_perfil():

    perfil_base = {
        "nombre": "",
        "edad": "",
        "como_quiere_ser_llamado": "",
        "meta_principal": "",

        "metas": [],
        "habitos": [],
        "proyectos": [],
        "aprendizaje": [],
        "pasiones": [],
        "intereses": [],
        "fortalezas": [],
        "debilidades": [],
        "miedos": [],
        "valores": [],
        "gustos": []
    }

    try:

        with open(PERFIL_FILE, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for clave, valor in perfil_base.items():

            if clave not in datos:
                datos[clave] = valor

        return datos

    except:

        return perfil_base
def guardar_perfil(categoria, dato):

    perfil = obtener_perfil()

    if dato not in perfil[categoria]:
        perfil[categoria].append(dato)

    with open(PERFIL_FILE, "w", encoding="utf-8") as f:
        json.dump(
            perfil,
            f,
            indent=4,
            ensure_ascii=False
        )
def clasificar_info(texto):

    texto = texto.lower()

    if "quiero" in texto or "meta" in texto:
        return "metas"

    if "ejercicio" in texto:
        return "habitos"

    if "leer" in texto:
        return "habitos"

    if "proyecto" in texto:
        return "proyectos"

    if "programación" in texto:
        return "aprendizaje"

    return None                