import os
from pipeline import PipelineFusion

def main():
    chemin_1= "data/cendrillon_ontology.json"
    chemin_2= "data/chaperon_rouge_ontology.json"
    chemin_sortie= "data/ontologie_fusionnee.json"

    if not os.path.exists(chemin_1) or not os.path.exists(chemin_2):
        print("Erreur : Les fichiers JSON n'ont pas été trouvés dans le dossier 'data/'.")
        return

pipeline = PipelineFusion()
pipeline.executer(chemin_1, chemin_2, chemin_sortie)


if __name__ == "__main__":
    main()
