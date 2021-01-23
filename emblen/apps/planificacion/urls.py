from django.urls import path, include

from apps.planificacion import views


urlpatterns = [
        path('', views.PrincipalView.as_view(), name='principal'),
]