import pyttsx3

hablando = False

def hablar(texto):

    global hablando

    hablando = True

    print("🔊 Nova hablando...")

    try:

        engine = pyttsx3.init()

        engine.setProperty('rate', 180)
        engine.setProperty('volume', 1)

        engine.say(texto)
        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print("ERROR TTS:", e)

    hablando = False

    print("✅ Nova terminó de hablar.")