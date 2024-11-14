# Dungeon Master

## Astin LAURENS et Maxence POLLOZEC
## EPSI B3 ASRBD

## Fichiers
#### Le fichier DM.py est Dungeon Master en console de commande codé en un seul fichier
#### Le ZIP DMC est ce même Dungeon Master cependant scindé en deux fichiers différents, main.py et data.py 

## Règles

#### Roguelike où vous allez concrètement traverser 20 salles générées aléatoirement. On commence avec 1 PV
#### Les salles sont soit vides ou pleines.
* Une salle vide est un passage sans encombre pour accéder à la salle suivante
* Une salle pleine veut dire un combat contre un ennemie, le combat se fait sur un jet de dé 1D6, pour faire simple, le combat est perdu si le résultat se situe entre 1 et 3 et remporté si le résultat se situe entre 4 et 6
#### Cependant, si lors d'un combat vous faites un 6 avec votre jet de dé, vous faites un Succès Critique, qui vous donne une vie supplémentaire

#### Par contre, si vous effectuez un 1 avec votre jet de dé, vous faites un Échec Critique, qui met fin à votre aventure, quelque soit le nombre de vies que vous possédez

#### Le but du jeu est de finir le donjon et terminer les 20 pièces en restant en vie, bonne chance !

## Fonctionnalités

#### Tout d'abord, nous avons deux versions à présenter pour notre rendu, une première qui se fait en console de commande et une autre en interface graphique

#### Abordons en premier lieu les fonctionnalités communes que nous avons en plus de celles demandées dans l'énoncé : 
* Cheminement effectué étape par étape par l'utilisateur 
* Personnalisation et immersion poussée -> 12 ennemies différents avec des description différentes correspondantes et des répliques de victoire ou défaite personnalisés en fonction de l'ennemi combattu -> effectué via une classe ennemie
* Il y a également des répliques différentes en fonction de si vous mourrez ou si vous perdez juste un PV tout en restant en vie, sortant in extremis du combat
* Il y a également plusieurs descriptions de pièces vides, illustrant différentes atmosphères
* Interactivité et utilisation de time sleep/delay pour des pauses et améliorer l'immersion pour profiter du jeu
* Indicateur de progression ( Salle x/20)
* Séparateur visuel des salles 

#### Pour ce qui concerne la version graphique, voici les spécificités :
* Effet de fade pour faire une transition entre deux pièces
* Sprites représentant le héros, l'ennemi, le donjon, le coeur, le dé et l'écran de Game Over
* Affichage dans un premier temps de la description de l'ennemi, suivi du jet de dé avec l'outcome (self.victoire ou self.defaite qui détaillera l'ennemi et ce qu'il se passe)
* Disparition du sprite de l'ennemi si ce dernier est vaincu au combat pour améliorer l'immersion

## Axes d'amélioration

#### Voici une liste des différents éléments que nous pouvons ajouter à notre projet :
* Du son 
* Des sprites différents pour les 12 ennemies différents 
* Des poses de combat/repos/marche pour notre protagoniste
* Des animations (combat, lancer de dé, marche)
* Des environnements de donjon/pièces différents
* Un système de sauvegarde
* Des succès
* Un système de score avec la capacité de terminer son aventure prématurement si l'on ne veut pas risquer la mort
* Des marchands lors de la génération de pièces aléatoires qui permettrait d'acheter de la vie et des relances de dés
* Des pièces sans combat avec du loot, dont certains piégés
* Un écran " You Win" un peu à l'image de celui pour le Game Over (Nous ne l'avons pas mis car il est très peu probable de gagner)
* Utiliser des sprites libres de droits, produits par nos soins ou bien commissionnés 
