# AiderAuth
![Grasp Logo](https://img.shields.io/static/v1?label=Grasp&message=we%20lmade%20this&color=green)

Startup project for exploring GeoDensity using Docker (compose), django & real data

## Application purpose

Intent of application is to visualize business denisity using geo- and business data.

![published lucidchart](#) # Add a project drawing if you want to :)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### simply put

- add your external database under the DATABASE section in config.ini
- add your secrets to .env file you create in /src directory
- add your query ("select * from table") to querries.py
- import and use querries is tasks.py
- create a model in models.py aligned with external database schema
- run task query_data if you want to create a .csv
- run example_store_data_to_model if you want to store data on your local DB

### Prerequisites

What you need to install the software and how to install them

```
python3.7
docker
docker-compose
pip install pipenv
local postgres db & pgadmin is convenient
```

### Environment Variables
```
Declare variables in shell (echo:linux/set:windows) or add .env file to project with your secrets. Make sure .env is referenced in .yml when docker-compose
```
- Host=secret
- Database=secret
- User=secret
- Password=secret

### Installing
```
Instructions on setting up a local project version:
```

- 1: mkdir <your_project_name>
- 1: cd <your_project_name>
- 3: git clone https://github.com/grasp-labs/geoDensity.git
- 4: cd geoDensity
- 5: cd src
- 5: pipenv install (installs dependencies)
- 6: pipenv shell (activates virual environment)

#### Localhost
```
Localhost require a little bit of configuration
```

- 1: create a local postgres DB
- 2: align db settings in .ini with your local DB
- 3: python manage.py runserver


#### docker-compose
```
cd to src/ folder and run docker-compose -f compose.yml up --build
```

Visit localhost:8000 and a simple index should be displayed.
visit localhost:8000/admin and logon with superuser/acde1234 (same as configured in settings/.ini)

##### Other
```
Connection to a external database with some actual data to play with is ideal
```
