# Utilisez une image de base Python avec Debian
FROM python:3.9-slim-buster

# Installez les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiez votre application Flask dans le conteneur
COPY . /app
WORKDIR /app

# Installez les dépendances Python
RUN pip install -r requirements.txt

# Exposez le port sur lequel votre application Flask s'exécute
EXPOSE 5000

# Démarrez votre application Flask
CMD ["python", "app.py"]