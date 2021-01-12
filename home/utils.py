import os

from django.conf import settings


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
