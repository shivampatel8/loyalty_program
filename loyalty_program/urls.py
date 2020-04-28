from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('loyalty/', include('loyalty.urls')),
    path('admin/', admin.site.urls),
]