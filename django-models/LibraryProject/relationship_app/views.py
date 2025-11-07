from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book
from .models import Library

# --- Task 1 views (kept) ---
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# --- Task 2: registration view ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")  # or wherever you prefer
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile

def is_role(user, role):
    if not user.is_authenticated:
        return False
    try:
        return user.userprofile.role == role
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(lambda u: is_role(u, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: is_role(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: is_role(u, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
# --- role checks ---
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, "profile") and user.profile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == "Librarian"

def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Admin view: only users with the 'Admin' role can access.")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Librarian view: only users with the 'Librarian' role can access.")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Member view: only users with the 'Member' role can access.")
