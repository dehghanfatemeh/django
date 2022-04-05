
## Steps I took to launch this program

#### Create a virtual environment, install Django
```python
virtualenv -p python3 venv

source venv/bin/activate

pip install django

```




#### I run the default Django apps on the migrate database
```python
python manage.py runserver

python manage.py makemigrations

python manage.py migrate

```




#### Build the first project
```python
django-admin startproject `name project` .
```




#### Build the first app
```python 
python manage.py startapp `name app`
```




#### Django admin panel
```python
python manage.py createsuperuser
```