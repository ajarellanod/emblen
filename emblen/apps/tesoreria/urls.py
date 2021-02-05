from django.urls import path

from apps.tesoreria import views

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

]