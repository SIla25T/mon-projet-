import streamlit as st

st.title("Projet Python combinaison")

left, middle, right = st.columns(3, vertical_alignment="bottom")

left.button("Texte 1", use_container_width=True)
right.button("Texte 2", use_container_width=True)

left, middle, right = st.columns(3, vertical_alignment="bottom")
middle.button("Combiner", use_container_width=True)
middle.button("Exporter", use_container_width=True)