# Simulation physique 2D

## Présentation

Ce projet est une application de simulation physique en deux dimensions développée en Python avec Tkinter.

L'objectif est de simuler le comportement de différents objets dans un environnement physique simple, en prenant en compte leurs propriétés, leurs déplacements et leurs interactions. L'application propose une interface graphique permettant de visualiser la simulation en temps réel, de contrôler son exécution et de modifier les propriétés des objets.

Le projet est conçu pour être évolutif : son architecture permet d'ajouter progressivement de nouveaux types d'objets, de nouvelles propriétés physiques et des mécanismes d'interaction plus avancés.

## Aperçu de l'application

Voici quelques démonstration illustrant le fonctionnement de l'application et les possibilités offertes par son interface graphique.

<video controls src="video_exemple.mp4" title="Title"></video>

<video controls src="video_exemple2.mp4" title="Title"></video>

## Fonctionnalités actuelles

### Simulation physique

* Mise à jour de la position et de la vitesse des objets au cours du temps.
* Prise en compte de l'accélération et de la gravité
* Gestion des rebonds avec un coefficient de restitution.
* Détection des collisions entre les balles et les rectangles.
* Gestion des collisions avec les limites de l'environnement.

### Interface graphique

* Affichage des objets dans un environnement 2D.
* Démarrage et mise en pause de la simulation.
* Réinitialisation de la simulation.
* Sélection d'un objet avec la souris.
* Consultation et modification des propriétés de l'objet sélectionné.

### Objets physiques

Le projet comporte actuellement deux types d'objets :

* **Ball** : un objet circulaire possédant un rayon
* **Rectangle** : un objet rectangulaire possédant une largeur, une hauteur

Ces objets héritent d'une classe de base `Body`, qui regroupe les propriétés et les comportements communs aux objets physiques.

## Technologies utilisées

* **Python** : langage principal du projet.
* **Tkinter** : création de l'interface graphique.
* **Programmation orientée objet** : organisation du code autour de classes et de responsabilités distinctes.
* **unittest** : écriture et exécution des tests automatisés.

## Architecture du projet

```text
newSimulation/
├── main.py
├── physics/
│   ├── __init__.py
│   ├── body.py
│   ├── ball.py
│   ├── rectangle.py
│   └── world.py
├── ui/
│   ├── __init__.py
│   ├── app.py
│   ├── renderer.py
│   └── renderers/
│       ├── ball_renderer.py
│       └── rectangle_renderer.py
├── tests/
│   ├── test_ball.py
│   ├── test_world.py
│   └── test_rectangle.py
└── README.md
```

### Organisation des modules

* **`main.py`** : point d'entrée de l'application.
* **`physics/body.py`** : classe de base des objets physiques. Elle centralise les propriétés communes, comme la position, la vitesse, l'accélération, la gravité et la masse.
* **`physics/ball.py`** : définition des objet circulaire.
* **`physics/rectangle.py`** : définition des objets rectangulaires.
* **`physics/world.py`** : gestion du monde physique, des objets présents, du temps et des collisions.
* **`ui/app.py`** : interface graphique et interactions avec l'utilisateur.
* **`ui/renderer.py`** : coordination de l'affichage des objets.
* **`ui/renderers/`** : rendu graphique propre à chaque type d'objet.
* **`tests/`** : tests automatisés des classes et des comportements physiques.

Cette séparation permet de faire évoluer la physique sans devoir réécrire l'interface graphique, et inversement.

## Installation

### Prérequis

* Python 3 installé.
* Tkinter disponible dans l'environnement Python.

Tkinter est généralement inclus avec Python. Sur certaines distributions Linux, il peut nécessiter une installation séparée.

### Récupération du projet

Clonez le dépôt, puis placez-vous dans le répertoire du projet :

```bash
git clone https://github.com/GoutteDeau/SimulationEnvironnementPhysique.git
cd SimulationEnvironnementPhysique
```

### Lancement

Exécutez le point d'entrée :

```bash
python main.py
```

## Tests

Les tests automatisés permettent de vérifier le comportement des objets physiques et du monde de simulation.

Pour lancer les tests depuis la racine du projet :

```bash
python -m unittest discover -s tests
```

## Pistes d'évolution

Le projet constitue une base pour explorer progressivement de nouveaux concepts de programmation et de mécanique. (Nouveaux concepts qui sont en cours d'implémentation)

### 1. Ajouter de nouveaux objets

L'architecture orientée objet permet d'envisager de nouveaux types d'objets, par exemple :

* **Triangle** : objet polygonal avec détection de collisions adaptée.
* **Polygone** : forme définie par une liste de sommets.
* **Particule** : objet simplifié destiné à simuler des effets collectifs.
* **Ressort** : élément reliant deux objets et exerçant une force selon son allongement.

Chaque nouveau type pourrait disposer de ses propres propriétés physiques et de son propre moteur de rendu.

### 2. Ajouter de nouveaux paramètres physiques

Plusieurs paramètres pourraient enrichir les simulations :

* **Frottement** : ralentissement des objets en contact ou en mouvement.
* **Résistance de l'air** : diminution progressive de la vitesse.
* **Force appliquée** : action d'une force extérieure sur un objet.
* **Charge électrique** : base possible pour explorer les interactions électrostatiques.

L'ajout de paramètres ne consiste pas uniquement à stocker de nouvelles valeurs : il faut également définir comment elles influencent les équations de mouvement et les interactions entre les objets.

### 3. Améliorer le moteur physique

Le moteur pourrait évoluer vers une simulation plus complète avec :

* Des collisions entre tous les types d'objets.
* Une meilleure gestion de la pénétration entre les objets.
* Un pas de simulation fixe pour améliorer la stabilité numérique.
* Transférer le code en C++ pour une meilleur efficacité.

### 4. Enrichir l'interface graphique

L'interface pourrait proposer :

* L'ajout et la suppression d'objets depuis l'application. (en cours)
* La création d'objets par clic ou par glisser-déposer. (en cours)
* Des commandes pour modifier la vitesse de la simulation.
* L'affichage des vecteurs vitesse, accélération et force.
* Des couleurs ou des informations visuelles indiquant les propriétés des objets.

### 5. Ajouter des outils d'analyse

Pour aller plus loin, il serait possible d'ajouter :

* Le suivi de l'énergie cinétique et de l'énergie potentielle.
* L'affichage de la quantité de mouvement.
* Des graphiques représentant la position et la vitesse au cours du temps.
* L'enregistrement et le chargement de configurations.
* L'export des données de simulation pour les analyser séparément.

### 6. Renforcer les tests

Les tests pourraient être étendus pour couvrir :

* Les collisions entre différentes paires d'objets.
* Les cas limites, notamment les objets superposés.
* La conservation de la quantité de mouvement lors de collisions élastiques.
* La cohérence de l'évolution des vitesses et des positions.
* Le comportement du moteur avec un grand nombre d'objets.

## Objectifs du projet

Ce projet me permet de travailler sur plusieurs aspects du développement logiciel :

* La programmation orientée objet et l'héritage.
* La séparation entre logique métier, moteur physique et interface graphique.
* La modélisation de phénomènes physiques.
* La détection et la résolution de collisions.
* La conception d'une architecture extensible.
* Les tests automatisés et la validation des comportements.
* L'amélioration progressive d'un projet existant.

## Conclusion

Cette simulation est un projet évolutif dont l'objectif est de construire progressivement un moteur physique 2D modulaire. Les prochaines étapes pourront porter sur l'amélioration des collisions, l'ajout de nouveaux objets et l'enrichissement des outils de contrôle et d'analyse.

Le développement se fait par étapes, avec une attention particulière portée à la compréhension des mécanismes physiques et à la qualité de l'architecture logicielle.
