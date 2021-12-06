# Cahier des charges - VLOBJ

## Introduction

Le but de ce projet est de compiler notre propre langage le **VLOBJ** en fichier **.obj** et **.mtl** lisible par blender.

## Description

L'utilisateur va pouvoir créer une scène blender via le langage VLOBJ qui s'inspire du python. L'utilisateur peut créer des cubes et des pyramides.

### VLOBJ

Voici, les fonctionnalités possibles du langage VLOBJ.

#### Shape

- Création d'un cube avec comme arguments la position (x,y,z), du centre, la taille de la forme et une Color

  ```VLOBJ
  Square(1, 0, 1, 2, 'bleu')
  ```

- Création d'une pyramide avec comme arguments la position (x,y,z), du centre, la taille de la forme et sans couleur se qui fait une forme de couleur blanche

  ```VLOBJ
  Pyramid(3, 2, 3, 4)
  ```

Dès que une forme est créé, elle sera ajouté dans le fichier ".obj".

#### Color

Une couleur peut être créer avec le mot clef **Color**. Les arguments contiennent le nom et les valeurs (r,g,b).

```VLOBJ
Color('bleu',0,0,255) # Couleur bleu
```

#### Boucle

- Les boucles représentées par **^^**

  ```VLOBJ
  x =) 0
  y =) 0
  z =) 0
  i =) 5
  ^^ (i > 0)
   :(
   Square(x+i,y,z,i)
   ):
  ```

#### Random

- Valeurs aléatoires

  ```VLOBJ
  i =) xD(start, stop)
  ```

- Forme aléatoire

  ````VLOBJ
  xS(x,y,z,taille)
  ````

#### Opérateur incrémentation et de décrémentation

  ```VLOBJ
  i+_+ # incrémente de 1 la variable i
  i-_- # Décremente de 2 la variable i
  ```

#### Les tests

```VLOBJ
:/ (taille == 4)
:(
	Square(1, 0, 1, 2, 'bleu')
):else:(
	Square(1, 0, 1, 2, 'red')
):
```

### .obj

Le fichier *.obj* contient la géométrie des formes avec leurs positions et tailles. Blender peut importer un fichier pour ajouter à sa scène les éléments présents dans le document.

- Un sommet est défini de la manière suivante :

  ```obj
  v 1.0 0.0 0.0
  ```

- Une coordonnée de texture est définie de la manière suivante :

  ```obj
  vt 1.0 0.0
  ```

- Une normale est définie de la manière suivante :

  ```obj
  vn 0.0 1.0 0.0
  ```

- Chaque face est ensuite définie par un ensemble d'indices faisant référence aux coordonnées des points, de texture et des normales définies précédemment : 

  ```obj
  f v1/vt1/vn1 v2/vt2/vn2 v3/vt3/vn3
  ```


### .mtl

Le fichier .mtl contient les informations sur les matériaux utilisés pour colorier les formes dur fichier .obj. Donc à chaque "Color()", un nouvau metériel est créer dans le fichier ".mtl".

```mtl
newmtl blue # nom du materiel
Ns 100
Ka 1.000000 1.000000 1.000000
Kd 0.000000 0.005973 0.800000 # L'unique paramètre à changer, pour modifier la couleur
Ks 0.500000 0.500000 0.500000
Ke 0.000000 0.000000 0.000000
Ni 1.450000
d 1.000000
illum 2
```
