from django.http import JsonResponse
from django.shortcuts import render

from .forms import UploadImageForm, TABLE_SIZE
from .utils import save_uploaded_file


def index(request):
    form = UploadImageForm()
    context = {
        'form': form,
        'table_sizes': range(1, TABLE_SIZE + 1)
    }
    template_name = 'index.html'
    return render(request, template_name, context)


def upload_image(request):
    if request.method == 'POST' and request.is_ajax():
        form = UploadImageForm(request.FILES)
        if form.is_valid():
            uploaded_file = save_uploaded_file(request.FILES['image_upload'])
            return JsonResponse({'uploaded_file': uploaded_file})

    return JsonResponse({'error': 'Something went wrong.'})
