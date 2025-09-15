# Asistente de voz con IA

Proyecto que transcribe audio/video y genera respuestas con GPT.
La API Key de OpenAI se carga desde un archivo .env para mayor seguridad.

## Tecnologías
- Python 3.13
- OpenAI API
- Faster-Whisper
- python-dotenv

## Instalación
1. Clona el repositorio (reemplaza tu_usuario por tu usuario de GitHub):
git clone https://github.com/buf1-0/asistente-voz-ia.git
cd asistente-voz-ia

2. Instala dependencias:
pip install -r requirements.txt

3. Crea un archivo .env en la carpeta del proyecto usando la plantilla .env.example:
OPENAI_API_KEY=TU_API_KEY_AQUI

## Cómo usar
1. Pon tus archivos de audio/video en la carpeta del proyecto (.mp3, .wav, .m4a, .mp4).
2. Ejecuta el script:
python main.py
3. Obtendrás en la consola la transcripción y la respuesta de GPT para cada archivo.

## Notas
- El archivo .env no debe subirse a GitHub (ya está en .gitignore).
- Compatible con múltiples archivos de audio/video en la carpeta.
- .env.example sirve como plantilla para que otros usuarios sepan cómo poner su API Key.