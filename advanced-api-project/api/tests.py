from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Clean Code",
            author=self.author,
            publication_year=2008,
        )

        self.user = User.objects.create_user(username="user", password="pass12345")
        self.admin = User.objects.create_superuser(
            username="admin", password="pass12345", email="admin@example.com"
        )

    def test_list_books_returns_200(self):
        res = self.client.get("/api/books/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_detail_book_returns_200(self):
        res = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_book_requires_auth(self):
        res = self.client.post(
            "/api/books/create/",
            {"title": "New Book", "author": self.author.id, "publication_year": 2020},
            format="json",
        )
        self.assertIn(res.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_authenticated_user_can_create_book(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.post(
            "/api/books/create/",
            {"title": "New Book", "author": self.author.id, "publication_year": 2020},
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_only_admin_can_update_book(self):
        # normal user denied
        self.client.force_authenticate(user=self.user)
        res = self.client.patch(
            f"/api/books/update/{self.book.id}/",
            {"title": "Hacked"},
            format="json",
        )
        self.assertIn(res.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

        # admin allowed
        self.client.force_authenticate(user=self.admin)
        res = self.client.patch(
            f"/api/books/update/{self.book.id}/",
            {"title": "Updated"},
            format="json",
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_only_admin_can_delete_book(self):
        # admin allowed
        self.client.force_authenticate(user=self.admin)
        res = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
