from datetime import date
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    title_upper = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "title_upper", "author", "published_year", "created_at"]

    def get_title_upper(self, obj: Book) -> str:
        return obj.title.upper()

    def validate_published_year(self, value: int) -> int:
        current_year = date.today().year
        if value < 1400 or value > current_year:
            raise serializers.ValidationError("published_year must be realistic.")
        return value
