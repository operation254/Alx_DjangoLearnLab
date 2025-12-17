from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


class LatestBooksView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by("-created_at")[:5]
