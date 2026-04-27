"""lieu d'extraction des fichiers jsons"""
import json
from fichiers_json import cendrillon, chaperon_rouge

with open("cendrillon.json", "r", encoding="utf-8") as f:
    data_text1 = json.load(f)

with open("chaperon_rouge.json", "r", encoding="utf-8") as f:
    data_text2 = json.load(f)