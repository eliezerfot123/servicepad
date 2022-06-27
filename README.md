# Servicepad Test
> Test for servicepad company for Eliezer Romero

## Distribution
There are two folders where the code is distributed:
1. logic_test (First part of the test - Logic Test).
2. app-servicepad (Second part of the test - REST Api Flask)

## How to install?

1.) You should install a packaging tool for Python

 ~~~ 
    $ pip3 install --user pipenv
 ~~~

2.) Create the python environment and install the necessary dependencies

~~~ 
    $ pipenv shell 
    $ pipenv install
~~~
> this install all dependencies in a python container


### To view the logic test, you should go into the logic_test folder and run each of the exercises and unit tests performed.

for example:

~~~
    $ cd logic_test

    $ python3 exercise01.py

    $ python3 exercise02.py

    $ python3 exercise03.py
~~~


see the unit test so you can execute
~~~
    $ pytest
~~~

### To view the REST API Flask, you should go into the api-servicepad folder and run each of the exercises and unit tests performed.

***
Please install postgresql on your computer 
***
$ sudo apt install postgresql

create your database for example:
> $ sudo su postgres 

> $ createdb yourdbname -O youruser

and now you can execute ant testing the rest api

1.) In the configuration file for 'SQLALCHEMY_DATABASE_URI'. Please for your user, password and name from you databae
> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://***youruser:yourpassword***@localhost/***yourdbname***'
***
****Boila! Now you can create your tables:****
~~~
    $ python3
    >>> from api.auth.models import Users
    >>> from api.publications.models import Publication
    >>> from config.settings import db
    >>> db.create_all()
~~~

With this you will have created the tables in your database, we will now be able to see our api.
> Remember to have your container active
> with pipenv shell 

So run that and test the rest api

~~~
    $ export FLASK_APP=apps
    $ flask run
    * Running on http://127.0.0.1:5000/
~~~
or
~~~
    $ python3 apps.py
~~~


Now go to [http://127.0.0.1:5000](http://127.0.0.1:5000) and you can see thanks to swagger the api documentation and see how it works. 