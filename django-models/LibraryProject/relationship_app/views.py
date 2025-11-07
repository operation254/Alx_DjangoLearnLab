from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

from .models import Book, Library, UserProfile

# ----- Task 1 -----
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# ----- Task 2 -----
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# ----- Task 3: role-based -----
def _has_role(user, role):
    if not user.is_authenticated:
        return False
    try:
        return user.userprofile.role == role   # NOTE: user.userprofile
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(lambda u: _has_role(u, "Admin"))
def admin_view(request):
    return HttpResponse("Admin view: only Admins can access.")

@user_passes_test(lambda u: _has_role(u, "Librarian"))
def librarian_view(request):
    return HttpResponse("Librarian view: only Librarians can access.")

@user_passes_test(lambda u: _has_role(u, "Member"))
def member_view(request):
    return HttpResponse("Member view: only Members can access.")
