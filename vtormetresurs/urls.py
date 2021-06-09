from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('', include('vtormet.urls')),
    path('signin/', Signin.as_view(), name='signin_url'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
