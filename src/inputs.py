"""lieu d'extraction des fichiers jsons"""
import json
from pathlib import Path

def import_json(uploaded_file):
    """
    Fonction d'importation de fichiers JSON.
    """
    if uploaded_file is None:
        return None
    try:
        return json.load(uploaded_file)
    except json.JSONDecodeError:
        return None

def input_text (path):
    """fonction d'extraction des données des fichiers jsons"""
    text = Path(path)
    with open(text, "r", encoding="utf-8") as f:
        text = json.load(f)
    return text
