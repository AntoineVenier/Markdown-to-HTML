import argparse 

arguments_passes=argparse.ArgumentParser()#On stocke dans arguments_passes les arguments passes au programme
#Message d aide pour chaque options
arguments_passes.add_argument("i",help="Dossier contenant les fichiers Markdown")
arguments_passes.add_argument("o",help="Dossier contenant les fichiers HTML convetis a partir de fichiers Markdown")
arguments_passes.parse_args()#on affiche les arguments passes au programme