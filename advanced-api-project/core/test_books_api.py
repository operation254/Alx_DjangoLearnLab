import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from core.models import Book


@pytest.mark.django_db
def test_anonymous_cannot_create_book():
    client = APIClient()
    res = client.post(
        "/api/books/",
        {"title": "Nope", "author": "Anon", "published_year": 2020},
        format="json",
    )
    assert res.status_code in (401, 403)


@pytest.mark.django_db
def test_authenticated_can_create_book():
    user = User.objects.create_user(username="kevin", password="pass12345")
    client = APIClient()
    client.force_authenticate(user=user)

    res = client.post(
        "/api/books/",
        {"title": "Yep", "author": "Auth", "published_year": 2020},
        format="json",
    )
    assert res.status_code == 201
    assert Book.objects.filter(title="Yep").exists()


@pytest.mark.django_db
def test_list_books_uses_list_serializer_fields():
    Book.objects.create(title="A", author="X", published_year=2020)
    client = APIClient()
    res = client.get("/api/books/")
    assert res.status_code == 200

    item = res.json()[0]
    assert "title_upper" not in item
    assert "created_at" not in item
    assert {"id", "title", "author", "published_year"}.issubset(item.keys())


@pytest.mark.django_db
def test_detail_book_has_extra_fields():
    book = Book.objects.create(title="Clean Code", author="Robert", published_year=2008)
    client = APIClient()
    res = client.get(f"/api/books/{book.id}/")
    assert res.status_code == 200

    data = res.json()
    assert data["title_upper"] == "CLEAN CODE"
    assert "created_at" in data


@pytest.mark.django_db
def test_filter_books_by_year():
    Book.objects.create(title="A", author="X", published_year=2020)
    Book.objects.create(title="B", author="Y", published_year=2021)

    client = APIClient()
    res = client.get("/api/books/?published_year=2021")
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["published_year"] == 2021


@pytest.mark.django_db
def test_search_books():
    Book.objects.create(title="Django for APIs", author="William", published_year=2022)
    Book.objects.create(title="Other", author="Someone", published_year=2010)

    client = APIClient()
    res = client.get("/api/books/?search=django")
    assert res.status_code == 200
    assert len(res.json()) == 1


@pytest.mark.django_db
def test_latest_books_endpoint():
    Book.objects.create(title="Old", author="A", published_year=2000)
    Book.objects.create(title="New", author="B", published_year=2001)

    client = APIClient()
    res = client.get("/api/books-latest/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
