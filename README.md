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
Got to `127.0.0.1:8000/` to the analytics or `127.0.0.1:8000/admin/` to access to admin panel
