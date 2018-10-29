
from django.conf import settings

import json
import urllib


def evaluate_recaptcha(request):
    # Google Recaptcha validation
    recaptcha_response = request.POST.get("g-recaptcha-response")
    url = "https://www.google.com/recaptcha/api/siteverify"
    values = {
        "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        "response": recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    if result["success"]:
        return None
    else:
        return "Site access denied, Google reCaptcha authentication failed"
