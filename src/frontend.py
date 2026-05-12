import streamlit as st
from inputs import import_json

st.title("Projet Python combinaison")

left, middle, right = st.columns(3, vertical_alignment="bottom")

with left:
    fichier_texte1 = st.file_uploader(
        "Texte 1",
        type=["json"],
        key="texte1"
    )

with right:
    fichier_texte2 = st.file_uploader(
        "Texte 2",
        type=["json"],
        key="texte2"
    )

texte1 = import_json(fichier_texte1)
texte2 = import_json(fichier_texte2)    

left, middle, right = st.columns(3, vertical_alignment="bottom")

middle.radio(
    "Stratégie de fusion",
    ["Union", "Intersection", "Priorité"]
)

left, middle, right = st.columns(3, vertical_alignment="bottom")
middle.button("Combiner", use_container_width=True)
middle.button("Exporter", use_container_width=True)