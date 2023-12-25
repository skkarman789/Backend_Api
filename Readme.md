## :star2: About the Project
 ```This Django project serves as a rule engine for monitoring and generating alerts based on vehicle data. It includes scheduled jobs for periodic data updates and alert generation. The project uses Django REST Framework for API endpoints and interacts with a SQLite3 database.```

## :toolbox: Getting Started



Clone the project

```bash
git clone https://github.com/skkarman789/Backend_Api.git
```

Navigate to the project directory:
```bash
cd enview
```
Create a virtual environment
```bash
pip install venv 
python -m venv venv 
venv/Scripts/Activate
```
Install project dependencies
```bash
pip install -r requirements.txt
```
Run migrations to set up the database
```bash
python manage.py makemigrations 
python manage.py migrate
```
Create a superuser for administrative tasks
```bash
python manage.py createsuperuser
```


### :running: Run Locally
Start the development server
```bash
python manage.py runserver
```

🚀 API Endpoints
``````bash
• GET /alerts/{alert_id}
➡️ Retrieve a single alert by ID.
    
• GET /alerts/
➡️Retrieve all alerts.

• POST /events/
➡️Receive driving events from the IoT device.

• GET /getevent/
➡️Retrieve all alerts.
```````
Happy Coding! 🚀
