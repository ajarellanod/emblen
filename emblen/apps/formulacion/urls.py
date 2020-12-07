from django.urls import path

from apps.formulacion import views

urlpatterns = [
    path("partidas/", views.PartidaView.as_view(), name="partidas"),
]