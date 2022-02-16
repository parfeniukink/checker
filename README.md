# Setup the project


## Mandatory steps
1. Install Docker



## Preparing
```bash
# Create a .env file based on .env.example
copy .env.example .env

# Run project in docker
docker-compose up -d
```


## Create user for admin
```bash
docker-compose exec django python manage.py createsuperuser

>>> admin
>>> admin@admin.com
>>> admin
>>> admin
>>> y
Enter
```


## Usage
Go to the `127.0.0.1:8000/` for analytics

or to the`127.0.0.1:8000/admin/` for getting the admin panel access
