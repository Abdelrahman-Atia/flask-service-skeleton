# Flask Rest API Skeleton
A flask  restful API Skeleton


## Technologies used
* **[Python](https://www.python.org/downloads/)** - 3.7
* **[Flask](flask.pocoo.org/)** - 1.0.2
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** 
* Minor dependencies can be found in the requirements.txt file on the root folder.


## Setup
* first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd flask-service-skeleton
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python venv
        $ pip install autoenv
        ```

* #### Environment Variables
    copy .env.example to .env file:
    ```
    $ cp .env.example .env
    ```
    Add a `config.py` file in the config folder (use `config/config.py.example` as a template).



    Save the file. CD out of the directory and back in. `Autoenv` will automagically set the variables.

* #### Install your requirements
    ```
    pip install -r requirements.txt
    ```

* #### Migrations
    if you are using  psql On your psql console, create your database first and change the name in the config.py file:
    ```
    > CREATE DATABASE flask_api;
    ```
    Then, make and apply your Migrations
    ```
     python manage.py db init

     python manage.py db migrate
    ```

    And finally, migrate your migrations to persist on the DB
    ```
    python manage.py db upgrade
    ```

* #### Running It
    On your terminal, run the server using:
    ```
    flask run
    ```
* #### Unit Testing
    add your test file to the `specs` folder usiing the following pattern `filename_spec.py`

    then on you terminal run 
    ```
    python manage.py test
    ```