release: python3 manage.py makemigrations
release: python3 manage.py sqlmigrate users 0001
release: python3 manage.py migrate
web: gunicorn ibbms1.wsgi --preload --log-file –