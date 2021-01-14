from django.shortcuts import render

from .forms import UploadImageForm, TABLE_SIZE


def index(request):
    form = UploadImageForm()
    context = {
        'form': form,
        'table_sizes': range(1, TABLE_SIZE + 1)
    }
    template_name = 'index.html'
    return render(request, template_name, context)
