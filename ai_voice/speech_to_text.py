import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

fs = 16000

# cargar modelo
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

# -------------------------
# GRABAR AUDIO
# -------------------------

def grabar_audio():

    print("🎤 Habla ahora...")

    audio_total = []

    silencio = 0.15 

    while True:

        audio = sd.rec(
            int(0.5 * fs),
            samplerate=fs,
            channels=1,
            dtype='int16'
        )

        sd.wait()

        volumen = np.abs(audio).mean()

        audio_total.append(audio)

        # detectar silencio
        if volumen < 700:
            silencio += 1
        else:
            silencio = 0

        # terminar después de silencio
        if silencio > 5:
            break

    audio_final = np.concatenate(audio_total, axis=0)

    write("audio/input.wav", fs, audio_final)

    print("✅ Grabación terminada.")

# -------------------------
# AUDIO A TEXTO
# -------------------------

def audio_a_texto():

   segments, info = model.transcribe(
       "audio/input.wav",
       language="es"
)

   texto = ""

   for segment in segments:
       texto += segment.text
   return texto    