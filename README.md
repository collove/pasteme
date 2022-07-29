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

#### 3. Get the `SECRET_KEY`.
Create a `.env` file in the root path of project (next to the `manage.py`) and generate a `SECRET_KEY` token using [Djecrety](https://djecrety.ir/) and paste it in the file.

```sh
# .env
SECRET_KEY=<TOKEN>
```

#### 4. PlanetScale database configuration. (Optional)
PasteMe uses the traditional SQLite database by default. However, you can override the `DATABASES` configuration by writing to the `pasteme/local_settings.py`. Follow the steps to connect your PasteMe to PlanetScale services.

- Create a new account on https://planetscale.com for FREE
- Create a new database
- Get the credentials (By pressing the "Connect" button in the dashboard)

Add the following configurations to the end of the `.env` file based on the recieved credentials.

```sh
# .env
...
DB_DATABASE=<Name>
DB_USER=<User>
DB_PASSWORD=<Password>
DB_HOST=<Host>
DB_PORT=3306
MYSQL_ATTR_SSL_CA=/etc/ssl/certs/ca-certificates.crt
```

Create a new file named `pasteme/local_settings.py` (next to `settings.py`) and add the following PlanetScale datatbase configurations.

```python
# local_settings.py

DATABASES = {
   'default': {
     'ENGINE': 'django_psdb_engine', # <-- already available as a 3rd party
     'NAME': config('DB_DATABASE'),
     'HOST': config('DB_HOST'),
     'PORT': config('DB_PORT'),
     'USER': config('DB_USER'),
     'PASSWORD': config('DB_PASSWORD'),
     'OPTIONS': {'ssl': {'ca': config('MYSQL_ATTR_SSL_CA')}, 'charset': 'utf8mb4'}
   }
}
```

#### 5. Finally, migrate the make-ready migrations and start the service.
```shell
$ python manage.py migrate
$ python manage.py runserver
```

#### 6. Docker (Optional)
You can have a PasteMe instance running in a Docker container on your machine. Make sure you have both `docker` and `docker-compose` installed on your system and run the following command.

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
