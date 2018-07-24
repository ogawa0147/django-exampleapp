```
$ django-admin.py startproject app
```

```
$ docker-compose up -d
$ docker-compose up --build
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py createsuperuser
$ docker-compose run web python manage.py startapp cms
$ docker-compose run web python manage.py makemigrations cms
$ docker-compose run web python manage.py migrate cms
$ docker-compose run web python manage.py startapp api
$ docker-compose run web python manage.py makemigrations api
$ docker-compose run web python manage.py migrate api
```


```
$ brew info python3
$ python -V
$ brew install python3
$ sudo easy_install pip
$ sudo pip install virtualenv virtualenvwrapper --ignore-installed six
```
```
$ mkdir ~/.virtualenvs
```
```
$ export WORKON_HOME=$HOME/.virtualenvs
$ source ~/.zshrc
```
```
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv --no-site-package --python /usr/local/bin/python3 env1
```
```
$ workon env1
```
```
$ deactivate
$ rmvirtualenv env1
```
```
$ workon env1
$ pip install django==2.0.1
```
```
$ pip freeze -l
```
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

```
$ python manage.py makemigrations cms
$ python manage.py migrate cms
```

```
$ python manage.py startapp api
```

```
$ pip install -r requirements.txt
```