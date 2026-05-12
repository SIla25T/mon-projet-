"""fonction output"""
import json

def output(characters, locations, events, relations, rules, fichier_sortie):
    """fonction de concatenation des résultats et de création du fiechier json de sortie"""
    tout_ensemble = f"{characters} {locations} {events} {relations} {rules}"
    with open(fichier_sortie, "w", encoding="utf-8") as f:
        json.dump(tout_ensemble, f, ensure_ascii=False, indent=4)
