from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from api import urls as api_url
from home import urls as home_url

urlpatterns = [
                  path('', include(home_url)),
                  path('api/', include(api_url)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
