# Delete a Book
book = Book.objects.get(id=1)
book.delete()
