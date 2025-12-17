from django.urls import path
from api.views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path("books/", ListView.as_view(), name="book-list"),
    path("books/<int:pk>/", DetailView.as_view(), name="book-detail"),
    path("books/create/", CreateView.as_view(), name="book-create"),

    # ALX expects these exact substrings: books/update and books/delete
    path("books/update/<int:pk>/", UpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>/", DeleteView.as_view(), name="book-delete"),
]
