- Application de gestion de tournoi d'échecs en local

- Projet entièrement en python

- Système utilisé pour la database : TinyDB

- Pour utiliser cette application il vous faut :
1. Dans Terminal ou CMD vous rendre dans le dossier OC-P4 téléchargé du repository github
2. Créer un environnement de développement dans le repertoire OC-P4 avec la commande suivante : python -m venv venv
3. Installer toutes les librairies indiquées dans le fichier requirements.txt via la commande : pip install -r requirements.txt
4. Lancer le programme via la commande : python main.py

- Pour générer un nouveau rapport flake8 il faut : 
1. Dans Terminal ou CMD nstaller flake8 sur votre votre via la commande : python pip install flake8-html
2. Dans Terminal ou CMD vous rendre dans le dossier OC-P2 téléchargé du repository github
3. Utiliser la commmande : flake8 --format=html --htmldir=flake8_rapport model helpers controller main.py view
