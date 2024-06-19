dev:
	py manage.py runserver localhost:8000

test:
	py manage.py test

prod:
	py manage.py runserver 0.0.0.0:8000