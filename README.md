<p align="center">
    <img src="https://raw.githubusercontent.com/collove/pasteme/295b20a2fc7375661fb123b140ed7089314c193d/.git_components/logo.svg" width="140">
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

#### 3. Create both `./pasteme/local_settings.py` and `.env` files and write the following contents in them.

```shell
$ touch ./pasteme/local_settings.py && touch .env
```

```python
# local_settings.py
DEBUG = True
ALLOWED_HOSTS = []
```

Generate a new Django `SECRET_KEY` using [Djecrety](https://djecrety.ir/) and paste it in the `.env` file in the root path of the project as follows.

```shell
SECRET_KEY=<COPIED SECRET_KEY HERE>
```

#### 4. Finally, migrate the make-ready migrations and start the service.

```shell
$ python manage.py migrate
$ python manage.py runserver
```

Check out http://localhost:8000 for the result!

### Technologies & Services
- __Frameworks and Tools__
  - [Django 4.0.6](https://www.djangoproject.com/) + [DRF](https://www.django-rest-framework.org/)
  - [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- __Infrastructures & Hosting Services__
  - [PythonAnyWhere](https://pythonanywhere.com)
  - [PlanetScale](https://planetscale.com)

### License
PasteMe is being licensed under the [MIT License](https://github.com/collove/pasteme/blob/main/LICENSE).

### Special Thanks to
- [Hashnode](https://hashnode.com/)
- [PlanetScale](https://planetscale.com/)

<a href="https://townhall.hashnode.com/planetscale-hackathon"><img width="190" height="45" src="https://raw.githubusercontent.com/collove/pasteme/main/.git_components/development_badge.png"></a>
