
from apps.anonymous.urls import DEFAULT_URL
from django.shortcuts import redirect
from django.urls import reverse


def error(request):
    """
    Custom handling of error requests; which default to home page with
    dialog pop up explaining the situation.
    """
    request.session["glaze_url"] = reverse("anonymous:error")
    return redirect(DEFAULT_URL)
