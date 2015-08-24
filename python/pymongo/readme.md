# Python & Mongo
And Flask, lol.

## Just playing Around, Setup:
Gotta have MongoDB installed, Go [here](http://docs.mongodb.org/manual/administration/install-on-linux/)

    $ virtualenv venv
    $ source /venv/bin/activate
    $ pip install -r requirements.pip

    # Some fake data
    $ python fixtures.py

## Run it
Make sure VENV is activated man..

    $ python manage.py runserver

- Go to `http://localhost:5000`
- Go to `http://localhost:5000/admin` with `admin:admin`