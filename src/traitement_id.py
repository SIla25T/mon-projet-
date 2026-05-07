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
