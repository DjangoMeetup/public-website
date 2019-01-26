**************************************************
Appendix 1: Python Installation
**************************************************

This guide assumes you have Python 3.X installed.  If you are still using Python 2.X, you may encounter some issues.   And while you can use the word python to run commands in both versions, if you have both versions installed you can avoid ambiguity by using python3 as the command.

If you’ve not got Python installed, head over to the Python release pages and download from there.  At time of writing, Python 3.7 would have been the latest stable version to use.
If you want to check your Python version, open your command line tool (eg. Bash, Git Bash for Windows, PowerShell, or just the plain old Windows command line), and run the following command:
::

    On Linux/Mac:
    python –V

    On Windows:
    py -V

Where py is the built-in Python launcher for Python3 on Windows.

Note also that the commands are to be pasted in after the terminal prompt sign.  In Linux, the default prompt is $. In Windows the default is >.

Flags
##################################################

A quick word about the command flags generally used with python commands.  For example, when you type python -m venv, the -m indicates that a module name follows, so there’s no need to use the .py suffix.

You can see all the flags by typing
::

    python --help

Alternatively you can look at the docs here: https://docs.python.org/3.7/using/cmdline.html
