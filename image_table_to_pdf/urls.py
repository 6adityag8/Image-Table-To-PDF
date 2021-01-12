from django.urls import path, include

from api import urls as api_url

urlpatterns = [
    path('api/', include(api_url)),
]
