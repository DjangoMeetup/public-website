.. Django Meetup documentation master file, created by
   sphinx-quickstart on Thu Jan 24 23:21:42 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. meta::
   :description: Installation guide for the Django Meetup public website.
   :keywords: Django Meetup, installation


Django Meetup - Overview
========================================

.. topic:: Overview

Django Meetup is an open source project designed to provide a working model for Meetup group members and other Django enthusiasts. This guide takes you through the process of setting up the public website from the `Django Meetup github repository <https://github.com/DjangoMeetup/public-website>`_.

Note that the information provided in `the official Django documentation <https://docs.djangoproject.com/en/>`_ is far more comprehensive.  However, this provides some additional practical understanding of what is going on when setting up this project.

The understanding is important because due to various permuations, such as different operating systems or different version numbers, you may encounter some errors and issues along the way (it happens often!).  Understanding the why to what you’re trying to do can help solve the problem, sometimes.

At worst, if you encounter a problem you’re unable to solve, you can simply delete all the folders created below, or one of either the environment or public website folders, and then start again.

While a large component of Django users use Linux/Mac, many new users come to Django via Windows.  This guide tries to document instructions for all those OS variants.

Contents:
----------

.. toctree::
   :maxdepth: 6

   guide/01_quickstart
   guide/02_download-project
   guide/03_virtualenv
   guide/04_packages
   guide/05_migrate-database
   guide/06_environment-variables
   guide/07_runserver
   guide/80_python
   guide/81_debugging-tricks
   guide/82_sphinx
   guide/99_rst-guide


