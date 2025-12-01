from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    Task 1: simple read-only endpoint to list all books.
    Public (no auth required).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Task 2 + 3:
    - Full CRUD for Book
    - Protected by TokenAuthentication + IsAuthenticated
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
