# M1-kalah

## Description
#### Jeu de kalah codé en Python avec la bibliothèque PyGame
Le kalah est un jeu à 2 joueurs où le but est d'obtenir plus de pions dans son kalah que son adversaire.  

## Règles
Le kalah d'un joueur est la case située à sa droite, à l'extrémité du plateau, et représente son score.  
Au début de la partie, les kalahs sont vides et les autres cases contiennent 3 pions chacune.  
À tour de rôle, les joueurs prennent les pions d'une case et les sèment une par une sur les cases suivantes dans le sens anti-horaire.  
Si le dernier pion semé est dans le kalah du joueur, il rejoue.  
Si le dernier pion semé est dans une case vide du côté du joueur, il récupère le dernier pion ainsi que tous les pions de la case opposée et les place dans son kalah.  
La partie se termine lorsqu'un joueur n'a plus de pions de son côté. Le joueur ayant des pions restants de son côté les récupère et les place dans son kalah.  
Le joueur ayant le plus de pions dans son kalah à la fin de la partie gagne.  

## Contrôles
Au démarrage:  
- Choisir la difficulté du jeu entre 1 et 4 (modifie le nombre de pions au début du jeu, difficulté 1 par défaut)  
- Entrer le nom des joueurs (Joueur 1 et Joueur 2 par défaut en laissant vide)  

Cliquer sur une case bleue pour jouer un coup  
R : Recommencer (le joueur qui commence change)  
S : Sauvergarder une partie  
L : Charger une partie  
M : Mode de jeu (2 joueurs, ou joueur vs IA)
