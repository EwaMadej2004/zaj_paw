# biblioteka/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters

# ---------- OSOBA ----------

# ---------- OSOBA (Refaktoryzacja na CBV) ----------

class OsobaListCreateAPIView(ListCreateAPIView):
    """
    Obsługuje:
    1. GET /api/osoby/ (Lista)
    2. POST /api/osoby/ (Tworzenie - zastępuje osoba_create)
    3. GET /api/osoby/?search=tekst (Wyszukiwanie - zastępuje osoba_filter_by_nazwisko)
    """
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    # Konfiguracja wyszukiwania (filtrowanie po nazwisku)
    filter_backends = [filters.SearchFilter]
    search_fields = ['nazwisko'] 


class OsobaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Obsługuje:
    1. GET /api/osoby/<pk>/ (Szczegóły - zastępuje GET z osoba_detail)
    2. PUT /api/osoby/<pk>/ (Pełna aktualizacja)
    3. PATCH /api/osoby/<pk>/ (Częściowa aktualizacja)
    4. DELETE /api/osoby/<pk>/ (Usuwanie - zastępuje DELETE z osoba_detail)
    """
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer




# ---------- STANOWISKO ----------

@api_view(["GET"])
def stanowisko_list(request):
    """GET /api/stanowiska/ - lista stanowisk"""
    stanowiska = Stanowisko.objects.all()
    serializer = StanowiskoSerializer(stanowiska, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def stanowisko_create(request):
    """POST /api/stanowiska/create/ - tworzenie stanowiska"""
    serializer = StanowiskoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
def stanowisko_detail(request, pk):
    """GET /api/stanowiska/<pk>/ - pobierz; DELETE /api/stanowiska/<pk>/ - usuń"""
    try:
        st = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StanowiskoSerializer(st)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

