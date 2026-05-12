"""pipeline qui sert à faire le liens entre les differents fichiers 
(il n'a a pas de déclaration de fonction ou de classe ou de méthode dans ce fichier.)"""
from pathlib import Path
from inputs import input_text
from traitement_id import traiter_id
from sous_classes.metas import Metas
from sous_classes.characters import Characters
from sous_classes.locations import Locations
from sous_classes.events import Events
from sous_classes.relations import Relations
from sous_classes.rules import Rules
from output import output

# impoter fichier depuis le front-end

# importation des fichiers jsons => envoie à la fonction input_text
chemin_1 = Path("src/sous_classes/cendrillon.json")
chemin_2 = Path("src/sous_classes/chaperon_rouge.json")
entree_1 = input_text(chemin_1)
entree_2 = input_text(chemin_2)

# traitement de l'id pour pas qu'elles ne se confondent pas
text1 = traiter_id(entree_1, "1")
text2 = traiter_id(entree_2, "2")


# instanciation des métas données
metas_text1 = [Metas(**text1["meta"])]
metas_text2 = [Metas(**text2['meta'])]
meta_fusion = Metas.fusionner(metas_text1, metas_text2)

# instanciation et fusion des personnages
characters_text1 = [Characters(**character) for character in text1['characters']]
characters_text2 = [Characters(**character) for character in text2['characters']]
character_fusionner = Characters.fusionner(characters_text1, characters_text2, text1, text2)
character_fusion = character_fusionner[0]
text1_traiter_char = character_fusionner[1]
text2_traiter_char = character_fusionner[2]
print(character_fusion)

# instanciation et fusion des lieux
locations_text1 = [Locations(**location) for location in text1_traiter_char['locations']]
locations_text2 = [Locations(**location) for location in text2_traiter_char['locations']]
location_fusionner = Locations.fusionner(locations_text1, locations_text2, text1_traiter_char, text2_traiter_char)
location_fusion = location_fusionner[0]
text1_traiter_loc = location_fusionner[1]
text2_traiter_loc = location_fusionner[2]
print(location_fusion)

# instanciation et fusion des evenements
events_text1 = [Events(**event) for event in text1_traiter_loc['events']]
events_text2 = [Events(**event) for event in text2_traiter_loc['events']]
event_fusion = Events.fusionner(events_text1, events_text2)
print(event_fusion)

# instanciation et fusion des relations
relations_text1 = [Relations(**relation) for relation in text1_traiter_loc['relations']]
relations_text2 = [Relations(**relation) for relation in text2_traiter_char['relations']]
relations_fusions = Relations.fusionner(relations_text1, relations_text2)
print(relations_fusions)

# instanciation et fusion des regles
rules_text1 = [Rules(**rule) for rule in text1_traiter_loc['rules']]
rules_text2 = [Rules(**rule) for rule in text2_traiter_loc['rules']]
rules_fusions = Rules.fusionner(rules_text1, rules_text2)
print(rules_fusions)

# exporter le tout dans un fichier json
path_output = Path("src/sous_classes/output.json")
output(character_fusion, location_fusion, event_fusion, relations_fusions, rules_fusions, path_output)
