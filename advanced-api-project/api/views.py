from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["publication_year", "author"]
    search_fields = ["title", "author__name"]
    ordering_fields = ["publication_year", "created_at", "title"]
    ordering = ["-created_at"]
