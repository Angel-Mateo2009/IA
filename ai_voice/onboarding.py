def perfil_completo(perfil):

    campos = [
        "nombre",
        "edad",
        "como_quiere_ser_llamado",
        "meta_principal"
    ]

    for campo in campos:

        if not perfil.get(campo):
            return False

    return True
def siguiente_pregunta(perfil):

    if not perfil.get("nombre"):
       return (
        "Hola. Soy Nova. "
        "Me gustaría conocerte mejor para poder ayudarte. "
        "¿Cómo te llamas?"
    )

    if not perfil.get("edad"):
       return (
        f"Mucho gusto, {perfil.get('nombre')}. "
        "¿Qué edad tienes?"
    )

    if not perfil.get("como_quiere_ser_llamado"):
       return (
        "Perfecto. "
        "¿Cómo te gustaría que te llamara?"
    )

    if not perfil.get("meta_principal"):
       return (
        "Última pregunta por ahora. "
        "¿Cuál es la meta más importante que te gustaría alcanzar?"
    )
    return None
import json

from memory import obtener_perfil

PERFIL = "perfil_usuario.json"

def guardar_campo(campo, valor):

    perfil = obtener_perfil()

    perfil[campo] = valor

    with open(PERFIL, "w", encoding="utf-8") as f:
        json.dump(
            perfil,
            f,
            indent=4,
            ensure_ascii=False
        )
def campo_faltante(perfil):

    if not perfil.get("nombre"):
        return "nombre"

    if not perfil.get("edad"):
        return "edad"

    if not perfil.get("como_quiere_ser_llamado"):
        return "como_quiere_ser_llamado"

    if not perfil.get("meta_principal"):
        return "meta_principal"

    return None