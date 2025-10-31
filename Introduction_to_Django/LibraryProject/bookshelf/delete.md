# Delete

```python
from bookshelf.models import Book
Book.objects.filter(title="Nineteen Eighty-Four", author="George Orwell", publication_year=1949).delete()
print(list(Book.objects.all()))
# Expected output: []
```
