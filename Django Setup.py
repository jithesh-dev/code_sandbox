#  Install Pip
sudo easy_install pip

# Pip view all packages

pip3 freeze

# Create Virtual Env

python3 -m venv ./venv

# Venv activate
source ./venv/bin/activate

# Venv Deactivate
deactivte

# venv > install Django
pip install django

#create project
django-admin startproject leadmanager

# Start pages app
python manage.py startapp pages

# run server
python manage.py runserver

#make migrartions
python manage.py makemigrations leads #where leads is foldername

#migrate
python manage.py migrate 

#shorten terminal path
PROMPT_DIRTRIM=3
