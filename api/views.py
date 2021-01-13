import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import create_pdf_file

logger = logging.getLogger('api_logger')


@api_view(['POST'])
def create_pdf_api(request):
    try:
        pdf_path = create_pdf_file(request.data)
        return Response({'created_pdf': pdf_path}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.exception(e)
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
