from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework import serializers

from .models import Book
from .serializers import BookSerializer


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_year"]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["published_year", "author"]
    search_fields = ["title", "author"]
    ordering_fields = ["published_year", "created_at", "title"]
    ordering = ["-created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer
        return BookSerializer
