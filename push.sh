#!/bin/bash
git add .
# git reset push.sh
git commit -m "modificado en casa"
git push -u origin master
git push heroku master

# heroku run python manage.py makemigrations
# heroku run python manage.py migrate
# heroku run python manage.py createsuperuser
