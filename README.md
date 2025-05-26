# Intro

(Ce repository est destiné au projet de fin de module ESGI pour le module "Conteneurs et Devops".)


# Chicago Art Explorer

Une web application Flask qui met en valeur les œuvres d'art de l'Art Institute of Chicago en utilisant leur API publique.

## Fonctionnalités

- Explorez les œuvres d'art de l'Art Institute of Chicago
- Affichez des informations détaillées sur chaque œuvre
- Recherchez des œuvres spécifiques
- Design réactif avec Bootstrap
- Support de la pagination

## Technologies Utilisées

- Python 3.7+
- Flask
- Requests
- pytest (pour les tests)
- waitress (déploiement en production)

## Lancement en local (Développement)

1. Clonez le dépôt :
```bash
git clone <repository-url>
cd <repository-name>
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # sur Windows, use: venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Lancez l'application Flask en mode développement :
```bash
python app.py
```

L'application sera disponible à l'adresse :
```
http://localhost:5000
```

## Déploiement en production

### En utilisant Waitress

Pour déployer l'application en production, nous recommandons d'utiliser Waitress, un serveur WSGI pour les applications Python.

```bash
python wsgi.py
```

L'application sera disponible à l'adresse :
```
http://localhost:8000
```

### En utilisant Docker

*<ins> A vous de créer le ou les Dockerfile qui vous permettront de déployer l'application en production, ainsi que de lancer les tests...</ins>*


## Exécution des Tests

L'application inclut des tests unitaires pour vérifier le bon fonctionnement des fonctionnalités principales.
```bash
python -m pytest
```

Pour exécuter les tests avec couverture de code, utilisez `coverage` :
```bash
coverage run -m pytest
coverage report
```

Pour générer un rapport de couverture de code (rapport au format HTML) :
```bash
coverage html
```


## API Documentation

Pour plus d'informations sur l'API de l'Art Institute of Chicago, consultez la documentation officielle :
https://api.artic.edu/docs/
