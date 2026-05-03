"""lieu d'extraction des fichiers jsons"""
import json
from pathlib import Path

def input_text (path):
    """fonction d'extraction des données des fichiers jsons"""
    text = Path(path)
    with open(text, "r", encoding="utf-8") as f:
        text = json.load(f)
    return text
