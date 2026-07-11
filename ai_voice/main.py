from brain import procesar_mensaje
from checkin import resumen_checkins
from checkin import (
    guardar_checkin,
    es_checkin
)
from onboarding import (
    obtener_perfil,
    siguiente_pregunta,
    guardar_campo, 
    campo_faltante
)
from memory import guardar_perfil, clasificar_info
from memory import (
    guardar,
    guardar_importante,
    es_importante
)
import time
from habits import guardar_habito, obtener_habitos, detectar_habito
from tracker import (
    guardar_estado,
    obtener_estados,
    detectar_estado,
    guardar_habito_actual,
    obtener_habito_actual
)

from planner import detectar_tareas, crear_plan
from speech_to_text import grabar_audio, audio_a_texto
from ai_response import generar_respuesta
from text_to_speech import hablar, hablando
from memory import guardar

print("🚀 Iniciando AI...")

def main():

    print("🔥 Entró al main")

    while True:

        print("🎤 Habla ahora...")
        if hablando:
           continue
        grabar_audio()

        
        texto = audio_a_texto()

        if not texto:
            continue
 
        if not texto.strip():
            print("⚠ No se detectó voz.")
            continue
        if len(texto.strip()) < 3:
            print("⚠ Texto demasiado corto.")
            continue
        print("🧠 Tú:", texto)
        
        respuesta_brain = procesar_mensaje(texto)

        if respuesta_brain:

         print("🤖 Nova:", respuesta_brain)

         guardar("Nova", respuesta_brain)

         hablar(respuesta_brain)

         continue
        
        if es_checkin(texto):
            guardar_checkin(texto)
        perfil = obtener_perfil()

        campo = campo_faltante(perfil)

        if campo:
         guardar_campo(campo, texto)

        perfil = obtener_perfil()
        pregunta = siguiente_pregunta(perfil)

        if "salir" in texto.lower():
            break

        guardar("Usuario", texto)
        categoria = clasificar_info(texto)

        if categoria:
            guardar_perfil(categoria, texto)
        if es_importante(texto):
            guardar_importante(texto)

        # -------------------------
        # HÁBITOS
        # -------------------------

        habitos = obtener_habitos()

        # -------------------------
        # SEGUIMIENTO
        # -------------------------

        estado = detectar_estado(texto)

        if estado:
            habito_actual = obtener_habito_actual()

            if habito_actual:
                guardar_estado(habito_actual, estado)

        estados = obtener_estados()

        seguimiento = ""

        for h in habitos:
            if h not in estados:
                seguimiento = f"¿Ya cumpliste tu hábito de {h} hoy?"
                guardar_habito_actual(h)
                break

        # -------------------------
        # PLANIFICADOR
        # -------------------------

        tareas = detectar_tareas(texto)
        plan = crear_plan(tareas)

        # -------------------------
        # RECORDATORIO
        # -------------------------

        if habitos:
            recordatorio = "Tus hábitos son: " + ", ".join(habitos)
        else:
            recordatorio = ""

        # -------------------------
        # RESPUESTA FINAL
        # -------------------------

        if pregunta:
            respuesta = pregunta

        if pregunta:
            respuesta = pregunta

        elif campo and not siguiente_pregunta(perfil):
            respuesta = (
        f"Perfecto {perfil['como_quiere_ser_llamado']}. "
        f"Entiendo que tu meta principal es "
        f"{perfil['meta_principal']}. "
        f"A partir de ahora intentaré ayudarte "
        f"a avanzar hacia ella."
    )

        elif plan:
            respuesta = plan

        else:
            respuesta = generar_respuesta(
              texto + ". " + recordatorio
    )
        if not respuesta or respuesta.strip() == "":
            respuesta = "No entendí bien, intenta otra vez."
        print("🤖 AI:", respuesta)
        guardar("Nova", respuesta)
        hablar(respuesta)
        time.sleep(2)

if __name__ == "__main__":
    main()