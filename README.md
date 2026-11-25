<img width="962" height="630" alt="Projet Python drawio" src="https://github.com/user-attachments/assets/ff2b144c-2473-452f-b302-1819caf1d977" />

## Diagramme (Brouillon)
J'ai mis un premier brouillon du diagramme juste pour qu'on puisse jeter un œil et s'en servir de référence. N'hésitez pas à m'envoyer un message si vous voulez modifier!

## 👥 Répartition des tâches

--- 

### Malick — Conception de la Map & Visuels des Terrains
* Gestion des Terrains : Implémentation des différentes classes de Tiles ( `RoadTile`,  `HerbeTile`,  `TerreTile`,  `GlaceTile`,  `VideTile`).
* Design des Circuits : Conception et modélisation de la grille de carte 2D (layouts des circuits).
* Affichage des Sprites : Implémentation initiale du rendu de la carte et du marqueur de direction de la voiture. 

--- 

### Léonard — Implémentation des Blocs & Logique de Course
* Gestion des Blocs Interactifs : Implémentation des mécanismes de blocs sur le circuit (Points de passage / Checkpoints  `C`, Lignes d'arrivée  `L`, Zones de boost  `B`, Blocs de départ  `1` &    `2`).
* Race Coordinator : Logique de comptage des tours, validation des checkpoints et suivi de l'état de la course. 

--- 

### Urin — Architecture MVC, Machine à États & Physique du Véhicule
* Machine à États ( `GameState`) &   IHM : Conception et intégration de la machine à états du jeu ( `MENU` ➔  `CIRCUIT _SELECT` ➔  `RACING`) ainsi que l'interface graphique de sélection des circuits.
* Contrôleur & Entrées : Gestion de la navigation dans les menus, des événements clavier et des commandes du véhicule ( `GameController`,  `InputHandler`).
* Dynamique & Physique de la Voiture : Implémentation de la physique du véhicule (accélération, freinage, inertie, dérapage/drift selon la friction des terrains).
