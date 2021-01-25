# Task-events  
# Motivations 
it is a Django task for events using: 
- Django. 
- Django Rest Framework. 
- Django filters for filtering on fields. 
## Getting Started
### Pre-requisites and Local Development
Developers using this project should already have Python3, Django and pipenv installed in their local machines.
#### PIP Dependencies
run this command that create virtual environment and install dependencies. 
```bash
pipenv install
``` 
to activate the virtual env run this. 
```bash
pipenv shell
```   
To run the Migrations, execute this commands in the root folder:  
```bash
python manage.py makemigrations
```
```bash 
python manage.py migrate
```   
To run the server, execute this command in the root folder:
```bash 
python manage.py runserver
``` 
To run the tests, execute this command in the root folder:  
```bash
python manage.py test
```
