# biblioteka/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # OSOBA
    path("osoby/", views.osoba_list, name="osoba-list"),
    path("osoby/create/", views.osoba_create, name="osoba-create"),
    path("osoby/<int:pk>/", views.osoba_detail, name="osoba-detail"),
    path("osoby/szukaj/<str:tekst>/", views.osoba_filter_by_nazwisko, name="osoba-szukaj"),

    # STANOWISKO
    path("stanowiska/", views.stanowisko_list, name="stanowisko-list"),
    path("stanowiska/create/", views.stanowisko_create, name="stanowisko-create"),
    path("stanowiska/<int:pk>/", views.stanowisko_detail, name="stanowisko-detail"),
]
