"""pipeline qui sert à faire le liens entre les differents fichiers 
(il n'a a pas de déclaration de fonction ou de classe ou de méthode dans ce fichier.)"""
from pathlib import Path
from input import input_text
from sous_classes.characters import Characters
from sous_classes.locations import Locations
from sous_classes.events import Events
from sous_classes.relations import Relations
from sous_classes.rules import Rules

# importation des fichiers jsons => envoie à la fonction input_text
chemin_1 = Path("src/sous_classes/cendrillon.json")
chemin_2 = Path("src/sous_classes/chaperon_rouge.json")
text1 = input_text(chemin_1)
text2 = input_text(chemin_2)

# instanciation et fusion des personnages
characters_text1 = [Characters(**character) for character in text1['characters']]
characters_text2 = [Characters(**character) for character in text2['characters']]
character_fusion = Characters.fusionner(characters_text1, characters_text2)
print(character_fusion)

# instanciation et fusion des lieux
locations_text1 = [Locations(**location) for location in text1['locations']]
locations_text2 = [Locations(**location) for location in text2['locations']]
location_fusion = Locations.fusionner(locations_text1, locations_text2)
print(location_fusion)

# instanciation et fusion des evenements
events_text1 = [Events(**event) for event in text1['events']]
events_text2 = [Events(**event) for event in text2['events']]
event_fusion = Locations.fusionner(locations_text1, locations_text2)
print(event_fusion)

# instanciation et fusion des relations
relations_text1 = [Relations(**relation) for relation in text1['relations']]
relations_text2 = [Relations(**relation) for relation in text2['relations']]
relations_fusions = Relations.fusionner(relations_text1, relations_text2)

# instanciation et fusion des regles
rules_text1 = [Rules(**rule) for rule in text1['rules']]
rules_text2 = [Rules(**rule) for rule in text2['rules']]
rules_fusions = Rules.fusionner(rules_text1, rules_text2)
