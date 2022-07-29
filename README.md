<p align="center">
    <img src="https://raw.githubusercontent.com/collove/pasteme/development/.git_components/dark.svg#gh-dark-mode-only" width="140">
    <img src="https://raw.githubusercontent.com/collove/pasteme/development/.git_components/light.svg#gh-light-mode-only" width="140">
    <h4 align="center">PasteMe - RESTful Pastebin Service</h4>
</p><br>

> [Check out the article describing the development and deployment steps behind this service on Hashnode](https://imsadra.me/pasteme-paste-codes-from-your-terminal).

A RESTful pastebin service made for [@hashnode](https://github.com/hashnode) purposes powered by the [@PlanetScale](https://github.com/planetscale) MySQL DBaaS. There is a [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) template shining behind the [DRF](https://www.django-rest-framework.org/) components to show the information but the focuse is on the RESTful service where you can create snippets from almost all platforms!

### Paste to PasteMe
Use the [`pasteme-cli`](https://pypi.org/project/pasteme-cli/) package and start pasting. Once you paste your content, you'll be able to share it with others.

```shell
$ pip install pasteme-cli
...
$ pasteme --help
```

### Service Installation

#### 1. To setup the webservice locally, clone the repository first.
```shell
$ git clone https://github.com/collove/pasteme.git && cd ./pasteme
```

#### 2. Create a new `venv` and install the dependencies.
```shell
$ virtualenv venv && source venv/bin/activate
$ pip install -r requirements.txt
```

#### 3. PlanetScale database configuration.
> In spite PasteMe prefers to connect to a PlanetScale database, you can simply use whatever database you want as your backend database.

In order to use PlanetScale databases as your backend database,

- Create a new account on https://planetscale.com
- Create a new database
- Get the credentials (By pressing the "Connect" button in the dashboard)

and add the following variables in a `.env` file in the root path of the project.

```sh
SECRET_KEY=<Token>

DB_DATABASE=<Database Name>
DB_USER=<Database Username>
DB_PASSWORD=<Database Password>
DB_HOST=<Database Hostname>
DB_PORT=3306
MYSQL_ATTR_SSL_CA=/etc/ssl/certs/ca-certificates.crt
```

Generate a new `SECRET_KEY` token using [Djecrety](https://djecrety.ir/) and paste it in front of `SECRET_KEY`. Value other variables based on the crendentials you recieved from the PlanetScale dashboard.

#### 4. SQLite database configuration.
If you want to use a sqlite database for your service, create `pasteme/.local_settings.py` (next to `settings.py`) file and write the following database configuration into it.

```python
# local_settings.py
from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }
}
```

#### 5. Finally, migrate the make-ready migrations and start the service.
```shell
$ python manage.py migrate
$ python manage.py runserver
```

#### 6. Docker (Optional)
You can have a PasteMe running in a Docker container on your machine. Make sure you have both `docker` and `docker-compose` installed on your system and run the following command.

```sh
$ docker-compose up -d --build
```

Check out http://localhost:8000 for the result!

### Tech Stack
- __Frameworks and Tools__
  - [Django 4.0.6](https://www.djangoproject.com/) + [DRF](https://www.django-rest-framework.org/)
  - [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- __Infrastructures & Hosting Services__
  - [PythonAnywhere](https://pythonanywhere.com)
  - [PlanetScale](https://planetscale.com)

### License
PasteMe is being licensed under the [MIT License](https://github.com/collove/pasteme/blob/main/LICENSE).

### Special Thanks to
- [Hashnode](https://hashnode.com/)
- [PlanetScale](https://planetscale.com/)

<img width="240" height="60" src="https://raw.githubusercontent.com/collove/pasteme/ee9db4cc136c004ef67d93e2942fbc17d990b6e7/.git_components/badge_light.svg#gh-light-mode-only">

<img width="240" height="60" src="https://raw.githubusercontent.com/collove/pasteme/ee9db4cc136c004ef67d93e2942fbc17d990b6e7/.git_components/badge_dark.svg#gh-dark-mode-only">
