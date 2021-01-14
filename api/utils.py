import os

import pdfkit
from django.conf import settings
from django.template.loader import get_template


def create_pdf_file(data):
    """
    Generates a PDF file using pdfkit package. It creates a HTML string and then convert it into PDF
    :param data: Querydict which contains the table & image data
    :return: file name of the generated pdf
    """
    # Get the PDF template
    template = get_template("pdf_template.html")

    # Creating a list of lists of the table data
    table_data = []
    for row in range(1, int(data.get('row', '0')) + 1):
        row_data = []
        for column in range(1, int(data.get('column', '0')) + 1):
            # Fetching the corresponding cell's value
            cell_value = data.get('table_data[{0}_{1}]'.format(str(row), str(column)), '')
            row_data.append(cell_value)
        table_data.append(row_data)

    # Renders the template with the context data
    context = {
        'image_path': data.get('image_path', ''),
        'table_data': table_data,
    }
    # getting html file as string
    html_string = template.render(context)

    # Creates the MEDIA ROOT directory if it doesn't exist
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)

    file_name = 'created_pdf.pdf'
    # Getting the path where the uploaded file will be saved
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    pdfkit.from_string(html_string, pdf_file_path, css=os.path.join(settings.STATIC_ROOT, 'home/css/index.css'))

    return file_name


def save_uploaded_file(image_file):
    """
    Saves the uploaded image in MEDIA_ROOT.
    :param image_file: file object received from frontend through POST request
    :return: path of the saved file
    """
    # Creates the MEDIA ROOT directory if it doesn't exist
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)

    # Getting the path where the uploaded file will be saved
    image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)

    with open(image_path, 'wb+') as destination:
        # handle the case when size of the image is over than 2.5 Mb
        if image_file.multiple_chunks:
            for chunk in image_file.chunks():
                destination.write(chunk)
        else:
            destination.write(image_file.read())

    return image_path
