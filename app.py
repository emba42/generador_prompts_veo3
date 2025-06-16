import streamlit as st
import random

# Lista de prompts de ejemplo de VEO 3 (simplificados)
prompt_ejemplos = [
    "In the back seat of a 90s taxi...",
    "Burning 90s NYC taxi with zebra cloth...",
    "Empty 90s taxi filled with popcorn...",
    "Underwater 90s taxi with fish...",
    "Woman painting nails in speeding taxi...",
    "Man reading 'Don't trust the driver'...",
    "White doves in 90s taxi at night...",
    "Men hold mirror in desert reflecting monkey cameraman...",
    "Supermarket mirror shows crops...",
    "Parrots holding mirror showing penguins...",
    "Rearview mirror reflects spaceship at gas station...",
    "Mirror shows meditating monks on scaffolding...",
    "High fashion jellyfish dress underwater...",
    "Lava lamp dress walking in Paris...",
    "Iron filing dress with magnetic waves...",
    "Morphing bubble biogel dress...",
    "Plus size jellyfish dress underwater...",
    "LED boots in white minimalist space...",
    "Dress made of octopuses gripping model...",
    "Dress morphs with motion in market..."
]

st.title("🧠 Generador de Prompts para VEO 3")
st.write("Este bot mejora tus ideas para que sean entendidas por la IA de VEO 3.")

idea = st.text_area("✍️ Escribe aquí tu idea para el prompt (en cualquier idioma):")

if st.button("🚀 Generar prompt optimizado"):
    if idea.strip() == "":
        st.warning("Por favor, escribe una idea primero.")
    else:
        # Simulamos traducción + mejora usando ejemplos
        ejemplo = random.choice(prompt_ejemplos)
        prompt_final = f"Optimized prompt based on your idea:\n\n{ejemplo}"
        st.success("✅ Prompt optimizado generado:")
        st.text_area("Prompt final:", value=prompt_final, height=300)
