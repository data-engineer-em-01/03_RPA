# RPA projet

## API Plateform

### Implémentation de l'API de gestion des factures

Dans ce TP, vous allez mettre en œuvre une API de gestion des factures pour une plateforme de gestion administrative. 

## Objectifs

- Mettre en place une API RESTful pour la gestion des factures.
- Implémenter différentes fonctionnalités pour récupérer des factures en fonction de différents critères tels que l'année, la date, le nom du formateur, le nom de l'école, etc.
- Tester l'API à l'aide d'outils tels que Postman ou curl.

1. Mise en place de l'environnement

Utilisez API platform

1. Modèle de données

Utilisez le fichier qui se trouve dans le dossier Data : [factures](./Data/factures.json)

1. Implémentation des endpoints

Implémentez les endpoints suivants pour récupérer les factures :

   1. `GET /factures` : Récupère toutes les factures.
   2. `GET /factures/annee/<annee>` : Récupère les factures pour une année spécifiée.
   3. `GET /factures/date/<date>` : Récupère les factures pour une date spécifiée.
   4. `GET /factures/formateur/<nom_formateur>` : Récupère les factures pour un formateur spécifié.
   5. `GET /factures/ecole/<nom_ecole>` : Récupère les factures pour une école spécifiée.
   6. `GET /factures/date/<date>/formateur/<nom_formateur>` : Récupère les factures pour une date et un formateur spécifiés.
   7. `GET /factures/date/<date>/ecole/<nom_ecole>` : Récupère les factures pour une date et une école spécifiées.
   8. `GET /factures/date/<date>/formateur/<nom_formateur>/ecole/<nom_ecole>` : Récupère les factures pour une date, un formateur et une école spécifiés.


1. Documentation

- Créez une documentation décrivant chaque endpoint, les paramètres acceptés et les réponses attendues.

## Livrables

- Code source de l'API.
- Documentation de l'API.
- Rapport décrivant les étapes de développement, les problèmes rencontrés et les solutions adoptées.