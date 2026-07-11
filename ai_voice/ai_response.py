from memory import obtener_perfil
from memory import obtener_importantes
from memory import obtener_recientes
import requests
from memory import cargar

def generar_respuesta(texto):
    memoria = cargar()
    contexto = ""

    for item in memoria:

     if isinstance(item, dict):

        tipo = item["tipo"]
        mensaje = item["mensaje"]

        contexto += f"{tipo}: {mensaje}\n"

    else:
        contexto += str(item) + "\n"
    memoria = obtener_recientes()

    contexto = ""

    for item in memoria:

     if isinstance(item, dict):

        tipo = item["tipo"]
        mensaje = item["mensaje"]

        contexto += f"{tipo}: {mensaje}\n"

    else:
        contexto += str(item) + "\n"

        importantes = obtener_importantes()
    
        contexto_importante = "\n".join(importantes)
    perfil = obtener_perfil()
    perfil_texto = f"""
    Metas:
    {perfil["metas"]}

    Habitos:
    {perfil["habitos"]}

    Proyectos:
    {perfil["proyectos"]}

    Aprendizaje:
    {perfil["aprendizaje"]}
"""
    prompt = f"""
Eres Nova, un asistente personal inteligente y humano.

Tu objetivo es ayudar al usuario a:
- mejorar cada día
- cumplir hábitos
- mantener disciplina
- organizar su vida
- avanzar hacia sus metas

Hablas:
- natural
- breve
- inteligente
- como una persona real
- nunca como robot

Sabes que el usuario:
- quiere ir a Japón
- trabaja en proyectos
- quiere mejorar física y mentalmente
- busca disciplina y progreso

Responde de manera útil, coherente y humana.
Perfil del usuario:

{perfil_texto}
Conversaciones recientes:
{contexto}
Usuario: {texto}
Información importante del usuario:
{contexto_importante}
Respuesta:
"""
    print("MEMORIA:", contexto)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]