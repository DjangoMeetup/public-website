
from apps.anonymous.forms import EntryForm
from apps.formality.views import evaluate_recaptcha
from apps.glaze.views import GlazeMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView


class ErrorGlaze(GlazeMixin, TemplateView):

    template_name = "anonymous/glaze_error.html"
    # Glaze configuration
    glaze_heading = "Error Raised"


class HoldingView(TemplateView):

    template_name = "anonymous/holding.html"


class EntryGlaze(GlazeMixin, FormView):

    form_class = EntryForm
    success_url = reverse_lazy("anonymous:entry_granted")
    template_name = "anonymous/glaze_entry_form.html"
    # Glaze configuration
    glaze_heading = "Under Development Access"
    glaze_form_heading = "Submit Credentials"
    glaze_form_action = reverse_lazy("anonymous:entry")

    def initialize_post(self, request):
        recaptcha_error = evaluate_recaptcha(request)
        if recaptcha_error:
            self.glaze_external_errors.append(recaptcha_error)


def entry_granted(request):

    request.session["is_site_accessible"] = True
    return HttpResponseRedirect(reverse("anonymous:home"))


class HomeView(TemplateView):

    template_name = "anonymous/home.html"
