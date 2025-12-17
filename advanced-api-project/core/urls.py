from django.urls import path
from rest_framework.routers import DefaultRouter

from .custom_views import LatestBooksView
from .views import BookViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    path("books-latest/", LatestBooksView.as_view()),
]
urlpatterns += router.urls
