from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books, LibraryDetailView,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book,
    register,
)

urlpatterns = [
    # Authentication
    path("login/",  LoginView.as_view(template_name="relationship_app/login.html"),  name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),

    # Books & libraries
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Role-based views
    path("roles/admin/", admin_view, name="admin_view"),
    path("roles/librarian/", librarian_view, name="librarian_view"),
    path("roles/member/", member_view, name="member_view"),

    # Permission-protected CRUD
    path("books/add/", add_book, name="add_book"),
    path("books/<int:pk>/edit/", edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", delete_book, name="delete_book"),
]
