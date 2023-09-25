=================
Coding task 
=================

For this challenge, we will work with Python, and specifically Django, In order to create an HTTP service with two  endpoints.
My enviroment is Ubuntu 20.04 in a Virtual Machine

if you say 'helloworld' it will reply back 'hello $name_of_the_person
if you 'status' it will reply with the status of the coding task

Installation
============

We need to install the pre-requirements, before running it.

Update repositories of available packages to install, with
the following command:


```
  $ sudo apt update
```
Install necessary minimum dependencies, with the following command:

```
  $ sudo apt-get install python3-venv    # If needed
  $ python3 -m venv env
```

 Install Django
```

    $ python3 -m pip install django

```
Install Requirments (if required)
```

    $ pip3 install djangorestframework #install rest_framework 
    

```
And later followed by:

```

    $ python3 manage.py migrate
```
Run application
===============

After which you can run, in our case we prefer to run it on the port 8080 
```
    $ python3 manage.py runserver 8080  #use another port if 8080 is used 
```
For testing our endpoints, we can used tools like "Postman", or use simply Curl command if you are in using CMD
```

    $ curl --location --request GET 'http://127.0.0.1:8080/status'
    $ curl --location --request GET 'http://127.0.0.1:8080/helloworld'
```
