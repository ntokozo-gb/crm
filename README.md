# Create python virtualenv
-$ https://virtualenv.pypa.io/en/stable/userguide/#usage

# Install requirements
-$ pip install -r requirements.txt

# Creating a superuser
-$ python manage.py createsuperuser
- This is the user you will use to login to the app

# Make migrations and migrate
-$ python manage.py makemigrations
-$ python manage.py migrate

# Run the server
-$ python manage.py runserver
- Browse to http://localhost:8000 and login
