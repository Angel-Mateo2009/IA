from habits import guardar_habito, obtener_habitos, detectar_habito
from user_knowledge import analizar_usuario
from emotion import detectar_emocion, responder_emocion
from patterns import analizar_tendencias
from patterns import generar_conclusiones
def crear_contexto(texto):
    return {
        "texto": texto,
        "emocion": None,
        "habito": None,
        "aprendio": False,
        "accion": None,
        "respuesta": None,
        "analisis": {}
    }
    


def comprender(contexto):
    texto = contexto["texto"]

# -------------------------
# APRENDER DEL USUARIO
# -------------------------

    aprendio = analizar_usuario(texto)

    contexto["aprendio"] = aprendio

# -------------------------
# APRENDER HÁBITOS
# -------------------------

    contexto["habito"] = detectar_habito(texto)

    if contexto["habito"]:
     guardar_habito(contexto["habito"])

# -------------------------
# EMOCIONES
# -------------------------

    contexto["emocion"] = detectar_emocion(texto)

    if contexto["emocion"]:
        contexto["respuesta"] = responder_emocion(
         contexto["emocion"]
    )

def analizar(contexto):
    
    texto = contexto["texto"].lower()
    if (
     "como voy" in texto
     or "estoy mejorando" in texto
     or "he progresado" in texto
    ):
     contexto["analisis"]["consulta_tendencias"] = True
    if (
     "como me ha ido" in texto
     or "que patrones ves" in texto
     or "qué patrones ves" in texto
    ):
     contexto["analisis"]["consulta_patrones"] = True 
def decidir(contexto):
    if contexto["analisis"].get("consulta_tendencias"):
     contexto["accion"] = "mostrar_tendencias"
    if contexto["analisis"].get("consulta_patrones"):
     contexto["accion"] = "mostrar_patrones"
def responder(contexto):
    if contexto["accion"] == "mostrar_tendencias":
     return analizar_tendencias()
    if contexto["accion"] == "mostrar_patrones":
     return generar_conclusiones()
    return contexto["respuesta"]

def procesar_mensaje(texto):

    contexto = crear_contexto(texto)
    comprender(contexto)
    analizar(contexto)
    decidir(contexto)
    respuesta = responder(contexto)
     
    return respuesta
