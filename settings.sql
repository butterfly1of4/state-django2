CREATE DATABASE usacapitals;
CREATE USER usacapitals_user WITH PASSWORD 'usacapitals';
GRANT ALL PRIVILEGES ON DATABASE usacapitals TO usacapitals_user;

--instructions:

-- if you already have an usacapitals database run:
--DROP DATABASE usacapitals;
--DROP USER usacapitals_user;

--Then, to create usacapitals database in psql run inside top level api directory:
--psql -U postgres -f settings.sql

--In your virtual environment (pipenv shell) translate the models into the schema for our database, run:
--python3 manage.py makemigrations
--python3 manage.py migrate

--To seed database still inside virtual environment, run:
--python3 manage.py loaddata usacapitals.json

--to view database in localhost:8000/admin create superuser:
--python3 manage.py createsuperuser

--to run the server:
--python3 manage.py runserver

--API!!!!!!

--to view as api with crud use:
--localhost:8000/projects 
--localhost:8000/services
--localhost:8000/members
--localhost:8000/contacts
--localhost:8000/volunteers
--localhost:8000/new_projects
--localhost:8000/blogs

