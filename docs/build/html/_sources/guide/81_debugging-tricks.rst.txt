**************************************************
Appendix 2: Debugging Tricks
**************************************************

There are several approaches you can use to help you in debugging.  Here are some of the more standard tricks.

Use The Debug Toolbar
##################################################

The Django Meetup model comes with the django debug toolbar in dev mode.  So use that.

Evaluate Variables In Settings File
##################################################

If for some reason the settings file doesn’t seem to be picking up the variables, you can use this approach to help determine what’s going on.

Simply introduce a print() statement into the settings file, with the name of the environment variable you want to inspect.

Of course, you’ll have to introduce it after the environment variable has been called.

For example, in the settings file, a print statement could appear as following:
::

    GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')
    print('RECAPTCHA KEY: ', GOOGLE_RECAPTCHA_SECRET_KEY)

Then when you execute the runserver command, you will see this variable printed out among the debugging feedback.
