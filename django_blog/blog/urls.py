from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Posts
    path("", views.PostListView.as_view(), name="post_list"),          # home
    path("posts/", views.PostListView.as_view(), name="posts_list"),   # optional alias
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # Comments
    path("posts/<int:post_id>/comments/new/", views.CommentCreateView.as_view(), name="comment_create"),
    path("comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment_edit"),
    path("comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),

    # Tags + Search
    path("tags/<slug:tag_slug>/", views.tag_posts_view, name="tag_posts"),
    path("search/", views.search_view, name="search"),

    # Auth
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", views.register_view, name="register"),
    path("profile", views.profile_view, name="profile"),
]
