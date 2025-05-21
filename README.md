# Traductor de Voz Español-Inglés

Este proyecto es un traductor de voz que convierte el habla en español a audio en inglés utilizando tecnologías de IA. Utiliza Whisper para la transcripción, el paquete `translate` para la traducción y ElevenLabs para la síntesis de voz.

## Características

- Transcripción de voz en español usando Whisper
- Traducción de texto español a inglés
- Síntesis de voz en inglés usando ElevenLabs
- Interfaz web amigable con Gradio

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Una cuenta en ElevenLabs (para la API key)

## Instalación

1. Clona este repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd voiceTranslator
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install gradio faster-whisper translate python-dotenv elevenlabs
```

4. Crea un archivo `.env` en la raíz del proyecto con tu API key de ElevenLabs:
```
ELEVENLABS_API_KEY=tu_api_key_aquí
```

## Uso

1. Asegúrate de tener todas las dependencias instaladas y el archivo `.env` configurado.

2. Ejecuta el script principal:
```bash
python main.py
```

3. Abre tu navegador en la URL que se muestra en la terminal (generalmente http://127.0.0.1:7860)

4. En la interfaz web:
   - Haz clic en el botón de grabación
   - Habla en español
   - El sistema transcribirá tu voz, traducirá el texto y generará un audio en inglés

## Estructura del Proyecto

```
voiceTranslator/
├── main.py           # Script principal
├── .env             # Archivo de configuración (no incluido en el repositorio)
├── audios/          # Directorio donde se guardan los audios generados
└── README.md        # Este archivo
```

## Tecnologías Utilizadas

- [Gradio](https://gradio.app/) - Para la interfaz web
- [Faster Whisper](https://github.com/guillaumekln/faster-whisper) - Para la transcripción de voz
- [Translate](https://pypi.org/project/translate/) - Para la traducción de texto
- [ElevenLabs](https://elevenlabs.io/) - Para la síntesis de voz

## Notas Importantes

- El modelo de Whisper está configurado para usar CPU por defecto. Si tienes una GPU compatible, puedes modificar el código para usarla.
- La calidad de la traducción depende de la claridad del audio de entrada.
- Se requiere una conexión a internet para usar las APIs de ElevenLabs.

## Solución de Problemas

Si encuentras algún error:

1. Verifica que todas las dependencias estén instaladas correctamente
2. Asegúrate de que tu API key de ElevenLabs sea válida
3. Comprueba que el directorio `audios/` exista y tenga permisos de escritura
4. Verifica que tu micrófono esté funcionando correctamente

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios que te gustaría hacer.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
