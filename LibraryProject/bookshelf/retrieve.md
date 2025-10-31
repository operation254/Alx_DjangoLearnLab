# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
print([book.title for book in books])
# Output: ["1984"]
