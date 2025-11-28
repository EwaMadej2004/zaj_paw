from rest_framework import serializers
from .models import Book, Author, Genre, MONTHS, BOOK_FORMATS, Osoba, Stanowisko
from rest_framework.validators import UniqueTogetherValidator

# -----------------------
# Serializer dla Book itd.
# -----------------------

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_month', 'book_format', 'author', 'genre', 'available_copies']
        read_only_fields = ['id']

    def validate_title(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Tytuł książki powinien rozpoczynać się wielką literą!"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Author.objects.all(),
                fields=['first_name', 'last_name']
            )
        ]

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        country = data.get('country')

        if first_name and not first_name.istitle():
            raise serializers.ValidationError(
                {"first_name": "Imię powinno rozpoczynać się wielką literą!"}
            )

        if last_name and not last_name.istitle():
            raise serializers.ValidationError(
                {"last_name": "Nazwisko powinno rozpoczynać się wielką literą!"}
            )

        if country and (len(country) != 2 or not country.isupper()):
            raise serializers.ValidationError(
                {"country": "Kod kraju musi składać się z 2 wielkich liter, np. 'PL'."}
            )

        return data

# -----------------------
# Funkcja walidująca dla Genre
# -----------------------
def multiple_of_two(value):
    """Walidator: liczba powinna być wielokrotnością 2."""
    if value % 2 != 0:
        raise serializers.ValidationError("Ocena popularności musi być wielokrotnością 2 (np. 0,2,4,6,8,10).")

class GenreSerializer(serializers.ModelSerializer):
    popularity_rank = serializers.IntegerField(validators=[multiple_of_two])

    class Meta:
        model = Genre
        fields = "__all__"

# -----------------------
# Serializery dla Osoba i Stanowisko (zadanie 3)
# -----------------------

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = "__all__"


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = "__all__"
