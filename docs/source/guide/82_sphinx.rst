==================================================
Appendix 4: Sphinx Help
==================================================

Using Sphinx
==================================================


PDF Creation
==================================================

Install Mitex
--------------------------------------------------

Download Mitex from mitex.org

Run installer and auto install missing packages.

This will create an app called TeXworks.

Open up TeXworks.


Create the PDF
--------------------------------------------------

Back in terminal, go to folder with Sphinx makefile and run:

`./make.bat latexpdf`

This creates a folder called latex in your build folder

Within it, Then in the documents/latext there is a file called DjangoMeetup.tex
This is the raw latex file.

Open this file in TeXworks.
Click run.
It should produce the finished pdf report in the latext folder.
