# How To Setup Environment

* Install [Python 3](https://www.python.org/).
* Create a virtual environment called OPTA and activate it. You can use [venv](https://docs.python.org/3/tutorial/venv.html) or [virtualenv](https://virtualenv.pypa.io/en/stable/#).
* Upgrade pip
    ```sh
    (OPTA) ~ $ pip install --upgrade pip
    ```
* Install Django
    ```sh
    (OPTA) ~ $ pip install django
    ```
* Clone this repository, then runserver
     ```sh
    (OPTA) ~ $ .../Opta/opta_project python manage.py runserver
    ```
* Create the database
     ```sh
    (OPTA) ~ $ .../Opta/opta_project python manage.py migrate
    ```
