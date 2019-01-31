.. meta::
   :description: This chapter provides a quick start overview of the Django Meetup public website.
   :keywords: Django Meetup, quick installation, quick start, quickstart

**************************************************
Quick Installation
**************************************************

For those already comfortable with the process, this section provides a skeleton of the steps involved.

Note, you would of course need to insert the name of your git repository when you see **<yourrepo>**. Also, these steps use github's HTTPS cloning method (as opposed to SSH).

If you prefer more detail, you can follow the full instructions in the subsequent sections.

--------------------------------------------------

On Linux/Mac:
##################################################

Download Project
==================================================

Create your project directory: ``mkdir DjangoMeetup``

Change to project directory: ``cd DjangoMeetup``

Fork the project from: ``https://github.com/DjangoMeetup/public-website``

Clone the project: ``git clone https://github.com/<yourrepo>/public-website.git``

Add parent repo: ``git remote add upstream https://github.com/DjangoMeetup/public-website.git``

Virtual Environment
==================================================

In the same directory, create a virtual environment: ``python -m venv env``

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

Windows commands are largely the same as for Linux and Macs.
In fact, the differences become nearly negligible if you download and use the excellent command line tool `Git Bash <https://gitforwindows.org/>`_
If you do use Git Bash, you'll have to include the source command when you activate the virtual environment, ie. ``source env/Sripts/activate``.
 
However, if using the Windows command line tool, then users should bear these in mind:

1. you only need type ``py`` instead of the full ``python``.
2. you must use back slashes for command line file paths.
3. virtual environment activate folder is kept in a Scripts folder (vs bin for Linux\Mac)
4. virtual environment activation does not require the source command, ie. it will suffice to use ``env/Sripts/activate``
5. file paths are not case sensitive.

Here are the steps restated for Windows users:

Download Project
==================================================

Create your project directory: ``mkdir DjangoMeetup``

Change to project directory: ``cd DjangoMeetup``

Fork the project from: ``https://github.com/DjangoMeetup/public-website``

Clone the project: ``git clone https://github.com/<yourrepo>/public-website.git``

Add parent repo: ``git remote add upstream https://github.com/DjangoMeetup/public-website.git``

Virtual Environment
==================================================

In the same directory, create a virtual environment: ``py -m venv env``

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
