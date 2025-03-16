from django.contrib import admin
from django.urls import path, include
from accounts.views import custom_404_view
from django.conf.urls import handler404


handler404 = custom_404_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('events.urls')),
    path('account/', include('accounts.urls')),
]
