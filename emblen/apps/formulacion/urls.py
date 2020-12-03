from django.urls import path

from apps.formulacion import views

urlpatterns = [
        path("formulacion/", views.PartidaView.as_view(), name="formulacion"),
]