from django.urls import path

from .views import create_pdf_api, upload_image

urlpatterns = [
    path('', create_pdf_api, name='create_pdf_api'),
    path('upload_image/', upload_image, name='upload_image'),
]
