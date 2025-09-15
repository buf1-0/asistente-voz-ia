from faster_whisper import WhisperModel
from openai import OpenAI

# Configura tu API Key de OpenAI
OPENAI_API_KEY = "TU_API_KEY"
client = OpenAI(api_key=OPENAI_API_KEY)

# Función para transcribir audio
def transcribir(audio_path):
	tab = WhisperModel("small", device="cpu")  # usa "cuda" si tienes GPU
	segments, _ = tab.transcribe(audio_path)
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
	audio = "audio.mp3"  # tu archivo de prueba
	print("[+] Transcribiendo audio...")
	texto = transcribir(audio)
	print("Texto reconocido:", texto)

	print("\n[+] Preguntando a GPT...")
	respuesta = preguntar_gpt(texto)
	print("Respuesta de GPT:", respuesta)
