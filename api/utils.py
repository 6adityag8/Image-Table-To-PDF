import os
import subprocess

import pdfkit
from django.conf import settings
from django.template.loader import get_template


def create_pdf_file(data):
    # creating html file as string to covert it into pdf using pdfkit package.
    template = get_template("pdf_template.html")

    # Renders the template with the context data.
    table_data = []
    for row in range(1, int(data.get('row', '0')) + 1):
        row_data = []
        for column in range(1, int(data.get('column', '0')) + 1):
            cell_value = data.get('table_data[{0}_{1}]'.format(str(row), str(column)), '')
            row_data.append(cell_value)
        table_data.append(row_data)
    context = {
        'image_path': data.get('image_path', ''),
        'table_data': table_data,
    }
    html_string = template.render(context)

    # Creates the MEDIA ROOT directory if it doesn't exist
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)

    file_name = 'created_pdf.pdf'
    # Getting the path where the uploaded file will be saved
    pdf_file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    # loading wkhtmltopdf path on heroku and passing it as config to pdfkit
    if 'DYNO' in os.environ:
        WKHTMLTOPDF_CMD = subprocess.Popen(
            ['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')],
            # we default to 'wkhtmltopdf' as the binary name
            stdout=subprocess.PIPE).communicate()[0].strip()
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
        pdfkit.from_string(html_string, pdf_file_path, configuration=config)
    else:
        pdfkit.from_string(html_string, pdf_file_path)

    return file_name
