#!/bin/bash

echo -e "\e[1m\e[34mBienvenue sur le script d'installation des Galeries Ponthé"
echo -e "Ce script est destiné aux distributions Ubuntu-like. \e[31mUn compte GitHub est nécessaire.\e[0m"
read -p "Adresse mail du compte GitHub : " mail
read -p "Prénom Nom : " name
echo -e "\e[1m\e[34mConfiguration de git...\e[0m"

git config --global user.name $name
git config --global user.email $mail
git config --global http.postBuffer 524288000
git config --global push.default simple
git config --global push.rebase true
git config --global credential.helper 'cache --timeout=86400'

### INSTALL ###
echo -e "\e[1m\e[34mInstallation des dépendances...\e[0m"
sudo -E apt-get update
sudo -E apt-get install -y python3-pip apt-transport-https

echo -e "\e[1m\e[34mInstallation de la base de données\e[0m"
sudo apt-get install mysql-server
echo "CREATE DATABASE ponthe;CREATE USER 'ponthe'@'localhost' IDENTIFIED BY ''; GRANT ALL ON ponthe.* TO 'ponthe'@'localhost'" | mysql -u root -p

cd web/app/instance/keys
openssl genrsa -out jwtRS256-private.pem 2048 && openssl rsa -in jwtRS256-private.pem -pubout -out jwtRS256-public.pem
cd ../..

echo -e "\e[1m\e[34mInstallation de l'environnement python\e[0m"
pip3 install virtualenvwrapper
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3;" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/virtenvs;" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh;" >> ~/.bashrc
mkvirtualenv ponthe
workon ponthe
pip install --editable .
export FLASK_APP=ponthe
flask db upgrade
flask load-data

mkdir -p instance/static/uploads && mkdir -p instance/static/thumbs && mkdir -p instance/tmp/uploads

echo -e "\e[1m\e[34mInstallation de la base de données\e[0m"
sudo apt-get install mysql-server
echo "CREATE DATABASE ponthe;CREATE USER 'ponthe'@'localhost' IDENTIFIED BY ''; GRANT ALL ON ponthe.* TO 'ponthe'@'localhost'" | mysql -u root -p

echo -e "\e[1m\e[34mAjout de dev-ponthe.enpc.org au fichier hosts\e[0m"

echo "127.0.0.1 dev-ponthe.enpc.org" | sudo tee -a /etc/hosts
