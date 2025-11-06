# Update

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected output: Nineteen Eighty-Four
```
