from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('video/', include('video.urls')),
    path('accounts/', include('accounts.urls')),
    path('questions/', include('questions.urls')),
    path('predication/', include('predication.urls')),
    path('forum/', include('forum.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)