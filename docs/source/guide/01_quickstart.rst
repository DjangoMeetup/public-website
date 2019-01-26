.. meta::
   :description: This chapter provides a quick start overview of the Django Meetup public website.
   :keywords: Django Meetup, quick installation, quick start, quickstart

**************************************************
Quick Installation
**************************************************

For those already comfortable with the process, this section provides a skeleton of the steps involved.

Note, you would of course need to insert the name of your git repository when you see **<yourrepo>**. Also, these steps use github's HTTPS cloning method (as opposed to SSH).

If you prefer, you can follow the full instructions in the subsequent sections.

--------------------------------------------------

On Linux/Mac:
##################################################

Download Project
==================================================

Create your project directory: ``mkdir DjangoMeetup``

Change to project directory: ``cd DjangoMeetup``

Fork the project from: ``https://github.com/DjangoMeetup/public-website``

Clone the project: ``git clone https://github.com/<yourrepo>/public-website.git``

Virtual Environment
==================================================

Create a virtual environment: ``python -m venv env``

Activate your environment: ``source env/bin/activate``

Load Packages
==================================================

Install packages: ``pip install requirements/dev.txt``

Migrate Database
==================================================

Run migrations: ``python manage.py makemigrations``

Run migrate: ``python manage.py migrate``

Environment Variables
==================================================

Create the environent file **.env** and add:
::

    DEBUG=True
    DOMAIN=localhost
    SECRET_KEY=-#^op)l91*7@$4qthsxjjs7dl1*-@1$l11^je_@@&3h9&ipe#w
    GOOGLE_RECAPTCHA_SECRET_KEY= 6LexSoNNCCCCCEt_8VpyiaubPwb48LLq21wmp4Mr
    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_USER=admin@djangomeetup.com
    EMAIL_HOST_PASSWORD=safeandsecure

Change SECRET_KEY and GOOGLE_RECAPTCHA_SECRET_KEY to your own keys

Run Server
==================================================

Start the server: ``python manage.py runserver``

--------------------------------------------------

On Windows
##################################################


Download Project
==================================================

Create your project directory: ``mkdir DjangoMeetup``

Change to project directory: ``cd DjangoMeetup``

Fork the project from: ``https://github.com/DjangoMeetup/public-website``

Clone the project: ``git clone https://github.com/<yourrepo>/public-website.git``

Virtual Environment
==================================================

Create a virtual environment: ``py -m venv env``

Activate your environment: ``env\scripts\activate``

Load Packages
==================================================

Install packages: ``pip install requirements\dev.txt``

Migrate Database
==================================================

Run migrations: ``py manage.py makemigrations``

Run migrate: ``py manage.py migrate``

Environment Variables
==================================================

Create the environent file **.env** and add:
::

    DEBUG=True
    DOMAIN=localhost
    SECRET_KEY=-#^op)l91*7@$4qthsxjjs7dl1*-@1$l11^je_@@&3h9&ipe#w
    GOOGLE_RECAPTCHA_SECRET_KEY= 6LexSoNNCCCCCEt_8VpyiaubPwb48LLq21wmp4Mr
    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_USER=admin@djangomeetup.com
    EMAIL_HOST_PASSWORD=safeandsecure

Change SECRET_KEY and GOOGLE_RECAPTCHA_SECRET_KEY to your own keys

Run Server
==================================================

Start the server: ``py manage.py runserver``
