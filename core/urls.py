from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("auth/", include("djoser.urls")),
        path("auth/", include("djoser.urls.jwt")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

# add adminurl path based on environment
if settings.DEBUG == True:
    urlpatterns += (path("admin/", admin.site.urls),)
