import os
from faster_whisper import WhisperModel
from openai import OpenAI
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configura tu API Key de OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Función para transcribir audio
def transcribir(audio_path):
    model = WhisperModel("small", device="cpu")  # usa "cuda" si tienes GPU
    segments, _ = model.transcribe(audio_path)
    texto = " ".join([seg.text for seg in segments])
    return texto

# Función para preguntar a GPT
def preguntar_gpt(texto):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": texto}]
    )
    return completion.choices[0].message.content

# Flujo principal
if __name__ == "__main__":
    # Busca todos los archivos de audio/video en la carpeta
    audio_files = [f for f in os.listdir() if f.endswith(('.mp3', '.wav', '.m4a', '.mp4'))]

    if not audio_files:
        print("No se encontró ningún archivo de audio/video en la carpeta.")
    else:
        for audio in audio_files:
            print(f"\n[+] Procesando: {audio}")
            texto = transcribir(audio)
            print("Texto reconocido:", texto)

            print("\n[+] Preguntando a GPT...")
            respuesta = preguntar_gpt(texto)
            print("Respuesta de GPT:", respuesta)