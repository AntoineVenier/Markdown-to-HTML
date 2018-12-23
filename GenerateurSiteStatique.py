import argparse 

arguments_passes=argparse.ArgumentParser()#On stocke dans arguments_passes les arguments passes au programme
#Message d aide pour chaque options (les arguments ne peuvent etre que des chaines de caracteres)
arguments_passes.add_argument("i",type=str,help="Dossier contenant les fichiers Markdown")
arguments_passes.add_argument("o",type=str,help="Dossier contenant les fichiers HTML convetis a partir de fichiers Markdown")
args=arguments_passes.parse_args()#on affiche les arguments passes au programme
print("Le dossier contenant les fichiers Mardown:",args.i)
print("Le dossier contenant les fichiers HTML:",args.o)
