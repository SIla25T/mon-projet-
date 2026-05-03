"""pipeline qui sert à faire le liens entre les differents fichiers 
(il n'a a pas de déclaration de fonction ou de classe ou de méthode dans ce fichier.)"""
import json
from typing import List
from pathlib import Path
from sous_classes.characters import Characters 
from src.strategy import CrossoverStrategy
from input import input_text

# importation des fichiers jsons => envoie à la fonction input_text
chemin_1 = Path("src/sous_classes/cendrillon.json")
chemin_2 = Path("src/sous_classes/chaperon_rouge.json")
text1 = input_text(chemin_1)
text2 = input_text(chemin_2)



class OntologieLoader: # existe déjà dans input.py
    """ 
    Classe responsable de la lecture des fichiers json
    """
    def lire_fichier(self, chemin_fichier):
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            data= json.load(f)
            return data

class OntologieFactory: # c'est exactement ce que font les classes Characters, Locations, Events, Relations et Rules dans leurs fichiers respectifs
    """ 
    Classe responsable de la création des objets à partir des données lues
    """
    def creer_ontologie(self, data_raw: dict):
        # extraire liste du fichier json pour ensuite créer les objets
        pass
    def creer_personnage(self, liste_json: List[dict]) -> List[Personnage]:
        # créer les personnages à partir de la liste du fichier json
        mes_personnages = []
        # parcourir la liste du json et créer les objets personnages
        for item in liste_json:
            nouveau_perso = Personnage(
                id_element=item['id'],
                nom=item['name'],
                role=item['role'],
                traits=item['traits',[]]
            )
            mes_personnages.append(nouveau_perso)
        return mes_personnages

class PipelineFusion:
    """ 
    Classe responsable de la fusion des ontologies 
    """
    def __init__(self):
        # Initialiser les composants nécessaires pour la fusion
        self.loader = OntologieLoader()
        self.factory = OntologieFactory()
        self.FusionStrategy = CrossoverStrategy()

    def executer(self, chemin_a: str, chemin_b: str, chemin_sortie: str):
        print("Début de la fusion des ontologies")

        # Lire les fichiers d'entrée
        data_a = self.loader.lire_fichier(chemin_a)
        data_b = self.loader.lire_fichier(chemin_b)
        # Créer les objets à partir des données lues
        persos_a = self.factory.creer_personnages(data_a["characters"])
        persos_b = self.factory.creer_personnages(data_b["characters"])

        # Fusionner les personnages
        print("Fusion des personnages en cours...")
        liste_finale = self.strategie_fusion.fusionner_personnages(persos_a, persos_b)

        # Sauvegarder le résultat dans un nouveau fichier JSON
        liste_dictionnaires = []
        for perso in liste_finale:
            liste_dictionnaires.append(perso.exporter())

        resultat_final = {
            "meta": {
                "title": "Ontologie Fusionnée (Crossover)",
                "description": "Fusion de Cendrillon et du Chaperon Rouge"
            },
            "characters": liste_dictionnaires
        }
        with open(chemin_sortie, 'w', encoding='utf-8') as f_sortie:
            json.dump(resultat_final, f_sortie, ensure_ascii=False, indent=4)
        print(f"Sauvegarde terminée dans {chemin_sortie} !")
        return chemin_sortie
