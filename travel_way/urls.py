from django.contrib import admin
from django.urls import path
from main.views import index, countries, country, tour, tours, sign_up, log_out, log_in, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('countries', countries),
    path('tours', tours),
    path('country/<int:id>', country),
    path('tour/<int:id>', tour),
    path('signup', sign_up),
    path('logout', log_out),
    path('login', log_in),
    path('profile', profile)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
