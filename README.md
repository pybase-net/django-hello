# Django Hello World

In this project, we'll go through all of django basic components.

## Hello World App

- Quiz: Question and Answers
- Quiz Game: User play quiz game

We'll make a project management app:

## Main features

- User: CRUD
- Auth: Login, Reset Password
- Project: CRUD
- Task: CRUD

### Manage Project App

```sh
python manage.py startapp projectmanagement
python manage.py makemigrations projectmanagement
python manage.py migrate
```

```sh
python manage.py createsuperuser
```

#### Postgresql

```sh
pip install psycopg2-binary
```

#### ENV

```sh
pip install python-dotenv
```

#### Models

- https://www.dothedev.com/blog/django-created-at-updated-at-auto-fields/
- https://www.hacksoft.io/blog/timestamps-in-django-exploring-auto-now-auto-now-add-and-default

#### Authentication

- [Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)

## References

- [Django Tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- [Django styleguide](https://github.com/HackSoftware/Django-Styleguide-Example)
- [Django Fields](https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices)
- [Django Meta](https://docs.djangoproject.com/en/5.0/ref/models/options/)
- [Django Rest Framework](https://www.django-rest-framework.org/api-guide/viewsets/#example_3)