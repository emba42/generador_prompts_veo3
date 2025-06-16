import streamlit as st
from transformers import pipeline
import random

st.title("🧠 Generador de Prompts para VEO 3")
st.write("Este bot toma tu idea en cualquier idioma, la traduce y la mejora para que funcione con VEO 3.")

# Simulación de 20 ejemplos como base de estilo (simplificados)
prompt_ejemplos = [
    "In the back seat of a 90s taxi with worn fabric and soft lighting...",
    "Burning 90s NYC taxi with zebra cloth, empty and dramatic flames...",
    "Speeding 90s NYC taxi filled with popcorn from a broken machine...",
    "Flooded 90s NYC taxi underwater with fish swimming inside...",
    "Woman painting nails in the backseat at night with soft lighting...",
    "Suited man reading newspaper saying 'Don't trust the driver'...",
    "90s taxi stuffed with white doves, woman staring outside...",
    "Men hold mirror in desert reflecting monkey cameraman...",
    "Supermarket workers with mirror reflecting crop fields...",
    "Parrots in jungle holding mirror reflecting penguins...",
    "Rearview mirror reflecting spaceship at a quiet gas station...",
    "Construction worker with mirror showing monks meditating...",
    "Underwater shot, fashion model wearing jellyfish dress...",
    "Paris night, woman in lava lamp dress, homemade VHS look...",
    "Model in iron filing magnetic dress with spiky motion...",
    "Model in flowing bubble biogel dress, cinematic underwater...",
    "Plus-size man in jellyfish dress underwater, fashion shot...",
    "Model with LED boots showing moving light patterns...",
    "Octopus dress wrapping model's body, surreal atmosphere...",
    "Kinetic morphing dress changing with every movement..."
]

# Cargamos el modelo de traducción (gratis)
@st.cache_resource
def load_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

translator = load_translator()

# Entrada del usuario
idea = st.text_area("✍️ Escribe tu idea (en cualquier idioma):")

if st.button("🚀 Generar prompt optimizado"):
    if not idea.strip():
        st.warning("Por favor, escribe una idea primero.")
    else:
        # Paso 1: Traducimos la idea al inglés
        try:
            translation = translator(idea, max_length=512)[0]['translation_text']
        except Exception as e:
            st.error("❌ Ocurrió un error al traducir. Intenta con una idea más corta.")
            st.stop()

        # Paso 2: Seleccionamos un ejemplo aleatorio y lo combinamos
        ejemplo = random.choice(prompt_ejemplos)
        prompt_final = f"{translation.strip().capitalize()} Inspired by: {ejemplo}"

        # Mostrar resultados
        st.success("✅ Prompt optimizado generado:")
        st.text_area("Prompt final:", value=prompt_final, height=300)

