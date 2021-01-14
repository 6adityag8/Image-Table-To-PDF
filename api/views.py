from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import create_pdf_file


@api_view(['POST'])
def create_pdf_api(request):
    try:
        pdf_path = create_pdf_file(request.data)
        return Response({'created_pdf': pdf_path}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
