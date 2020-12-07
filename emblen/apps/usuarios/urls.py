from django.urls import path

from apps.usuarios import views

urlpatterns = [
    path("", views.PrincipalView.as_view(), name="principal"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]