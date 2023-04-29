# Star Wars

## Scope

App which allows you to collect, resolve and inspect information about characters in
the Star Wars universe from the SWAPI.
The entry endpoint for data retrieval is: https://swapi.co/api/people/

## Technology Stack

Django Framework<br/>
postgreSQL - Database<br/>
docker-compose - to created and orchestrate different services<br/>

## App Setup:

1. Clone the repo 
  **git clone https://github.com/TulasiMakam/swapi_django**

2. The application is containerized using Docker. Run docker-compose command below to build and create 2 services one for swapi and another for db.
  **docker-compose up -d**<br/>

**NOTE:** Install the binary dependencies or dev dependencies if needed based on your enviroment or OS.<br/>

3. In browser, go to http://localhost:8000/, the application up and running.

4. Follow the steps below to Create a superuser within application service(only if needed to access django_admin)<br/>

    docker exec -it swapi sh<br/>
    python manage.py createsuperuser<br/>
    Add username, user email and password<br/>
    Now your admin login is created<br/>

Login to:
Django-admin : http://localhost:8000/admin/
Browser: http://localhost:8000/

## Features:

1. Clicking on 'Fetch' button in the browser will fetch all the data from the swapi and stores data in the form of csv file. 
2. Collections Button - Will display the list of CSV Files
3. Select a CSV File for the detailed display. This view has sort, search, loadmore and also a feature to count the occurences of custom columns.

## Improvements:

1. Make the tasks asynchronous - Celery
2. In-memory db, caching - Redis
3. Make REST Complaint - djangorestframework
4. Interface for restful APIs - Swagger OpenAPI
5. Unit tests, integration tests
6. UI - Angular App