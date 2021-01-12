import os

import pdfkit
from django.conf import settings
from django.template.loader import get_template


def create_pdf_file(data):
    # creating html file as string to covert it into pdf using pdfkit package.
    template = get_template("pdf_template.html")

    # Renders the template with the context data.
    html_string = template.render(data)

    # Creates the MEDIA ROOT directory if it doesn't exist
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)

    file_name = 'created_pdf.pdf'
    # Getting the path where the uploaded file will be saved
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    pdfkit.from_string(html_string, pdf_file_path)

    return file_name
