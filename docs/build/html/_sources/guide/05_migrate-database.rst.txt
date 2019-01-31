**************************************************
Migrate Database
**************************************************

After cloning the project, we need to create the equivalent tables in our database.  Note that the database is deliberately exclude from the GitHub source control, via an entry of *.sqlite3 in the .gitignore file.
That way, each developer builds the database from scratch and and then works with a clean set of tables for their development purposes.

First though, a good practice is to first run the makemigrations command before you make changes to the database.  
This doesn't touch the database, but instead creates a trail of python code that replicates the instructions required to be made.
In turn, this can be used later to roll back or recreate model changes, and investigate what took place.

After having run the migrations command, we then run the migrate command.
This does affect the database, and the first time we run it, it migrates the complete data structure by replicating the models as tables in the database.
Thereafter the migrate command updates the database with the latest changes.

So, lets make migrations and migrate the models via the following:

::

    On Linux/Mac:
    python manage.py makemigrations
    python manage.py migrate

    On Windows:
    py manage.py makemigrations
    py manage.py migrate
