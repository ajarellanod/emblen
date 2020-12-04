from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout

from braces.views import LoginRequiredMixin


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
            return render(request, self.template_name, {"error": True})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("usuarios:login")