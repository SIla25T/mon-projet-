"""classe Metas"""
from dataclasses import dataclass
from .classe_abstraite import ElementOntologie

@dataclass
class Metas(ElementOntologie):
    """classe pour les metas données des fichiers json"""
    title: str
    author: str
    year: int
    source: str
    language: str
    domain: str

    @classmethod
    def fusionner(cls, data_text_1, data_text_2):
        """trouve les conflits et les résoud"""
        # Implémentation du crossover pour fusionner les lieux
        metas_fusionnes = []
        for meta_a in data_text_1:
            metas_fusionnes.append(meta_a)
        for meta_b in data_text_2:
            conflit= False
            for meta_deja_range in metas_fusionnes:
                if meta_b.title != meta_deja_range.title :
                    print(f"fusion en cours : {meta_b.title} n'est pas similaire à {meta_deja_range.title} !")
                    meta_deja_range.title = f"Ontologie résultant de l'union de {meta_deja_range.title} et {meta_b.title}"
                if meta_b.author != meta_deja_range.author :
                    print(f"fusion en cours : {meta_b.author} n'est pas similaire à {meta_deja_range.author} !")
                    meta_deja_range.t = f"{meta_deja_range.author} et {meta_b.author}"
                if meta_b.year != meta_deja_range.year :
                    print(f"fusion en cours : {meta_b.year} n'est pas similaire à {meta_deja_range.year} !")
                    meta_deja_range.year = meta_deja_range.year, meta_b.year
                if meta_b.source != meta_deja_range.source :
                    print(f"fusion en cours : {meta_b.source} n'est pas similaire à {meta_deja_range.source} !")
                    meta_deja_range.source = f"{meta_deja_range.source} et {meta_b.source}"
                if meta_b.language != meta_deja_range.language :
                    print(f"fusion en cours : {meta_b.language} n'est pas similaire à {meta_deja_range.language} !")
                    meta_deja_range.language = f"{meta_deja_range.language} et {meta_b.language}"
                if meta_b.domain != meta_deja_range.domain :
                    print(f"fusion en cours : {meta_b.domain} n'est pas similaire à {meta_deja_range.domain} !")
                    meta_deja_range.domain = f"{meta_deja_range.domain} et {meta_b.domain}"
                    conflit= True
                    break
            if not conflit:
                metas_fusionnes.append(meta_b)
        return metas_fusionnes