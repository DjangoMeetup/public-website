**************************************************
Migrate Database
**************************************************

After cloning the project, we need to create the equivalent tables in our database.  Note that the database is deliberately exclude from the GitHub source control, so that each developer gets to work with a clean set of tables.

A way to do this is migrate the data structure using the migrate command, which will replicate the models as tables in the database.

However, a good practice is to first run the makemigrations command.  This creates a trail of python code that replicates the instructions made to the database each time the migrate command is used.  In turn, this can be used later to recreate model changes, or even investigate what took place.

So, lets make migrations and migrate the models by running the following:

::

    On Linux/Mac:
    python manage.py makemigrations
    python manage.py migrate

    On Windows:
    Py manage.py makemigrations
    py manage.py migrate
