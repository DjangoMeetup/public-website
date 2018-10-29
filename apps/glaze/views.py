
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string


def reset_session(request):
    del request.session["glaze_url"]
    return HttpResponse(None)


class GlazeMixin:

    # Context variables for Templates
    glaze_heading = None
    glaze_form_submit_name = None
    glaze_form_action = None
    glaze_cancel_url = None
    glaze_callback_context = {}
    glaze_success_url = None
    glaze_external_errors = []


    def get_success_url(self):
        """
        Overridden so that only one success url needs to be defined
        i.e. either success_url for standard full page redirect_url
        or the glaze_success_url for Ajax render in the glaze overlay
        """
        if (self.glaze_success_url is None):
            try:
                return super.get_success_url()
            except AttributeError:
                self.success_url
        else:
            return self.glaze_success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (self.glaze_heading is not None):
            context["glaze_heading"] = self.glaze_heading
        if (self.glaze_form_submit_name is not None):
            context["glaze_form_submit_name"] = self.glaze_form_submit_name
        if (self.glaze_form_action is not None):
            context["glaze_form_action"] = self.glaze_form_action
        if (self.glaze_cancel_url is not None):
            context["glaze_cancel_url"] = self.glaze_cancel_url
        context = {**context, **self.glaze_callback_context}
        return context

    def post(self, request, *args, **kwargs):
        self.initialize_errors()
        self.initialize_post(request)
        form = self.get_form()
        is_form_valid = form.is_valid()
        if self.glaze_external_errors:
            for error in self.glaze_external_errors:
                form.add_error(None, error)
        super().post(request, *args, **kwargs)
        data = {}
        if (is_form_valid & (not self.glaze_external_errors)):
            if (self.glaze_success_url is None):
                data["is_glaze"] = False
                data["redirect_url"] = self.success_url
            else:
                data["is_glaze"] = True
                data["glaze_success_url"] = self.glaze_success_url
            self.finalize_post(request)
        else:
            data["is_glaze"] = True
            data["glaze_html"] = render_to_string(
                self.template_name,
                self.get_context_data(form=form),
                request=request)
        return JsonResponse(data)

    def dispatch(self, request, *args, **kwargs):
        """
        If the url call has come direct from the browser then return a bad request
        """
        if not (request.is_ajax()):
            return HttpResponseBadRequest()
        else:
            return super(GlazeMixin, self).dispatch(request, *args, **kwargs)

    def initialize_errors(self):
        """
        Ensure no previous errors are carried through from previous submission
        """
        self.glaze_external_errors = []

    def initialize_post(self, request):
        """
        Complete any additional functionality prior to form submission
        """
        # Intensionally empty

    def finalize_post(self, request):
        """
        Complete any additional functionality upon successful form submission
        """
        # Intensionally empty
