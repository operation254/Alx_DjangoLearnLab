# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve a single book by ID
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
