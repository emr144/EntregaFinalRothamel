from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("admin/",admin.site.urls),
    path("app/",include("AppProyectoFinal.urls")),
    path("start/",include('Startapp.urls')),
    path('chpp/', include('chatapp.urls')),
  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])