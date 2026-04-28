"""lieu d'extraction des fichiers jsons"""
import json
from pathlib import Path

def input_text (path_1, path_2):
    """fonction d'extraction des données des fichiers jsons"""
    text1 = Path(path_1)
    text2 = Path(path_2)
    with open(text1, "r", encoding="utf-8") as f:
        text1 = json.load(f)
    with open(text2, "r", encoding="utf-8") as f:
        text2 = json.load(f)
    return text1, text2
