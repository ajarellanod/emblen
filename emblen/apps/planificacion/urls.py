from django.urls import path, include

from apps.planificacion import views


urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),
    path('modificacion/', views.ModificacionView.as_view(), name='modificacion'),
]