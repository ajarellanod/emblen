from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import JsonResponse, Http404
from django.db.models.functions import Substr

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin


class EmblenPermissionsMixin(LoginRequiredMixin, MultiplePermissionsRequiredMixin):
    class Meta:
        abstract = True


class EmblenView(View):
    
    template_name = False
    json_post = False

    def get(self, request, *args, **kwargs):
        altget = self.altget(request, *args, **kwargs)
        if isinstance(altget, dict):
            if isinstance(self.template_name, str):
                return render(request, self.template_name, altget)
            else:
                raise ValueError("template_name is not set")
        else:            
            return altget

    def post(self, request, *args, **kwargs):
        if request.POST.get("json") is not None and self.json_post:
            jsonpost = self.jsonpost(request, *args, **kwargs)
            if isinstance(jsonpost, dict):
                return JsonResponse(jsonpost, safe=False)
            return jsonpost
        else:
            altpost = self.altpost(request, *args, **kwargs)
            if isinstance(altpost, dict):
                if isinstance(self.template_name, str):
                    return render(request, self.template_name, altpost)
                else:
                    raise ValueError("template_name is not set")
            else:
                return altpost
            
    def altget(self, request, *args, **kwargs):
        return Http404()

    def altpost(self, request, *args, **kwargs):
        return Http404()

    def jsonpost(self, request, *args, **kwargs):
        return Http404()

    class Meta:
        abstract = True