from django.contrib import admin
# from baton.autodiscover import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
]
