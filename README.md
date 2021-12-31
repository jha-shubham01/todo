# TODO

# Description
This project is a simple TODO web application
where backend and frontend are sparate apps.

## Technology Stack
Backend: Django, Django Rest Framework
Frontend: VueJS CLI

## To run the project
Prerequisits: Python3, virutalenv, node, npm

1. Checkout the code
### Backend
2. Create virtual environment (virutalenv .env)
3. Activate the environment (source .env/bin/activate)
4. Install all the packages (pip install -r requirements.txt)
5. Navigate inside the project (cd backend)
6. Migrate (python manage.py migrate)
7. Create a super user (python manage.py createsuperuser)
   Fill in all the details on the terminal to create the super user
8. Run the backend server (python manage.py runserver)

### Frontend
2. Navigate in the frontend dir (cd frontend)
3. Install the packages (npm install)
4. Run the backend server
5. Run the frontend server (npm run serve)


### Assumptions: 
Before running the frontend app, there should be at least 1 user in the database.
Always the user with id 1 is creating the Todo list.

### Future Scope:
Adding VueX.
Create Login for the app.
Use the logged in user to create the Todo list.
Filter the Todo list by logged in user.
Deletion of Todo
