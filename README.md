# Convertisseur Markdown vers HTML

 GenerateurSiteStatique.py est un programme python sous licence **BSD3** qui prend comme paramètres:

    -i: Le dossier comportant tous les fichiers Markdown à convertir en html.

    -o: Le dossier où seront stockés tous les fichiers markdown converties en HTML.

    -t: Le fichier HTML qui servira de modèle pour chaque page html generée.

###  **exemple:**

![](/images_readme/parametres.png)

Il est aussi possible d'utiliser l'option -h ou --help pour avoir des informations sur les arguments du programme.

![](/images_readme/help1.png)

### **resultat:**

![](/images_readme/help.png)

## Convertion du Markdown en HTML

Pour la conversion du Mardown en HTML j'ai utilisé le module markdown2

```python
import markdown2
```

Pour chaque ligne qui se trouve dans un fichier markdown je l'ai convertie en HTML avec le code suivant:

```python
for ligne in mon_fichier_md:
    markdown2.markdown(ligne)
```

## Exemple de page HTML generée par le programme

![](/images_readme/exemple.png)

NB : Vous pouvez tester le programme en utilisant les fichiers markdown qui se trouvent dans le dossier Fichiers_Markdown.