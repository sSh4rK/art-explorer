# Étape 1 : choisir l'image de base Python
FROM python:3.8-slim

# Étape 2 : définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : copier tous les fichiers du projet dans l'image
COPY . .

# Étape 4 : installer les dépendances depuis requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Étape 5 : indiquer la variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Étape 6 : exposer le port 5000
EXPOSE 5000

# Étape 7 : commande de démarrage de l'application
CMD ["flask", "run"]

