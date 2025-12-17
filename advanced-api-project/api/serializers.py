from datetime import date
from rest_framework import serializers
from api.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "publication_year", "created_at"]

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value < 1400 or value > current_year:
            raise serializers.ValidationError("Invalid publication_year")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
