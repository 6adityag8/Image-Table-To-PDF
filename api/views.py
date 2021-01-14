from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import create_pdf_file, save_uploaded_file


@api_view(['POST'])
def create_pdf_api(request):
    try:
        pdf_path = create_pdf_file(request.data)
        return Response({'created_pdf': pdf_path}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def upload_image(request):
    try:
        uploaded_file = save_uploaded_file(request.FILES['image_upload'])
        return Response({'uploaded_file': uploaded_file}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
