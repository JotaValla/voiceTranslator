import gradio as gr
from faster_whisper import WhisperModel 
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

def translator(audio_file):
    try:
        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(audio_file, language="es")
        transcription = " ".join([segment.text for segment in segments])
    except Exception as e:
        raise gr.Error(f"Error al transcribir el audio: {e}")
    
    #2 Traducir texto
    try:
        translator_obj = Translator(from_lang="es", to_lang="en")
        translated_text = translator_obj.translate(transcription)
    except Exception as e:
        raise gr.Error(f"Error al traducir el texto: {e}")
        
    #3 Generar audio traducido usando ElevenLabs
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=translated_text,
            model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
    except Exception as e:
        raise gr.Error(f"Error al generar el audio traducido: {e}")
    
    #4 Guardar audio traducido
    save_path = "audios/en.mp3"
    with open(save_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    
    return save_path
        
web = gr.Interface(
    fn=translator,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs=[gr.Audio(label="Audio traducido")],
    title="Voice Translator",
    description="Translate spoken language to text",
)

web.launch()
