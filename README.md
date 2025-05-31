# Kanban Board 

### Tech stack
- HTML
- Bootstrap CSS
- Django
- Sqlite3
- Selenium for testing

### Prerequisites
- Installed Django
- Installed selenium
- Installed crispy forms. Reference the file login.html under the hometouser app to see the setup

### Set Up

#### Activate the virtual environment
- `python3 -m venv <desired_name>`
- `ls`
- `cd` into the one folder that should result from `ls`
- `source ./bin/activate` to activate the environment always work within this when making any changes to the project to install packages, etc.

### Managing the database
- Accessing the database via `python manage.py shell`
- Then any models or forms made access via `User.objects.all()` (user is already created)
- Tip: To quickly add a new user `User.objects.create_user(username='guest', password='secret')` replace guest and secret with your own variables.

### Features so far
1) Full user authentication and database storage.
2) Passwords are hashed correctly for secure login.
3) Routing between pages.
4) HTML and CSS are connected.
5) Selenium is connected.

### In progress...

