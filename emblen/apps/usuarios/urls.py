from django.urls import path

from apps.usuarios import views
 
from django.conf.urls import handler404
from apps.usuarios.views import mi_error_404,mi_error_500


urlpatterns = [
    path("", views.PrincipalView.as_view(), name="principal"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("perfil/<int:pk>/", views.UserView.as_view(), name="perfil"),    
]

handler404 = mi_error_404
handler500 = mi_error_500