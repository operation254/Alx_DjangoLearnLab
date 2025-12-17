import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Author, Book


@pytest.mark.django_db
def test_create_book():
    author = Author.objects.create(name="Tester")

    user = User.objects.create_user(username="tester", password="pass12345")
    client = APIClient()
    client.force_authenticate(user=user)

    res = client.post(
        "/api/books/",
        {"title": "Test Book", "author": author.id, "publication_year": 2020},
        format="json",
    )
    assert res.status_code == 201, res.json()
    assert Book.objects.filter(title="Test Book").exists()

@pytest.mark.django_db
def test_list_books():
    author = Author.objects.create(name="A1")
    Book.objects.create(title="A", author=author, publication_year=2020)

    client = APIClient()
    res = client.get("/api/books/")
    assert res.status_code == 200
    assert len(res.json()) >= 1


@pytest.mark.django_db
def test_detail_book():
    author = Author.objects.create(name="Robert")
    book = Book.objects.create(title="Clean Code", author=author, publication_year=2008)

    client = APIClient()
    res = client.get(f"/api/books/{book.id}/")
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "Clean Code"
    assert data["publication_year"] == 2008


@pytest.mark.django_db
def test_filter_books_by_publication_year():
    author = Author.objects.create(name="X")
    Book.objects.create(title="A", author=author, publication_year=2020)
    Book.objects.create(title="B", author=author, publication_year=2021)

    client = APIClient()
    res = client.get("/api/books/?publication_year=2021")
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["publication_year"] == 2021


@pytest.mark.django_db
def test_search_books():
    author = Author.objects.create(name="William")
    Book.objects.create(title="Django for APIs", author=author, publication_year=2022)
    Book.objects.create(title="Other", author=author, publication_year=2010)

    client = APIClient()
    res = client.get("/api/books/?search=django")
    assert res.status_code == 200
    assert len(res.json()) == 1


@pytest.mark.django_db
def test_author_has_nested_books():
    author = Author.objects.create(name="Nested Author")
    Book.objects.create(title="One", author=author, publication_year=2000)

    client = APIClient()
    res = client.get(f"/api/authors/{author.id}/")
    assert res.status_code == 200
    data = res.json()
    assert "books" in data
    assert len(data["books"]) == 1
