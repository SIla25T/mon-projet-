"""lieu d'extraction des fichiers jsons"""
import json
from pathlib import Path
json_cendrillon = Path("src/sous_classes/cendrillon.json")
json_chaperon_rouge = Path("src/sous_classes/chaperon_rouge.json")

with open(json_cendrillon, "r", encoding="utf-8") as f:
    data_text1 = json.load(f)

with open(json_chaperon_rouge, "r", encoding="utf-8") as f:
    data_text2 = json.load(f)
