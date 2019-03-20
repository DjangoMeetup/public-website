"""
Populate test data for Django Meetup
"""


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.dev')

import django
django.setup()

# Requried models
from member.models import Person


# Populate Runningman with test data
def populate_test_data():

    # Create array of user details
    users = (
        ('dirk', 'dirk@djangomeetup.com', 'Django001'),
        ('gary', 'gary@djangomeetup.com', 'Django001'),
        ('andrey', 'andrey@djangomeetup.com', 'Django001'),
        ('chris', 'chris@djangomeetup.com', 'Django001'),
        ('felix', 'felix@djangomeetup.com', 'Django001'),
        ('jason', 'jason@djangomeetup.com', 'Django001'),
    )

    # Populate database with known users
    for user_details in users:
        new_user = Person(username=user_details[0], email=user_details[1])
        new_user.set_password(user_details[2])
        new_user.is_email_verified = True
        new_user.is_active = True
        new_user.save()


# Default execution and console log
if __name__ == '__main__':
    print('Populating test data')
    populate_test_data()
    print('Populating test data is complete')
