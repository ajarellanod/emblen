from django.urls import path

from apps.contabilidad import views

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),
]