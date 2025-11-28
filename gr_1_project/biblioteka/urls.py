# biblioteka/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # OSOBA
    path("osoby/", views.OsobaListCreateAPIView.as_view(), name="osoba-list-create"),
    path("osoby/<int:pk>/", views.OsobaRetrieveUpdateDestroyAPIView.as_view(), name="osoba-detail-update-delete"),

    # STANOWISKO
    path("stanowiska/", views.stanowisko_list, name="stanowisko-list"),
    path("stanowiska/create/", views.stanowisko_create, name="stanowisko-create"),
    path("stanowiska/<int:pk>/", views.stanowisko_detail, name="stanowisko-detail"),
]
