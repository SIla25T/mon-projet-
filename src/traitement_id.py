"""fonction traiter id"""
import re
import ast

def traiter_id(text, nb_text):
    """permet de rajouter l'origine du texte des id pour qu'elles ne soit plus similaires 
    et n'interfèrent pas entre elles"""
    text_a_modifier = f"{text}"
    regex = r"\1_"+nb_text
    regex1 = r"(\w+_\d+)"
    text_modifier_id = re.sub(regex1, regex, text_a_modifier)
    text_dict = ast.literal_eval(text_modifier_id)
    return text_dict

def traiter_id_text(text, id_modifier):
    """permet de rajouter l'origine du texte des id pour qu'elles ne soit plus similaires 
    et n'interfèrent pas entre elles"""
    text_a_modifier = f"{text}"
    id_traiter = id_modifier
    regex1 = r"(\w+_\d+)_\d"
    regex2 = r"\1"
    id_minimal = re.sub(regex1, regex2, id_traiter)
    regex3 = f"{id_minimal}_"+r"\d"
    regex4 = f"{id_minimal}_0"
    text_modifier_id = re.sub(regex3, regex4, text_a_modifier)
    text_dict = ast.literal_eval(text_modifier_id)
    return text_dict

def traiter_id_classe(classe_id):
    """permet de modifier l'id des classes"""
    id_modifier = f"{classe_id}"
    regex1 = r"(\w+_\d+)_\d"
    regex2 = r"\1"
    id_minimal = re.sub(regex1, regex2, id_modifier)
    id_final = f"{id_minimal}_0"
    return id_final
