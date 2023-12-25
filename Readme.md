## :star2: About the Project
 ```This Django project serves as a rule engine for monitoring and generating alerts based on vehicle data. It includes scheduled jobs for periodic data updates and alert generation. The project uses Django REST Framework for API endpoints and interacts with a SQLite3 database.```

## :toolbox: Getting Started



1. Clone the project

```bash
git clone https://github.com/skkarman789/Backend_Api.git
```

2. Navigate to the project directory
```bash
cd enview
```
3. Create a virtual environment
```bash
pip install venv 
python -m venv venv 
venv/Scripts/Activate
```
4. Install project dependencies
```bash
pip install -r requirements.txt
```
5. Run migrations to set up the database
```bash
python manage.py makemigrations 
python manage.py migrate
```
6. Create a superuser for administrative tasks
```bash
python manage.py createsuperuser
```


### :running: Run Locally
<b>Start the development server</b>
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
