from django.urls import path

from apps.ejecucion import views

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

]