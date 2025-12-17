from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class TestBookViews(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Clean Code",
            author=self.author,
            publication_year=2008,
        )
        self.user = User.objects.create_user(username="user", password="pass12345")
        self.admin = User.objects.create_superuser(
            username="admin", password="pass12345", email="admin@example.com"
        )

    def test_list_books_returns_200_and_data(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ALX expects this string:
        self.assertIsInstance(response.data, list)

    def test_detail_book_returns_200_and_has_id(self):
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.book.id)

    def test_authenticated_user_can_create_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            "/api/books/create/",
            {"title": "New Book", "author": self.author.id, "publication_year": 2020},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_admin_can_update_book(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            f"/api/books/update/{self.book.id}/",
            {"title": "Updated"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated")

    def test_admin_can_delete_book(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
