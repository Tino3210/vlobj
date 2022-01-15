# VLOBJ - Projet compilateur

Ce projet est un compilateur python qui permet de compiler le langage VLOBJ en deux fichiers *.obj* et *.mtl*. Le but est de pouvoir créé des objets 3D (cube et pyramide) de choisir leur position, la taille et leur couleur. Après la compilation, les deux fichiers de sortie peuvent être importés dans un logiciel de modélisation 3D comme Blender.

# Guide utilisateur - VLOBJ

## Prérequis

Avant de pouvoir commencer ce guide utilisateur. Veuillez vous assurer que vous avez bien installé toutes les recommandations ci-dessous. Si vous ne savez pas comment programmer avec le langage VLOBJ renseignez-vous dans le rapport.

### Installation

**Python**

Avant de pouvoir commencer ce guide. Il faut installer python et les modules PLY et pydot.
> Version utilisée de Python 3.9

**Environnement 3D**

Le meilleur logiciel pour le rendu 3D est Blender, car il offre le support de la gestion de couleur lors de l'importation d'un **.obj** avec le fichier **.mtl** associé. Mais si vous ne voulez pas installer Blender la visionneuse 3D de Windows fera l'affaire (sans les couleurs).

## Guide

### Clonage du projet

Il est nécessaire au préalable de cloner le projet qui se trouve sur GitHub.

```bash
# HTTPS
git clone https://github.com/Tino3210/vlobj.git
```

```bash
# SSH
git clone git@github.com:Tino3210/vlobj.git
```

### Compilation

Vous pouvez compiler votre fichier **.vlobj** avec la commande : 

> Exécuter a la racine du projet

```
user> python .\compilateurVLOBJ.py .\exemple\shapes.vlobj
```

Cela vous créer deux fichiers **.obj** (les objets) et **.mtl** (les couleurs).

### Importation

**Blender**

Ouvrir blender et aller dans l'onglet **Fichier > Import > Wavefront(.obj)**. Cela peut prendre quelques secondes s’il y a trop d'objets comme dans les des captures d'écran dans le dossier **"capture"**.

![](https://i.imgur.com/Hygflg4m.png)

**Visionneuse 3D Windows**

Ouvrir la visionneuse Windows et aller dans l'onglet **Fichier > Ouvrir**.

![](https://i.imgur.com/ZLnrWEo.png)
