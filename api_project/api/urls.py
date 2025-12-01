from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView from Task 1
    path('books/', BookList.as_view(), name='book-list'),

    # Token auth endpoint
    path('token/', obtain_auth_token, name='api-token'),

    # All CRUD routes from the ViewSet
    path('', include(router.urls)),
]
