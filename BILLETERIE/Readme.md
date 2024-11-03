# Exercice : Billetterie du Métro de Fukuoka

## 📜 Contexte

Le métro municipal de Fukuoka, situé au sud-ouest du Japon, comprend trois lignes :
- **Airport Line** (orange),
- **Hakozaki Line** (bleu),
- **Nanakuma Line** (vert).

Ce projet se concentre exclusivement sur la **Airport Line**. En cas de panne des machines de billetterie automatiques, il est demandé de développer une interface de secours fonctionnant dans un terminal, permettant au personnel de gare d’émettre des billets de manière rapide et simple. Le programme doit calculer le tarif total en fonction des informations fournies par le client (nombre de billets, type de tarif, distance à parcourir).

## 🏁 Objectifs

L’objectif principal est de développer un programme en Python, capable de :

1. **Poser des questions au client** :
   - Nombre de billets adulte,
   - Nombre de billets à tarif réduit (enfants, personnes handicapées),
   - Choix de la station de départ et de la station d'arrivée, avec une liste numérotée pour minimiser les erreurs de saisie.

2. **Calculer le coût total** :
   - Le tarif est déterminé selon la **zone tarifaire** correspondant à la distance parcourue, divisée en quatre zones :
     - **Zone 1** : 0-3 km, 210 yen (plein tarif), 110 yen (tarif réduit),
     - **Zone 2** : 3.1-7 km, 260 yen (plein tarif), 130 yen (tarif réduit),
     - **Zone 3** : 7.1-11 km, 300 yen (plein tarif), 150 yen (tarif réduit),
     - **Zone 4** : 11.1-15 km, 340 yen (plein tarif), 170 yen (tarif réduit).
   - La tarification se base sur le tarif plein, auquel peut s'ajouter un tarif réduit en fonction du nombre de billets demandés.

3. **Afficher les détails du billet** :
   - Le programme affiche le récapitulatif complet du trajet, y compris les stations sélectionnées, la distance parcourue, la zone tarifaire, le prix total et la voie du train à emprunter :
     - **Voie 1** : Meinohama > Fukuokakuko,
     - **Voie 2** : Fukuokakuko > Meinohama.

4. **Gérer les erreurs de saisie** :
   - En cas d'erreur dans la saisie (numéro de station incorrect, nombre de billets non valide, etc.), le programme demande à l’utilisateur de saisir à nouveau une valeur correcte.

## ⭕ Conditions de Réussite

- L’utilisateur peut acheter des billets à tarif plein et/ou réduit.
- Le programme fonctionne dans les deux sens de la ligne (Meinohama > Fukuokakuko ou inversement).
- Le détail de l'itinéraire (distance, zone tarifaire, coût) est affiché au client.
- Le programme vérifie et gère les erreurs de saisie pour assurer une expérience fluide.
