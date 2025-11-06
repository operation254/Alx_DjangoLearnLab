# Retrieve

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
print(book.title, book.author, book.publication_year)
# Expected output: 1984 George Orwell 1949
```
