# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title)
# Output: 1984
