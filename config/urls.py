from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from products.views import deploy

urlpatterns = [
    path("my-webhook/", deploy, name="deploy"),
]
