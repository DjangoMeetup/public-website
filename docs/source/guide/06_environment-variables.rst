**************************************************
Environment Variables
**************************************************

The settings file uses python-decouple to read in environment variables from a .env file.  However, this file contains sensitive password data, so it is deliberately excluded from the public git repo (via the .gitignore file).  Not also, that because the file name is preceded by a dot (‘.’) it becomes a hidden file.

So we need to create our own .env file.  For initial purposes of getting the web project up and running, we can use dummy variables to provide you with an idea of the type of variables required.

In the public-website folder, we create that .env file, and then save the following into it.

::

    DEBUG=True
    DOMAIN=localhost
    SECRET_KEY=-#^op)l91*7@$4qthsxjjs7dl1*-@1$l11^je_@@&3h9&ipe#w
    GOOGLE_RECAPTCHA_SECRET_KEY= 6LexSoNNCCCCCEt_8VpyiaubPwb48LLq21wmp4Mr
    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_USER=admin@djangomeetup.com
    EMAIL_HOST_PASSWORD=safeandsecure

This would allow the basic front page of the web site to get up and running.  
However, you'll still need to tailor these variables for your own usage.  
In particular, you'll want to use your own **SECRET_KEY**. 
And in the case of the **GOOGLE_RECAPTCHA_SECRET_KEY**, you’ll have to get one from Google otherwise your captcha won’t work.

So lets modify these variables to provide your own. Here’s a rundown on how to do that.

Secret Key
##################################################

Your secret key is variously used for hashing tokens for user sessions, password resets, and other types of encryption.   Its important to keep your’s secure, and out of version control.
For development purposes, generate your own secret key.  You can create one either by django’s inbuilt function, or by using a helpful website.

To use the Django Inbuilt function, run the following command:

::

    On Linux/Mac:
    python3 manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

    On Windows:
    py manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Alternatively you can generate a django secret key from other places, such as this website:  `<https://www.miniwebtool.com/django-secret-key-generator/>`_

Google Recaptcha Secret Key
##################################################

The Django Meetup website uses Google’s reCAPTCHA v2 version.  You will need to sign up for an API key pair for the site, and register your localhost.

Head over to https://www.google.com/recaptcha/admin#list and register your localhost address after choosing a reCAPTCHA version 2 tickbox type.

For the label, use localhost, and for the domain, use 127.0.0.1.  Then add an email address of your choice.

The admin site then should provide you with your site key and your secret key.

The site key is added to the HTML in the widget file.  The file address for that in mine was:
CAN WE ADD A settings.RECAPTCHA_SITE_KEY AS A VIEWS CONTEXT VARIABLE?

::

    /djangomeetup/public-website/apps/formality/templates/formality/widget_recaptcha.html

    /env/bin/public-website/apps/formality/templates/formality/widget_recaptcha.html

The secret key is added to your .env file, as shown above, and should be kept away from git source control, and anyone else’s eyes.

If you want a tutorial on the process, this provides some useful information: https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html
