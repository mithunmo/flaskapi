
FLASK APi
=======================================

API end points
=======================================

1) /outbound/sms

2) /inbound/sms

1) The API can be accessed using HTTP basic authentication

2) Only POST methods are allowed

3) The API accepts json input and accepts to,from and text fields


PACKAGES USED
========================================
Install the following packages in the virtualenv  ( pip install -r requirements.txt)

`
appdirs==1.4.0

click==6.7

Flask==0.12

Flask-HTTPAuth==3.2.1

Flask-Redis==0.3.0

Flask-SQLAlchemy==2.1

itsdangerous==0.24

Jinja2==2.9.4

MarkupSafe==0.23

mockredispy==2.9.3     # For unit testing only

packaging==16.8

psycopg2==2.6.2

py==1.4.32

pyparsing==2.1.10

pytest==3.0.6

redis==2.10.5

requests==2.13.0

six==1.10.0

SQLAlchemy==1.1.5

Werkzeug==0.11.15

wheel==0.24.0`


RUN the APP
============================================

start the postgresql server with the test data

start the redis

`python run.py`



TESTING
==========================================

</b> UNIT TESTING </b>

To run the unit testcases go to home folder of the flask app and execute .
It makes use of sqllite and mockredis to perform the tests

`pytest tests`

<b>AUTOMATED TESTING </b>

All the testcases are defined in tests/testcases.json
To run the  testcases go to tests folder and execute . This needs the postgresql server and redis server to be started .
 Postgresql should have test dump data .

`python testautomation.py`

This outputs the number of testcases passed and failed based on the testcase message value















