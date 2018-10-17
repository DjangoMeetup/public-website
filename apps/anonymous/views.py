
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView


class HoldingView(TemplateView):

    template_name = "anonymous/holding.html"
