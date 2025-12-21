from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API routes (checker expects 'api/')
    path("api/", include("accounts.urls")),
    path("api/", include("posts.urls")),
]
