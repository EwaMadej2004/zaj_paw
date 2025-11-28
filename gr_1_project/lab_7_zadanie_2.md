from biblioteka.models import Osoba, Stanowisko

# 1. Wyświetl wszystkie obiekty modelu Osoba
Osoba.objects.all()

# 2. Wyświetl obiekt Osoba z id = 3
Osoba.objects.get(id=3)

# 3. Wyświetl osoby, których nazwisko zaczyna się na "K"
Osoba.objects.filter(nazwisko__startswith="K")

# 4. Wyświetl unikalną listę stanowisk przypisanych do Osoba
Osoba.objects.values("stanowisko").distinct()

# 5. Nazwy stanowisk posortowane malejąco
Stanowisko.objects.order_by("-nazwa").values("nazwa")

# 6. Dodaj nową osobę
st = Stanowisko.objects.first()
Osoba.objects.create(imie="Anna", nazwisko="Testowa", plec="K", stanowisko=st)
