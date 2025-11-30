from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required

from .models import Book
from .forms import BookForm


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    """List all books – only for users with can_view."""
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    """Create a book – only for users with can_create."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    """Edit a book – only for users with can_edit."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    """Delete a book – only for users with can_delete."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(
        request,
        "bookshelf/confirm_delete.html",  # you can create this simple template
        {"book": book},
    )

