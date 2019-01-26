**************************************************
Virtual Environment
**************************************************

Create the Virtual Environment
##################################################

Each time we start a new project, we want the virtual environment to be associated with that project and neatly isolated from any other projects we're working on. So let’s create a new virtual environment inside the DjangoMeetup folder.

Versions of Python before 3.3 used pip or pyvenv + third party tools to create virtual environments.  However, Python 3.3 and versions since have an in-built venv module, which is recommended.  So we’ll assume you’re using venv.

You can use any name you choose for the virtual environment, but typical names include the likes of venv , env, or env_projectname.  Here we’ll just use env to help distinguish from the venv command.

Make sure your command line is in the DjangoMeetup folder, then run the following command to create the virtual environment env:

::

    On Linux/Mac:
    python -m venv env

    On Windows:
    py -m venv env

Because the virtual environment folder env is above the public-website folder, its kept out of the git source control. That’s good because the environment only works on your machine and would be just bloat in the source control.

Activate & Deactivate Virtual Environment
##################################################

We then activate the virtual environment.  In Linux and Mac, you use the source command to run the activate file in the bin folder.  In Windows, you simply run the activate.bat file in the Scripts folder.

Note that the venv command you ran earlier creates a bin folder in Linux/Mac and a Scripts folder in Windows, so your path to the activate file will obviously differ depending on your OS.

For PowerShell users, see the note below.

In Windows, you can also use Git Bash, which mimics the Linux and Mac commands.  In which case, you would also use the source command.

::

    On Linx & Mac:
    source env/bin/activate

    On Windows:
    env\Scripts\activate

    On Windows Git Bash
    source env/Scripts/activate

After you’ve run activate you’ll be reminded that you’re in the virtual environment, because at the beginning of your prompt you will now see the environment name in parentheses.  For example, the **(env)** in the following:

::

    On Linux/Mac:
    (env) ~/DjangoMeetup/ $

    On Windows:
    (env) C:\Owner\Projects\DjangoMeetup >

This means the Python you now execute will be from the virtual environment, as are all packages (and package installations will go to that virtual environment, rather than the system)
To deactivate the environment, you simply use the command:

::

    deactivate

Note that if you are using Windows PowerShell, you might run into restrictions trying to utilize the activation script and will have to first run the command below as an administrator. This allows the activation script to be run since it was signed locally.

::

    Set-ExecutionPolicy RemoteSigned
