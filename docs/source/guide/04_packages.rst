**************************************************
Load Packages
**************************************************

Now that we have the environment basics set up, we can add the packages required for the project.

Packages are a collection of libraries, with each library containing pre-written code typically for some specific use.  The Python Package Manager bundles these libraries together in a package, which makes it easier to download the entire package, rather than each library seperately.

We could add the packages individually, one-by-one, using the following pip command:

::

    pip install package-name

However, its smarter to use the dependency management.

Dependency Management
##################################################

The repo includes requirements files in the requirements folders, namely the **base.txt**, **dev.txt** and **prod.txt**.  If you inspect each file you’ll see the the packages and their version numbers required.  Note that the dev and prod file already include a link to the base file.

We’re only concerned with development at this stage.  So change into the requirements folder and install the required dev & base packages via the following command:

::

    pip install dev.txt
