from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginView(View):

    template_name = "usuarios/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/exitoso/")
        else:
            return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return redirect("/exitoso/")
        else:
            return render(request, self.template_name)


@method_decorator(login_required, name="dispatch")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("usuarios:login")