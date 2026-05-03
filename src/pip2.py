"""pipeline qui sert à faire le liens entre les differents fichiers 
(il n'a a pas de déclaration de fonction ou de classe ou de méthode dans ce fichier.)"""
from pathlib import Path
from input import input_text
from sous_classes.characters import Characters

# importation des fichiers jsons => envoie à la fonction input_text
chemin_1 = Path("src/sous_classes/cendrillon.json")
chemin_2 = Path("src/sous_classes/chaperon_rouge.json")
text1 = input_text(chemin_1)
text2 = input_text(chemin_2)

characters_text1 = [Characters(**character) for character in text1['characters']]
characters_text2 = [Characters(**character) for character in text2['characters']]
character_fusion = characters_text1.fusionner(characters_text2)

print(characters_text1)
print(characters_text2.id)
print(character_fusion)
