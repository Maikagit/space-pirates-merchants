# Plan de Développement - Space Pirates and Merchants

Ce document détaille l'organisation du développement du jeu "Space Pirates and Merchants" en plusieurs phases et journées de travail distinctes.

## Structure globale

Le code sera réorganisé selon la structure de modules suivante :

```
space-pirates-merchants/
│
├── assets/                  # Ressources du jeu
│   ├── images/              # Images et sprites
│   ├── sounds/              # Effets sonores
│   └── music/               # Musiques
│
├── src/                     # Code source du jeu
│   ├── entities/            # Classes pour les entités du jeu
│   │   ├── ship.py          # Classe de base pour les vaisseaux
│   │   ├── player.py        # Vaisseau du joueur
│   │   ├── npc.py           # Vaisseaux non-joueurs
│   │   ├── projectile.py    # Projectiles et armes
│   │   ├── celestial.py     # Corps célestes (planètes, étoiles)
│   │   └── station.py       # Stations spatiales
│   │
│   ├── game/                # Logique principale du jeu
│   │   ├── game.py          # Classe principale du jeu
│   │   ├── state.py         # Gestionnaire d'états du jeu
│   │   ├── universe.py      # Génération procédurale de l'univers
│   │   ├── physics.py       # Moteur physique
│   │   ├── economy.py       # Système économique
│   │   └── combat.py        # Système de combat
│   │
│   ├── ui/                  # Interfaces utilisateur
│   │   ├── menu.py          # Menus du jeu
│   │   ├── hud.py           # Interface en jeu
│   │   ├── dialog.py        # Boîtes de dialogue
│   │   └── screen.py        # Écrans de transition
│   │
│   └── utils/               # Fonctions et classes utilitaires
│       ├── resource.py      # Gestionnaire de ressources (images, sons)
│       ├── config.py        # Configuration du jeu
│       ├── save.py          # Sauvegarde/chargement
│       └── math.py          # Fonctions mathématiques utiles
│
├── main.py                  # Point d'entrée du jeu
└── requirements.txt         # Dépendances Python
```

## Plan de développement jour par jour

### Jour 1 : Structure de base et refactoring
- Déplacer le code existant dans une structure modulaire
- Créer les classes de base pour les entités
- Implémenter le système de rotation du vaisseau
- Mettre en place la structure principale du jeu

### Jour 2 : Système de physique et de contrôle
- Améliorer la physique des vaisseaux (inertie, freinage)
- Implémenter la rotation visuelle des vaisseaux pendant les déplacements
- Créer un système de caméra qui suit le joueur
- Ajouter la génération d'étoiles en arrière-plan

### Jour 3 : Armes et projectiles
- Implémenter un système de projectiles
- Créer différents types d'armes
- Ajouter des effets visuels pour les tirs
- Intégrer la détection de collision pour les projectiles

### Jour 4 : Corps célestes et environnement
- Créer des classes pour représenter les planètes et étoiles
- Mettre en place la génération procédurale de systèmes solaires
- Implémenter la navigation entre les systèmes
- Ajouter des champs d'astéroïdes et obstacles

### Jour 5 : Stations spatiales et interface de commerce
- Développer des stations spatiales interactives
- Créer un système économique de base
- Implémenter l'interface d'achat/vente de marchandises
- Ajouter la fluctuation des prix entre les stations

### Jour 6 : IA et PNJ
- Créer des comportements pour les vaisseaux non-joueurs
- Implémenter différents types de PNJ (marchands, pirates, patrouilles)
- Ajouter un système de réputation de base
- Intégrer des interactions avec les PNJ

### Jour 7 : Interface utilisateur et menus
- Développer les menus principaux du jeu
- Améliorer l'interface en jeu (HUD)
- Créer des écrans de dialogue
- Ajouter des tutoriels de base

### Jour 8 : Système d'audio
- Intégrer le son du moteur du vaisseau
- Ajouter des effets sonores pour les armes et collisions
- Implémenter une musique de fond dynamique
- Créer un gestionnaire audio complet

### Jour 9 : Sauvegarde et chargement
- Mettre en place un système de sauvegarde
- Permettre de sauvegarder l'état du jeu
- Implémenter la persistance du monde
- Créer une interface de chargement de parties sauvegardées

### Jour 10 : Améliorations et équilibre
- Affiner les mécaniques de jeu
- Équilibrer l'économie
- Améliorer les visuels
- Optimiser les performances

## Ordre des tâches prioritaires

1. Réorganiser le code dans une structure modulaire
2. Implémenter la rotation visuelle des vaisseaux pendant les déplacements
3. Ajouter les sons du moteur
4. Créer un système de projectiles fonctionnel
5. Développer l'environnement spatial (planètes, étoiles)

## Notes techniques

- Utiliser pygame.transform.rotate() pour la rotation des sprites
- Implémenter un système de particules pour les effets visuels du moteur
- Utiliser opensimplex pour la génération procédurale de l'univers
- Garder une séparation claire entre la logique et l'affichage
- Implémenter un gestionnaire d'états pour faciliter les transitions entre les différentes parties du jeu