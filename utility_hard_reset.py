"""
Hard reset for database through the following:
a) deleting the following:
- someProject/db.sqlite3
- someProject/someApp/__pycache__/ (deletes all contents)
- someProject/someApp/migrations/ (deletes the entire folder)
b) run the following script
- python manage.py migrate
- python manage.py migrate --run-syncdb
- python manage.py makemigrations
- python manage.py migrate
"""

import os, shutil
import manage

base_dir = os.path.dirname(os.path.abspath(__file__))

# a) delete all unwanted files and folders
for root, dirs, files in os.walk(base_dir):
    # Remove unwanted files
    for name in files:
        file_path = os.path.join(root, name)
        # Remove sqlite3 databases
        if ('.sqlite3' in file_path):
            if os.path.isfile(file_path):
                os.unlink(file_path)
        # Remove all files in __pycache__
        if ('__pycache__' in file_path):
            if os.path.isfile(file_path):
                os.unlink(file_path)
    
    """
    # Remove unwanted folders
    for name in dirs:
        folder_path = os.path.join(root, name)
        # Remove all folders that contain migrations
        if ('migrations' in folder_path):
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
    """

# b) run migration scripts
os.system('python manage.py migrate')
os.system('python manage.py migrate --run-syncdb')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
