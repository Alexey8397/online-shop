from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
#django_auth/urls.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('users.urls')),
    path('basket/', include("basket.urls", namespace='basket')),
    path('', include('myshop.urls', namespace='shop')),
    path('api/', include("myshop_api.urls")),

    path('api-auth/', include('rest_framework.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)