"""buy_and_sell_auto URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('auto.urls'), name='auto-urls'),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    ]
