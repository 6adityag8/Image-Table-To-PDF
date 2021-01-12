from django.urls import path

from .views import create_pdf_api

urlpatterns = [
    path('', create_pdf_api, name='create_pdf_api'),
]
