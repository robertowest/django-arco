# django-arco



# Crea nuevo proyecto
```
$ cd ../Python/
$ mkdir -p arco/static
$ cd arco/
$ touch .gitattributes
$ touch .gitignore
$ touch Procfile
$ touch requirements.txt
```

# Creamos nuestro archivo .gitignore

En mi caso, deseo ignorar **venv**, **python** y **visualstudiocode**

Siga este enlace para generar el archivo [.gitignore](https://www.gitignore.io/?templates=venv,python,visualstudiocode)



# Creamos y conectamos a nuestro environment
```
$ python3 -m venv .env
$ source .env/bin/activate
```

# Creamos nuestro proyecto django 3
```
$ django-admin startproject config .
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

# Creamos nuestro proyecto heroku
```
$ heroku login
$ heroku create arcotuc --buildpack heroku/python
```

<!---
# Creamos una base de datos 

La db se llamará **hobby-dev**, este nombre es obligatorio en la versión gratuita
```
$ heroku addons:create heroku-postgresql:hobby-dev --app arcotuc
$ heroku run python manage.py makemigrations --settings=config.settings.heroku
$ heroku run python manage.py migrate --settings=config.settings.heroku
$ heroku run python manage.py createsuperuser --settings=config.settings.heroku
```
Credenciales de la db
Host        ec2-3-91-112-166.compute-1.amazonaws.com
Database    dfgmkdpc6aihlp
User        sbgsdoavionrbs
Port        5432
Password    74fe50b36187169c0b273ec770b3c90ab38d6cba558bc553ade0030c0c5fad1b
URI         postgres://sbgsdoavionrbs:74fe50b36187169c0b273ec770b3c90ab38d6cba558bc553ade0030c0c5fad1b@ec2-3-91-112-166.compute-1.amazonaws.com:5432/dfgmkdpc6aihlp
Heroku CLI  heroku pg:psql postgresql-cubed-68520 --app arcotuc
-->


# Creamos repositorio git y preparamos primera carga
```
$ git init
$ git add --all .
$ git commit -m "primera subida a Heroku"
```

### Enlazamos el proyecto heroku a git
```
$ heroku git:remote -a arcotuc
```

### Realizamos nuestro primer checkin
previamente, desabilitamos collectstatic
```
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ git push heroku master
```


### Siguientes modificaciones ...
```
$ git add --all .
$ git commit -m "modificaciones en Heroku"
$ git push [heroku master]
```


# Conectarse a la base de datos Heroku desde psql
```
$ heroku pg:psql

psql>\dt
psql>select * from homepage_entries;
psql>\q
```


# Modificaciones al proyecto Django

Realizamos las modificaciones necesarias para que nuestro proyecto django funcione correctamente en **Heroku**


# deploy-django-heroku

Modificaciones a nuestro [settings](https://codigofacilito.com/articulos/deploy-django-heroku)
