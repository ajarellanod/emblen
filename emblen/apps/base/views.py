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
        if isinstance(self.template_name, str):
            return render(request, self.template_name)
        else: 
            raise ValueError("template_name is not set")

    def altpost(self, request, *args, **kwargs):
        raise Http404()

    def jsonpost(self, request, *args, **kwargs):
        raise Http404()

    class Meta:
        abstract = True


class EmblenDeleteView(View):

    model = False
    success_url = False

    def get(self, request, *args, **kwargs):
        if self.model and self.success_url:
            obj = get_object_or_404(self.model, pk=kwargs["pk"])
            obj.eliminar()
            return redirect(self.success_url)
        else:
            raise ValueError("Model and/or SuccessURL don't set")

    def post(self, request, *args, **kwargs):
        raise Http404()

    class Meta:
        abstract = True


class EmblenFormView(EmblenView):
    
    form_class = False
    success_url = False
    update_form = False
    instance_model = False

    def validate_attrs(self):
        if not self.form_class and not self.success_url:
            raise ValueError("Form and/or SuccessURL don't set")

        if self.update_form:
            self.instance_model = self.form_class._meta.model
            return True
        else:
            return False

    def get_form(self, form):
        self.form_class = form
        return self.form_class

    def get_data(self, data, instance=False):
        if not instance:
            return {'data': data}

        return {'instance': instance, 'data': data}

    def altget(self, request, *args, **kwargs):
        if self.validate_attrs():
            obj = get_object_or_404(self.instance_model, pk=kwargs["pk"])
            form = self.form_class(instance=obj)
        else:
            form = self.form_class()

        return {"form": self.get_form(form)}

    def altpost(self, request, *args, **kwargs):
        if self.validate_attrs():
            obj = get_object_or_404(self.instance_model, pk=kwargs["pk"])
            form = self.form_class(**self.get_data(request.POST, instance=obj))
        else:
            form = self.form_class(**self.get_data(request.POST))

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        return {"form": form}


class EmblenReport(View):
    view_template = False
    report_template = False
    with_modal = False

    def validate_attrs(self):
        if not self.view_template and not self.report_template:
            raise AttributeError("EmblenReport attributes are not set.")

    def send_response(self, request, response, method="get"):
        self.validate_attrs() # Validate all need attrs are set
        if isinstance(response, dict):
            if method == "get": 
                return render(request, self.view_template, response)
            elif method == "post":
                return render(request, self.report_template, response)
            else:
                raise Http404()
        else:            
            return response

    def get(self, request, *args, **kwargs):
        response = self.altget(request, *args, **kwargs)
        return self.send_response(request, response)

    def post(self, request, *args, **kwargs):
        response = self.altpost(request, *args, **kwargs)
        return self.send_response(request, response, method="post")
            
    def altget(self, request, *args, **kwargs):
        if self.with_modal:
            raise Http404()
        return render(request, self.view_template)

    def altpost(self, request, *args, **kwargs):
        raise Http404()

    class Meta:
        abstract = True