import argparse 
from pathlib import Path

arguments_passes=argparse.ArgumentParser()#On stocke dans arguments_passes les arguments passes au programme
#Message d aide pour chaque options (les arguments ne peuvent etre que des chaines de caracteres)
arguments_passes.add_argument("i",type=str,help="Dossier contenant les fichiers Markdown")
arguments_passes.add_argument("o",type=str,help="Dossier contenant les fichiers HTML convetis a partir de fichiers Markdown")
args=arguments_passes.parse_args()#on affiche les arguments passes au programme
print("Le dossier contenant les fichiers Mardown:",args.i.split("/")[-2])
print("Le dossier contenant les fichiers HTML:",args.o.split("/")[-2])

#lister tous les fichiers markdown du dossier passe en argument en utilisant la methode glob de pathlib
chemin_fichiers_markdown=Path(args.i)
fichiers_markdown=list(chemin_fichiers_markdown.glob('**/*.md'))
print(fichiers_markdown)

#afficher le contenu des fichiers markdown
with fichiers_markdown[0].open() as mon_fichier:
    for ligne in mon_fichier:
        print(ligne)
