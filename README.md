# TODO App

# Description
This project is a simple TODO web application <br />
where the backend and frontend are standalone apps.

## Technology Stack
Backend: Django, Django Rest Framework <br />
Frontend: VueJS CLI

## To run the project
Prerequisites: Python3, virutalenv, node, npm

1. Checkout the code
### Backend
2. Create virtual environment (virutalenv .env)
3. Activate the environment (source .env/bin/activate)
4. Install all the packages (pip install -r requirements.txt)
5. Navigate inside the project (cd backend)
6. Migrate (python manage.py migrate)
7. Create a superuser (python manage.py createsuperuser) <br />
   Fill in all the details on the terminal to create the superuser
8. Run the backend server (python manage.py runserver)

### Frontend
2. Navigate in the frontend dir (cd frontend)
3. Install the packages (npm install)
4. Run the backend server
5. Run the frontend server (npm run serve)


### Assumptions
Before running the frontend app, there should be at least 1 user in the database. <br />
Always the user with id 1 is creating the Todo list. <br />

### Future Scope
Add VueX. <br />
Create a login for the app. <br />
Use the logged in user to create the Todo list. <br />
Filter the Todo list by logged in user. <br />
Deletion of Todo <br />


### Learn from the Video Series:
https://youtube.com/playlist?list=PLdLYbRBk3sGmX02sfc4dNU0DLh7hmK59P

