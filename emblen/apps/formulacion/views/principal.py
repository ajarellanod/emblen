from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "formulacion/principal.html"
