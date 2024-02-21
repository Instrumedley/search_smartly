## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Pre-requisites

Before you begin, ensure you have met the following requirements:

- ⚡️ Python 3.11 installed on your system.
- 🦾 PostgreSQL with PostGIS extension for GeoDjango.
- 🫀 OSGeo4W for GeoDjango dependencies on Windows


### Installing ⚡️

A step-by-step on how to get the environment up and running.

Setting up the Environment:

- #### Install Python 3.11 or above

    Make sure Python 3.11 is installed on your Windows machine. You can download it from the [official Python website](https://www.python.org/downloads/)

- #### Virtual environment
    - Create a virtual environment to isolate our package dependencies locally.
       ```bash 
      python -m venv env
      ```
    - Activate the virtual environment:
      - On Windows: `env\Scripts\activate`
      - On macOS/Linux: `source env/bin/activate` 
      _Tip: If you use an IDE like PyCharm, this can be easily taken care for you_ 

    
- ####  GeoDjango Dependencies:
    Download and install OSGeo4W from [OSGeo4W website](https://trac.osgeo.org/osgeo4w/). This includes GDAL, GEOS, and PROJ.4, which are necessary for GeoDjango. During installation, select Express Install and choose to install the GDAL package.


- #### PostgreSQL and PostGIS:
  Install PostgreSQL and the PostGIS extension. You can download PostgreSQL from PostgreSQL Official Site and follow the 
  instructions to install PostGIS within your PostgreSQL installation.


### Configuring the Project ⚡️


Clone this repository to your local machine:

 ```sh
git clone https://github.com/Instrumedley/search_smartly.git
 ```

Install dependencies:
Ensure you are in the project root directory where `requirements.txt` is located, then run:
```sh
  pip install -r requirements.txt
```
This command installs all the necessary Python packages listed in `requirements.txt`.

- #### Database Setup:

Create a PostgreSQL database and apply the PostGIS extension. This project uses the default port 5432
```sql
CREATE DATABASE smartly;
\c smartly;
CREATE EXTENSION postgis;
```

or if you decide to create one with a different name or port, make sure to update `settings.py` to reflect your DB

- #### Run migrations
 
Apply migrations to set up your database tables:
```shell
python manage.py migrate
```

- #### Run the server
 
Start the Django development server.
```shell
python manage.py runserver
```

- #### Importing PoI Data
 
Use the custom management command to import Points of Interest from your data files.
```shell
python manage.py import_pois path/to/your/datafile1.csv path/to/your/datafile2.json
```


## Using the Admin site ⚡️

Access the Django admin site at http://127.0.0.1:8000/admin to manage the Points of Interest.

Log in using your superuser account, or create one if you haven't already:

```shell
python manage.py createsuperuser
```

### Built with ⚡️

- Django 
- GeoDjango 
- PostgreSQL & PostGIS

### Author ⚡️

Rafael Alfredo Santos

