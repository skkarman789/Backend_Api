## :toolbox: Getting Started

### :gear: Installation

Clone the project

```bash
https://github.com/skkarman789/Backend_Api.git
```

Navigate to the project directory:
```bash
cd enview
```
Create a virtual environment:
```bash
pip install venv python -m venv venv venv/Scripts/Activate
```
Install project dependencies:
```bash
pip install -r requirements.txt
```
Run migrations to set up the database:
```bash
python manage.py makemigrations python manage.py migrate
```
Create a superuser for administrative tasks:
```bash
python manage.py createsuperuser
```


### :running: Run Locally
Start the development server:
```bash
python manage.py runserver
```