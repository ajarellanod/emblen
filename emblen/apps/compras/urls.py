from django.urls import path

from apps.compras import views

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

]