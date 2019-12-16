# Understanding Django
Look through the commits to get a basic idea for understanding django for creating APIs.

## Setting up postgres

Setup postgres for your database.

### Installing postgres in your system.

For Ubuntu 17.04 - 17.10 -

```
sudo apt-get install postgresql-9.6
```

### Using postgresql

For Entering the postgresql command line.

```
psql -U <user_name> -d postgres
```

### Creating a user and setting up a database for your project.

Create a User with password and create a database for your project.

```
CREATE USER “project’_one_rw” WITH PASSWORD 'password123’;
CREATE DATABASE project_one with owner 'project_one_rw';
```

## Cloning this github project

Clone this github project to your local.

```
git clone https://github.com/Hawkeye091/Codeasylums_Django.git
```

## Change directory and enter student_project

Enter the project directory.

```
cd student_project
```


## Virtual Environment

Make sure you install and make a virual environment which will have all the packages required for your project.

### Installing virtual environment

Virtual enviroment installation.

```
sudo pip3 install virtualenv 
```

### Create and use Virtual environment

Creating a virtual environment for your project.

```
virtualenv --python=$(which python3) student_project_env
```

Using/activating a virtual environment.

```
source student_project_env/bin/activate
```

Command to deactivate a virtual environment when you don't need it.

```
deactivate
```

### Installing requirements.txt

Install the required packages for the project.

```
pip install requirements.txt
```

## Setting the environment variables

Source the variables.sh file so the your variables are exported in the environment.

```
source variables.sh
```

## Making migrations and migrating

The custom tables made in the app's models.py need to be migrated into the postgres database you've created.

```
python manage.py makemigrations
python manage.py migrate
```

## Runserver

Runserver to interact with the admin or apis.

```
python manage.py runserver
```
