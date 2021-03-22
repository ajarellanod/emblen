from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin

from django.template import RequestContext
from django.views.defaults import page_not_found

from django.contrib.auth.models import User

from apps.base.views import (
    EmblenFormView
)

from apps.usuarios.forms import (
    UserForm
)


def mi_error_404(request, exception):
    nombre_template = 'usuarios/404.html'

    if request.path.startswith('/'):
        nombre_template = 'usuarios/404.html'
    elif request.path.startswith('/formulacion'):
        nombre_template = 'usuarios/404.html'

    return page_not_found(request,exception, template_name=nombre_template)


def mi_error_500(request, *args, **argv):
    nombre_template = 'usuarios/500.html'

    if request.path.startswith('/'):
        nombre_template = 'usuarios/500.html'
    elif request.path.startswith('/formulacion'):
        nombre_template = 'usuarios/500.html'

    return page_not_found(request,exception, template_name=nombre_template)

class PrincipalView(LoginRequiredMixin, View):

    template_name = "usuarios/principal.html"

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):

    template_name = "usuarios/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("usuarios:principal")
        else:
            return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            if not remember:
                request.session.set_expiry(2592000)
            login(request, user)
            return redirect("usuarios:principal")
        else:
            return render(request, self.template_name, {"error": True})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("usuarios:login")


class UserView(LoginRequiredMixin, EmblenFormView):
    template_name = "usuarios/perfil.html"
    form_class = UserForm
    update_form = True
    success_url = "usuarios:principal"
    

    def get_data(self, data, instance):
        new_data = data.copy()
        if data['password'] == '':
            new_data.update({
                "password": instance.password
            })
        else:
            nueva_clave = make_password(data['password'])
            new_data.update({
                "password": nueva_clave
            })
        return super().get_data(new_data, instance)