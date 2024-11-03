# Jeu d'Aventure Textuel - Consignes

## 📜 Situation

Un manga très en vogue souhaite être adapté en jeu vidéo par son comité de production. Afin de valider les idées de gameplay, le ton des dialogues et pour récapituler rapidement tout ce que l'on pourra faire dans le jeu, le studio a décidé de créer un prototype sous forme de jeu d'aventure textuel qui se joue dans le terminal.

Dans le scénario du manga, le lycée A.U. vise à former les meilleurs héros de sa région. Son nom vient de la prononciation des lettres "AU" en anglais, qui ressemble à la prononciation de "héros" en japonais ("eiyuu"). Toute ressemblance avec d'autres lycées est purement fortuite...

L'action du jeu se déroule donc dans ce lycée. Après avoir rempli un questionnaire au début du jeu pour créer le personnage principal, le joueur peut se déplacer librement dans différents endroits de l'école, chacun proposant diverses actions.

## 🏁 Objectifs

Les fondations du jeu sont posées, mais il reste encore beaucoup à faire : créer des lieux pour y accéder et y réaliser des actions, notamment la salle d'entraînement où les joueurs peuvent s'engager dans des combats basiques.

Cette fois-ci, le joueur devra lire et manipuler des variables en fonction de ses actions. L'utilisateur peut entrer seulement deux types d'entrées : le nom d'un autre **lieu** pour se déplacer ou le nom d'une **action**.

Bien sûr, au-delà d'avoir un code fonctionnel, l'objectif est de s'amuser un peu. N'hésitez pas à ajouter votre touche personnelle à travers les dialogues, les actions réalisables, ou même en introduisant de nouveaux lieux ou fonctionnalités. Si une idée que vous tenez absolument à réaliser vous semble trop difficile, n'hésitez pas à demander conseil.

### 🞲 Gestion des Objets

Le jeu commence avec un smartphone comme **objet clé** (qui n'a pas de fonction spéciale) et un **inventaire** vide.

Les objets clés n'ayant qu'une seule instance, nous utilisons une liste pour les stocker.

L'inventaire, en revanche, permet de garder plusieurs quantités d'un même objet ; ainsi, nous utilisons un dictionnaire pour suivre la quantité de chaque objet.

Les deux types d'objets peuvent être utilisés tout au long du jeu. Les joueurs peuvent récupérer des objets en fonction des lieux visités ou des actions réalisées.

### 🞲 Les Lieux

Pour être complet, le jeu doit inclure au minimum les lieux suivants :

* Hall d'entrée (RDC)
* Couloir du RDC
* Classe 1-A (RDC)
* Couloir du 1er étage
* Cafétéria (1er étage)
* Salle d'entraînement (1er étage)

Les joueurs ne peuvent se déplacer d'un lieu à un autre que s'ils sont à proximité (par exemple, du couloir du 1er étage à la classe 1-A). L'accès à la salle d'entraînement nécessite un passe.

### 🞲 Les Actions

Une action est un verbe à l'infinitif. Peu importe le lieu, l'action `observer` doit être incluse, ce qui affiche simplement une description de l'endroit dans le terminal. Par exemple, dans le hall, cela affichera : "Vous êtes dans un hall..."

**Hall** :
* Action `quitter` => quitte simplement le script.

**Cafétéria** : 
* Action `manger` => Après avoir demandé le plat souhaité, le joueur gagne 10 PV (points de vie). Chaque plat n'a que 2 exemplaires en stock, donc il faut **soustraire** un plat du stock à chaque utilisation et **annuler** l'action si un plat demandé n'est plus en stock.

**Classe 1-A** :
* Action `demander` => Permet de recevoir le passe (un objet clé) de la part du professeur, ce qui permet d'entrer dans la salle d'entraînement du 1er étage.
* Action `montrer` => Permet de montrer au professeur le nombre de badges que l'on a en main ; si le joueur possède trois badges gagnés lors de combats contre le mannequin d'entraînement, le jeu est réussi et le script s'arrête.

**Salle d'entraînement** :
* Action `combattre` => Lance une **boucle** qui continue jusqu'à ce que les PV du mannequin d'entraînement atteignent zéro. Au début d'un combat, le mannequin commence toujours avec 50 PV. Dans cette boucle, l'utilisateur peut choisir d'`attaquer` ou de `fuir` (ce qui **annule** la boucle). Une attaque réduit les PV du mannequin de 15, et le mannequin riposte en réduisant les PV du joueur de 10. Si le joueur perd tous ses PV, le script s'arrête. En revanche, si le mannequin est vaincu, le joueur gagne un **badge** dans son inventaire comme preuve de réussite.

### 🞲 Plan de l'Établissement

**RDC**

**1er étage**

## ⭕ Conditions de Réussite

* ✔️ Le joueur peut créer son personnage et voir un récapitulatif de celui-ci.
* ✔️ Le joueur peut `observer` dans chaque lieu.
* ✔️ Le joueur peut `manger` au maximum 2 exemplaires de chaque plat à la cafétéria, ce qui augmente ses points de vie.
* ✔️ Le joueur peut `demander` le passe au professeur dans la classe 1-A ; s'il l'a déjà, il peut lui montrer ses badges.
* ✔️ Le joueur peut `combattre` contre un mannequin dans la salle d'entraînement.
* ✔️ Le jeu s'arrête sur un game over si les points de vie du joueur tombent à zéro lors d'un combat.
* ✔️ Le jeu s'arrête sur une réussite si le joueur montre 3 badges au professeur dans la classe 1-A.
